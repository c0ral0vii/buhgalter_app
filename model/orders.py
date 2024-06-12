from model.model import Orders, Area, City, Customers, Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, desc, asc

def get_all_orders():
    with Session() as session:
        orders = session.query(Orders).order_by(Orders.created_at.asc()).all()
        ready_orders = []
        for order in orders:
            order = (str(order.id), order.customer.name, order.status, order.type, order.cities[0].name, ','.join([area.name for area in order.areas]), str(order.count), str(order.limit))
            ready_orders.append(order)
        
        return ready_orders


def get_orders():
    with Session() as session:
        orders = session.query(Orders).filter(Orders.status == 'Выполняется').order_by(Orders.created_at.asc()).all()
        
        ready_orders = []
        for order in orders:
            order = (str(order.id), order.customer.name, order.status, order.type, order.cities[0].name, ','.join([area.name for area in order.areas]), str(order.count), str(order.limit))
            ready_orders.append(order)
        
        return ready_orders


def get_archive():
    with Session() as session:
        orders = session.query(Orders).filter(Orders.status == 'В архиве').order_by(Orders.created_at.asc()).all()

        ready_orders = []
        for order in orders:
            order = (str(order.id), order.customer.name, order.status, order.type, order.cities[0].name, ','.join([area.name for area in order.areas]), str(order.count), str(order.limit))
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


def get_or_create_city(citys: list):
    with Session() as session:
        all_cities = []

        for city_name in citys:
            city = session.execute(select(City).where(City.name == city_name)).scalar_one_or_none()
            if city is None:
                city = City(
                    name=city_name
                    )
                session.add(city)
                session.flush()  
                session.commit()

            all_cities.append(city)

        return all_cities


def create_area(areas: dict):
    with Session() as session:
        all_areas = []

        for area_name, area_count in areas.items():
            area = Area(
                name=area_name,
                count=0,
                limit=area_count
                )
            session.add(area)
            session.flush()
            session.commit()

            all_areas.append(area)
            
        return all_areas
    

def create_order(customer: str, type: str, city: list, area: dict):
    with Session() as session:
            customer_id = get_or_create_customer(customer_name=customer)
            citys_id = get_or_create_city(citys=city)

            if area is not None:
                areas_id = create_area(areas=area)

            order = Orders(
                customer=customer_id,
                type=type,
            )
            order.cities.extend(citys_id)
            if areas_id:
                order.areas.extend(areas_id)
            session.add(order)

            order.update_limit(session)

            session.commit()
            print(customer, area, city, type)


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
                order_info = {'customer_name': order.customer.name,
                                'type': order.type,
                                'datetime': order.created_at,
                                'status': order.status,
                                'city': [city.name for city in order.cities],
                                'areas': {area.name: [area.count, area.limit] for area in order.areas},
                                }
                print(order_info)
                return order_info
            return False
        except Exception as e:
            return False

def change_order(id: int, data: int):
    with Session() as session:
        try:
            order = session.query(Orders).filter_by(id=id).first()

            if order:
                session.commit()
                return True

            return False
        except Exception as e:
            return False