from model.model import Orders, Area, City, Customers, Session, Type
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, desc, asc, or_


def get_all_orders():
    with Session() as session:
        orders = session.query(Orders).order_by(asc(Orders.created_at)).all()

        ready_orders = []
        for order in orders:
            order = (str(order.id), order.customer.name, order.status, str(order.count), str(order.limit), order.comment, order.type, ','.join([city.name for city in order.cities]), ','.join([area.name for city in order.cities for area in city.areas]))
            ready_orders.append(order)
        
        return ready_orders


def get_orders():
    with Session() as session:
        orders = session.query(Orders).filter(Orders.status == 'Выполняется').order_by(Orders.created_at.asc()).all()
        
        ready_orders = []
        for order in orders:
            order.update_limit(session)
            order.update_count(session)
            order.check_complete(session)
            order = (str(order.id), order.customer.name, order.status, str(order.count), str(order.limit), order.comment, order.type, ','.join([city.name for city in order.cities]), ','.join([area.name for city in order.cities for area in city.areas]))

            ready_orders.append(order)


        return ready_orders


def get_archive():
    with Session() as session:
        orders = session.query(Orders).filter(
            or_(Orders.status == 'В архиве', Orders.status == 'Выполнено')
        ).order_by(Orders.created_at.asc()).all()

        ready_orders = []
        for order in orders:
            order = (str(order.id), order.customer.name, order.status, str(order.count), str(order.limit), order.comment, order.type, ','.join([city.name for city in order.cities]), ','.join([area.name for city in order.cities for area in city.areas]))

            ready_orders.append(order)
        
        return ready_orders


def get_or_create_customer(customer_name: str):
    with Session() as session:
        customer = session.execute(select(Customers).where(Customers.name == customer_name)).scalar_one_or_none()
        if customer is None:
            customer = Customers(
                name=customer_name
            )

            session.add(customer)
            session.flush()
        session.commit()

        return customer


def create_city(city_name: str, areas: dict, session: Session = None):
    if session is None:
        session = Session()
    city = City(
        name=city_name
        )
    session.add(city)

    for name, count in areas.items():
        print(count[0], count[1], count[-1])
        area = Area(
            name=name,
            count=int(count[0]),
            limit=int(count[1]),
        )
        session.add(area)
        area.update_remainder(session)

        city.areas.append(area)

    session.commit()

    city.update_limit(session)
    city.update_count(session)
    city.update_remainder(session)
    city.update_status(session)

    if session is None:
        session.close()

    return city


def create_order(customer: str, type: str, data: dict):
    with Session() as session:
            customer_id = get_or_create_customer(customer_name=customer)
            all_cities = []
            for name, area in data.items():
                cities = create_city(city_name=name, areas=area)
                all_cities.append(cities)

            order = Orders(
                customer=customer_id,
                type=type,
            )

            session.add(order)
            session.flush()
            for city in all_cities:
                order.cities.append(city)

            order.update_limit(session)
            order.update_count(session)
            order.update_remainder(session)
            order.check_complete(session)

            session.commit()

def delete_order(id: int):
    with Session() as session:
        try:
            order = session.query(Orders).filter_by(id=id).first()

            if order:
                session.delete(order)
                session.commit()

                return True
            else:
                return False
        except SQLAlchemyError as e:
            print(f"An error occurred while deleting the order: {e}")
            return False
        

def archivate(id: int):
    with Session() as session:
        try:
            order = session.query(Orders).filter_by(id=id).first()

            if order:
                order.status = 'В архиве'

                session.commit()

                return True
            else:
                return False
        except Exception as e:
            return False


def change_status(id: int, status: str, comment: str):
    with Session() as session:
        try:
            order = session.query(Orders).filter_by(id=id).first()

            if order:
                order.status = status
                order.comment = comment

                session.commit()

                return True
            else:
                return False
        except Exception as e:
            return False
        

def get_order_info(id: int):
    with Session() as session:
        try:
            order = session.query(Orders).filter_by(id=id).first()

            if order:
                cities = {}

                for city in order.cities:
                    cities[city.name] = {}
                    cities[city.name].update({'Итого': [city.count, city.limit, city.remainder]})
                    for area in city.areas:
                        cities[city.name].update({area.name: [str(area.count), str(area.limit), str(area.remainder)]})

                order_info = {'id': order.id,
                                'customer_name': order.customer.name,
                                'type': order.type,
                                'datetime': order.created_at,
                                'status': order.status,
                                'cities': cities,
                                'limit': order.limit,
                                'count': order.count,
                                'remainder': order.remainder,
                                'comment': order.comment,
                                }
                return order_info
            return False
        except Exception as e:
            return False


def change_order(id: int, customer: str, status: str, type: str, comment: str):
    with Session() as session:
        try:
            order = session.query(Orders).filter_by(id=id).first()

            order.status = status
            order.type = type
            order.customer.name = customer
            order.comment = comment
            refresh()

            session.commit()

            return True
        except Exception as e:
            return False


def create_area(name: str, areas: list):
    with Session() as session:
        try:
            area = Area(
                name=name,
                count=areas[0],
                limit=areas[1],
            )


            session.add(area)
            session.flush()
            area.update_remainder(session)
            session.commit()
            return area
        except Exception as e:
            session.rollback()
            return False


def change_city(id: int, city_name, areas):
    with Session() as session:
        try:
            city = session.query(City).filter_by(id=id).first()

            if not city:
                city = create_city(city_name=city_name, areas=areas)
            else:
                for area_name, counts in areas.items():
                    area = create_area(name=area_name, areas=counts)
                    city.areas.append(area)

            session.commit()

        except Exception as e:
            session.rollback()
            return False

def refresh():
    with Session() as session:
        cities = session.query(City).all()
        for city in cities:
            city.update_remainder(session)
            city.update_count(session)
            city.update_limit(session)

        areas = session.query(Area).all()
        for area in areas:
            area.update_remainder(session)

        orders = session.query(Orders).all()
        for order in orders:
            order.update_remainder(session)
            order.update_count(session)
            order.update_limit(session)
            order.check_complete(session)


def add_areas(id: int, data: dict):
    '''Добавление города'''

    with Session() as session:
        try:
            order = session.query(Orders).filter_by(id=id).first()

            if not order:
                return

            # Создаем словарь для быстрого доступа к городам заказа
            existing_cities = {city.name: city for city in order.cities}

            for city_name, areas in data.items():
                if city_name in existing_cities:
                    # Обновляем существующий город
                    city = existing_cities[city_name]
                    city.update_areas(areas)
                else:
                    # Создаем новый город
                    print(areas)
                    city = create_city(city_name=city_name, areas=areas, session=session)
                    order.cities.append(city)

            session.commit()

            order.update_count(session)
            order.update_limit(session)
            order.update_remainder(session)
            order.check_complete(session)
            refresh()
        except Exception as e:
            print(e)
            session.rollback()
            return False

def create_type(name: str):
    with Session() as session:
        try:
            type = Type(
                name=name
            )

            session.add(type)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            return False


def get_types():
    with Session() as session:
        types = session.query(Type).all()

        return types


def delete_type(name: str):
    with Session() as session:
        try:
            session.delete(session.query(Type).filter_by(name=name).first())
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(e)
            return False