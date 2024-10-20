from config import *
from fastapi import FastAPI, HTTPException
from genai.accommodation import get_accommodation
from genai.transportation import get_transportation
from genai.activities import get_activities


app = FastAPI()

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

@app.post('/adventuro/accommodation')
def accommodation(input: AccommodationInput):
    try:
        details = get_accommodation(location=input.location, budget=input.budget, duration=input.duration)
        return details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/adventuro/transportation')
def transportation(input: TransportationInput):
    try:
        details = get_transportation(from_location=input.from_location, to_location=input.to_location, budget=input.budget)
        return details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/adventuro/activities')
def activities(input: ActivitiesInput):
    try:
        details = get_activities(location=input.location, duration=input.duration)
        return details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  
    uvicorn.run(app, host="0.0.0.0", port=port)