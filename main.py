from fastapi import FastAPI

from car.car_api import car_router
from parking.parking_api import parking_router

from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(car_router)
app.include_router(parking_router)