from model.model import Orders, Area, City, Customers, Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, desc, asc

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
        orders = session.query(Orders).filter(Orders.status == 'В архиве').order_by(Orders.created_at.asc()).all()

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


def create_city(city_name: str, areas: dict):
    with Session() as session:
        city = City(
            name=city_name.replace(',', '')
            )
        session.add(city)
        session.flush()

        for name, count in areas.items():
            area = Area(
                name=name,
                count=count[0],
                limit=count[1]
            )
            session.add(area)
            session.flush()
            area.update_remainder(session)

            city.areas.append(area)

        city.update_limit(session)
        city.update_count(session)
        city.update_remainder(session)
        city.update_status(session)
        session.commit()

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
                        cities[city.name].update({area.name: [area.count, area.limit, area.remainder]})

                order_info = {'customer_name': order.customer.name,
                                'type': order.type,
                                'datetime': order.created_at,
                                'status': order.status,
                                'cities': cities,
                                'limit': order.limit,
                                'count': order.count,
                                'remainder': order.remainder,
                                }
                return order_info
            return False
        except Exception as e:
            return False


def change_order(id: int, data: dict, customer: str):
    with Session() as session:
        try:
            order = session.query(Orders).filter_by(id=id).first()

            if order and data:
                for city in order.cities:
                    find_city = data.get(city.name)
                    for area in city.areas:
                        find_area = find_city.get(area.name)
                        if find_area:
                            print(find_area[0])
                            area.count = find_area[0]
                            area.limit = find_area[1]
                            area.update_remainder(session)
                            city.update_count(session)
                            city.update_limit(session)
                            city.update_remainder(session)
                            session.flush()
            order.update_limit(session)
            order.update_count(session)
            order.update_remainder(session)
            order.check_complete(session)
            session.commit()
            return True
        except Exception as e:
            return False