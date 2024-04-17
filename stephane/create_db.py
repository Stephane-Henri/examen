from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["examen"]

# Define the schema for the plants collection
plants_collection = db["plants"]
plants_collection.insert_many([
    {"id": 1, "type": "Фикус", "watering_frequency": "1 раз в неделю"},
    {"id": 2, "type": "Замиокулькас", "watering_frequency": "2 раза в неделю"},
    {"id": 3, "type": "Кактус", "watering_frequency": "1 раз в неделю"}
])

# Define the schema for the users collection
users_collection = db["users"]
users_collection.insert_many([
    {"id": 1, "login": "cactuses", "password": "111cactus111", "type": "Кактус", "next_watering_date": "2023-01-27"},
    {"id": 2, "login": "planter", "password": "wfiosdjnv", "type": "Фикус", "next_watering_date": "2023-01-30"},
    {"id": 3, "login": "maria", "password": "wfhowuhgvwou", "type": "Фикус", "next_watering_date": "2023-02-01"}
])