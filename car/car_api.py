from fastapi import APIRouter

from database.car_servise import add_new_car_db, delete_car_db, get_car_info_db
from car import CarAddModel


car_router = APIRouter(prefix='/car', tags=['car'])


@car_router.post('/add-car')
async def add_new_car(data: CarAddModel):
    new_car_data = data.model_dump()
    result = add_new_car_db(**new_car_data)
    return {'status': 1, 'message': result}


@car_router.get('/get-car-info')
async def get_car_info(car_id: int):
    result = get_car_info_db(car_id)
    return {'status': 1 if result else 0, 'message': result}


@car_router.delete('/delete-car')
async def delete_car(car_id: int):
    result = delete_car_db(car_id)
    return {'status': 1 if result else 0, 'message': result}



