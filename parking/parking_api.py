from fastapi import APIRouter

from database.parking_servise import (add_parking_place_db, get_parking_info_db, add_car_to_parking_db,
                                      remove_car_from_parking_db)
from parking import AddRemoveCar


parking_router = APIRouter(prefix='/parking', tags=['parking'])


@parking_router.post('/add-parking-place')
async def add_parking_place(total_parking_place: int):
    result = add_parking_place_db(total_parking_place)
    return {'status': 1, 'message': result}


@parking_router.get('/get-info-parking')
async def get_parking_info(parking_id: int):
    result = get_parking_info_db(parking_id)
    return {'status': 1 if result else 0, 'message': result}


@parking_router.post('/add-car-to-parking')
async def add_car_to_parking(data: AddRemoveCar):
    car_and_parking_data = data.model_dump()
    result = add_car_to_parking_db(**car_and_parking_data)
    return {'status': 1 if result else 0, 'message': result}


@parking_router.delete('/remove-car-from-parking')
async def remove_car_to_parking(data: AddRemoveCar):
    car_and_parking_data = data.model_dump()
    result = remove_car_from_parking_db(**car_and_parking_data)
    return {'status': 1 if result else 0, 'message': result}




