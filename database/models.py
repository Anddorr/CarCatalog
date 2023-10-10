from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class ParkingPlace(Base):
    __tablename__ = 'parking_places'
    parking_id = Column(Integer, autoincrement=True, primary_key=True)
    total_parking_place = Column(Integer)
    used_parking_place_int = Column(Integer, default=0)


class Car(Base):
    __tablename__ = 'cars'
    car_id = Column(Integer, autoincrement=True, primary_key=True)
    model = Column(String)
    color = Column(String)
    create_year = Column(Integer)
    need_parking_place = Column(Integer)
    in_parking = Column(Integer, ForeignKey('parking_places.parking_id'), default=None)