from database import get_db
from database.models import ParkingPlace

from database.car_servise import get_car_info_db


global db
db = next(get_db())


# Add new parking place
def add_parking_place_db(total_parking_place: int) -> bool:
    new_parking_place = ParkingPlace(total_parking_place=total_parking_place)
    db.add(new_parking_place)
    db.commit()
    return True


# Get info about parking place
def get_parking_info_db(parking_id: int):
    exact_parking = db.query(ParkingPlace).filter_by(parking_id=parking_id).first()
    if exact_parking:
        return exact_parking
    return False


# Add car to parking
def add_car_to_parking_db(car_id: int, parking_id: int) -> bool:
    exact_parking = get_parking_info_db(parking_id)
    exact_car = get_car_info_db(car_id)
    if exact_car.in_parking is None:
        if (exact_parking.total_parking_place - exact_parking.used_parking_place_int) >= exact_car.need_parking_place:
            exact_parking.used_parking_place_int += exact_car.need_parking_place
            exact_car.in_parking = exact_parking.parking_id
            return True
        print(1)
        return False
    print(2)
    return False


# Remove car from parking
def remove_car_from_parking_db(car_id: int, parking_id: int) -> bool:
    exact_parking = get_parking_info_db(parking_id)
    exact_car = get_car_info_db(car_id)
    if exact_car.in_parking not in None:
        exact_parking.used_parking_place_int -= exact_car.need_parking_place
        exact_car.in_parking = None
        return True
    return False

