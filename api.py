from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

EXCEL_FILE = "flights.xlsx"

app = FastAPI(title="Airline Ops Manager API")
class Flight(BaseModel):
    FlightNo: str
    Origin: str
    Destination: str
    Date: str

def load_flight():
    try:
        return pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["FlightNo", "Origin", "Destination", "Date"])
    

def save_flights(df):
    df.to_excel(EXCEL_FILE,index=False)

@app.get("/flights")
def get_flights():
    df = load_flight()
    return df.to_dict(orient = "records")

@app.post("/flights")
def add_flight(flight: Flight):
    df = load_flight()
    new_row = pd.DataFrame([flight.model_dump()])
    df = pd.concat([df,new_row], ignore_index=True)
    save_flights(df)

    return flight