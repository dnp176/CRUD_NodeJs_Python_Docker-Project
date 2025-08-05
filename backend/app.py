import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv

# Load ENV variables
load_dotenv()

BACKEND_PORT = int(os.getenv("BACKEND_PORT", 8000))
#DB_HOST = os.getenv("DB_HOST", "localhost")
#DB_PORT = int(os.getenv("DB_PORT", 27017))
#DB_NAME = os.getenv("DB_NAME", "crudapp")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

mongo_url = f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?authSource=admin"

# MongoDB Connection
#mongo_url = f"mongodb://{DB_HOST}:{DB_PORT}/"
mongo_url = f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?authSource=admin"

try:
    client = MongoClient(mongo_url)
    db = client[DB_NAME]
    users_collection = db["users"]
    print(f"✅ Connected to MongoDB at {mongo_url}, using DB: {DB_NAME}")
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")

# FastAPI App
app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Model
class User(BaseModel):
    first_name: str
    last_name: str
    email: str

# Helper: Convert ObjectId to str
def serialize_user(user):
    return {
        "_id": str(user["_id"]),
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"]
    }

# Routes
@app.get("/users")
def get_users():
    users = list(users_collection.find())
    return [serialize_user(user) for user in users]

@app.post("/users")
def create_user(user: User):
    user_data = user.dict()
    result = users_collection.insert_one(user_data)
    return {"message": "User created successfully", "id": str(result.inserted_id)}

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    try:
        obj_id = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")
    result = users_collection.delete_one({"_id": obj_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
