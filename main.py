from fastapi import FastAPI
from dotenv import load_dotenv

# DB models
# TODO ADD REAL MODELS!! NEEDED SO IT WORKS!
from app.models.storage_unit import StorageUnit
from app.models.storage_unit_type import StorageUnitType
from app.models.food_stock import FoodStock
from app.models.food_type import FoodType

# Other routes
# from app.routers.example import router as example_router

# Load .env variables in the app
load_dotenv()

app = FastAPI()

# Register the other routers
#TODO put REAL other routers
# app.include_router(example_router)

@app.get("/")
def root():
	return "Welcome to the Zoo Food Service API"