from pydantic import BaseModel


class AddRemoveCar(BaseModel):
    car_id: int
    parking_id: int
