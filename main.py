from fastapi import FastAPI
from dotenv import load_dotenv

# DB models
# TODO ADD REAL MODELS!! NEEDED SO IT WORKS!
from app.models.example import Example

# Other routes
from app.routers.example import router as example_router

# Load .env variables in the app
load_dotenv()

app = FastAPI()

# Register the other routers
#TODO put REAL other routers
app.include_router(example_router)

@app.get("/")
def root():
	return "Welcome to the Zoo Food Service API"