import datetime

from sqlalchemy import BigInteger, ForeignKey, create_engine, Table, Column, Integer, event
from sqlalchemy.orm import relationship, Mapped, mapped_column, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///database.db', echo=True)

Session = sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()


orders_cities = Table('orders_cities', Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id')),
    Column('city_id', Integer, ForeignKey('cities.id'))
)

cities_areas = Table('cities_areas', Base.metadata,
                Column('city_id', Integer, ForeignKey('cities.id')),

                     Column('area_id', Integer, ForeignKey('areas.id'))
                     )

class Customers(Base):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    orders: Mapped[list['Orders']] = relationship(back_populates='customer')


class Orders(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[str] = mapped_column(default=datetime.datetime.now(
                                                tz=datetime.timezone(
                                                    datetime.timedelta(hours=3)
                                            )))
    
    limit: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)
    count: Mapped[int] = mapped_column(default=0)
    remainder: Mapped[int] = mapped_column(default=0)

    type: Mapped[str] = mapped_column()

    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))

    status: Mapped[str] = mapped_column(default='Выполняется')
    comment: Mapped[str] = mapped_column(nullable=True)

    customer: Mapped['Customers'] = relationship(back_populates='orders')

    cities: Mapped[list['City']] = relationship(
        'City',
        secondary=orders_cities,
        back_populates='orders'
    )

    def update_limit(self, session):
        """Обновляет limit у заказа"""

        all_limit = []
        for city in self.cities:
            for area in city.areas:
                all_limit.append(area.limit)

        self.limit = sum(int(limit) for limit in all_limit)
        session.add(self)
        session.commit()

    def update_count(self, session):
        '''Обновляем count у заказа'''

        all_count = []
        for city in self.cities:
            for area in city.areas:
                all_count.append(area.count)

        self.count = sum(int(count) for count in all_count)
        session.add(self)
        session.commit()

    def update_remainder(self, session):
        '''Обновляем остаток у заказа'''

        self.remainder = int(self.limit) - int(self.count)
        session.add(self)
        session.commit()

    def check_complete(self, session):
        '''Обновляем выполнение'''

        if self.status != 'В архиве' or self.status != 'Пауза' or self.status == 'Стоп':
            if self.count >= self.limit:
                self.status = 'Выполнено'
                session.add(self)
                session.commit()


class City(Base):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    count: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)
    limit: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)
    remainder: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)

    status: Mapped[bool] = mapped_column(default=False, nullable=False)

    orders: Mapped[list['Orders']] = relationship(
        'Orders',
        secondary=orders_cities,
        back_populates='cities'
    )

    areas: Mapped[list['Area']] = relationship(
        'Area',
        secondary=cities_areas,
        back_populates='cities'
    )

    def update_count(self, session):

        self.count = sum(int(area.count) for area in self.areas)

        session.add(self)
        session.commit()

    def update_limit(self, session):

        self.limit = sum(int(area.limit) for area in self.areas)

        session.add(self)
        session.commit()

    def update_status(self, session):
        if self.count >= self.limit:
            self.status = True
            session.add(self)
            session.commit()

    def update_remainder(self, session):
        self.remainder = int(self.limit) - int(self.count)
        session.add(self)
        session.commit()


class Area(Base):
    __tablename__ = 'areas'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, default='Весь город')

    count: Mapped[int] = mapped_column(default=0)
    limit: Mapped[int] = mapped_column(default=0)
    remainder: Mapped[int] = mapped_column(default=0)

    cities: Mapped[list['City']] = relationship(
        'City',
        secondary=cities_areas,
        back_populates='areas'
    )

    def update_remainder(self, session):
        self.remainder = int(self.limit) - int(self.count)
        session.add(self)
        session.commit()


def create_db():
    Base.metadata.create_all(engine)