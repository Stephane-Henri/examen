from fastapi import FastAPI, HTTPException, Depends, status, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pymongo import MongoClient
import secrets

app = FastAPI()
security = HTTPBasic()

client = MongoClient("mongodb://localhost:27017/")
db = client["examen"]

def verify_credentials(credentials: HTTPBasicCredentials):
    users_col = db["users"]
    user_doc = users_col.find_one({"login": credentials.username})
    if user_doc:
        correct_username = user_doc["login"]
        correct_password = user_doc["password"]
        is_valid = secrets.compare_digest(credentials.username, correct_username) \
            and secrets.compare_digest(credentials.password, correct_password)

        if not is_valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )


@app.get("/plant-time/{id}")
def get_plan_time(id: int, credentials: HTTPBasicCredentials = Depends(security)):
    verify_credentials(credentials)
    users_col = db["users"]
    user = users_col.find_one({"id": id})
    if not user:
        raise HTTPException(status_code=404, details="Нет таких данных")
    return {
        "вид": user["type"],
        "время_полива": user["next_watering_date"],
    }


@app.get("/plant-type/{id}")
def get_plant_type(id: int):
    print(type)
    plants_col = db["plants"]
    plant = plants_col.find_one({"id": id})
    if not plant:
        raise HTTPException(status_code=404, detail="Растение не существует на базе")

    return {
        "вид": plant["type"],
        "частота_полива": plant["watering_frequency"]
    }