from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="883",
        database="shipping_db"
    )

# User model
class User(BaseModel):
    name: str
    email: str
    password: str

# Order model
class Order(BaseModel):
    user_id: int
    parcel_size: float
    parcel_weight: float
    destination_country: str

# Register a new user
@app.post("/register")
async def register(user: User):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                       (user.name, user.email, user.password))
        conn.commit()
    except mysql.connector.Error as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "User registered successfully"}

# Place an order
@app.post("/place_order")
async def place_order(order: Order):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Calculate shipping charge (basic logic)
    shipping_charge = order.parcel_weight * 10  # Example: 10 units per kg
    try:
        cursor.execute("INSERT INTO orders (user_id, parcel_size, parcel_weight, destination_country, shipping_charge) VALUES (%s, %s, %s, %s, %s)",
                       (order.user_id, order.parcel_size, order.parcel_weight, order.destination_country, shipping_charge))
        conn.commit()
    except mysql.connector.Error as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Order placed successfully", "shipping_charge": shipping_charge}
