from pydantic import BaseModel


class CarAddModel(BaseModel):
    model: str
    color: str
    create_year: int
    need_parking_place: int
