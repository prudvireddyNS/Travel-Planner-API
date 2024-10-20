from config import *
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from genai.accommodation import get_accommodation
from genai.transportation import get_transportation
from genai.activities import get_activities
from genai.travel_plan import get_travel_plan


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or you can specify the frontend URL like ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

from pydantic import BaseModel

class AccommodationInput(BaseModel):
    location: str
    budget: str
    duration: str

class TransportationInput(BaseModel):
    from_location: str
    to_location: str
    budget: str

class ActivitiesInput(BaseModel):
    location: str
    duration: str

@app.get('/')
def available_apis():
    return {"accommodation": "https://travel-planner-api-b6l8.onrender.com/adventuro/accommodation",
            "transportation": "https://travel-planner-api-b6l8.onrender.com/adventuro/transportation",
            "activities": "https://travel-planner-api-b6l8.onrender.com/adventuro/activities",
            "travel plan": "https://travel-planner-api-b6l8.onrender.com/adventuro/travel-plan"
            }

@app.post('/adventuro/accommodation')
async def accommodation(input: AccommodationInput):
    try:
        print("ACC")
        details = await get_accommodation(location=input.location, budget=input.budget, duration=input.duration)
        return details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/adventuro/transportation')
async def transportation(input: TransportationInput):
    try:
        print("TRANS")
        details = await get_transportation(from_location=input.from_location, to_location=input.to_location, budget=input.budget)
        return details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/adventuro/activities')
async def activities(input: ActivitiesInput):
    try:
        print("ACT")
        details = await get_activities(location=input.location, duration=input.duration)
        return details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/adventuro/travel-plan')
async def travel_plan(input: TravelPlanInput):
    try:
        details = await get_travel_plan(from_location= input.from_location, 
                                  to_location= input.to_location, 
                                  budget= input.budget, 
                                  duration= input.duration, 
                                  accommodation= input.accommodation, 
                                  transportation= input.transportation, 
                                  activities= input.activities)
        return details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  
    uvicorn.run(app, host="0.0.0.0", port=port)
