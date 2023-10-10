from database import get_db
from database.models import Car


global db
db = next(get_db())


# Add new car
def add_new_car_db(model: str, color: str, create_year: int, need_parking_place: int):
    new_car = Car(model=model, color=color, create_year=create_year,
                  need_parking_place=need_parking_place)
    db.add(new_car)
    db.commit()
    return True


# Delete car
def delete_car_db(car_id: int):
    exact_car = db.query(Car).filter_by(car_id=car_id).first()
    if exact_car:
        db.delete(exact_car)
        return True
    return False


# Get info about car
def get_car_info_db(car_id: int):
    exact_car = db.query(Car).filter_by(car_id=car_id).first()
    if exact_car:
        return exact_car
    return False
