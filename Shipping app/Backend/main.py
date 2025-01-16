from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import mysql.connector

# FastAPI app instance
app = FastAPI()

# MySQL Database connection setup
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="883",  # Use your MySQL password
        database="shipping_db"
    )
    return connection

# Pydantic models for validation
class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    country: str

class OrderCreate(BaseModel):
    parcel_size: float
    parcel_weight: float
    destination_country: str

# API Endpoints

@app.post("/users/")
def create_user(user: UserCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE username = %s", (user.username,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    cursor.execute("INSERT INTO users (username, password, email, country) VALUES (%s, %s, %s, %s)", 
                   (user.username, user.password, user.email, user.country))
    conn.commit()
    conn.close()
    return {"message": "User created successfully!"}

@app.post("/orders/")
def create_order(order: OrderCreate):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch country details
    cursor.execute("SELECT * FROM countries WHERE country_name = %s", (order.destination_country,))
    country = cursor.fetchone()
    
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")

    # Check if parcel size and weight exceed country limits
    if order.parcel_size > country[1] or order.parcel_weight > country[2]:  # assuming max_size and max_weight are at indexes 1 and 2
        raise HTTPException(status_code=400, detail="Parcel exceeds country limit")
    
    # Calculate shipping charge (simple model)
    shipping_charge = (order.parcel_weight * 10) + (order.parcel_size * 5) + country[3]  # Assuming custom_duty_tax is at index 3
    
    # Insert the order into the orders table
    cursor.execute("INSERT INTO orders (user_id, parcel_size, parcel_weight, destination_country_id, shipping_charge, order_status) "
                   "SELECT user_id, %s, %s, country_id, %s, 'pending' FROM users, countries WHERE username = %s AND country_name = %s", 
                   (order.parcel_size, order.parcel_weight, shipping_charge, "default_user", order.destination_country))
    conn.commit()
    conn.close()

    return {"message": "Order placed successfully!", "shipping_charge": shipping_charge}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
