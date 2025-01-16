import requests
import streamlit as st

# Backend URL (Update this with your hosted FastAPI backend URL or local backend URL)
BACKEND_URL = "https://fastapi-backend-url.com"  # Replace with your backend URL

# Function to register a new user
def register_user(name, email, password):
    url = f"{BACKEND_URL}/register"
    payload = {
        "name": name,
        "email": email,
        "password": password
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for HTTP codes >= 400
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"success": False, "message": str(e)}

# Function to place an order
def place_order(user_id, parcel_weight, parcel_size, destination):
    url = f"{BACKEND_URL}/place_order"
    payload = {
        "user_id": user_id,
        "parcel_weight": parcel_weight,
        "parcel_size": parcel_size,
        "destination": destination
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"success": False, "message": str(e)}

# Streamlit UI
st.title("Shipping App")

# Tabs for User Registration and Place Order
tab1, tab2 = st.tabs(["User Registration", "Place Order"])

# Tab 1: User Registration
with tab1:
    st.header("Register a New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Register"):
        if name and email and password:
            result = register_user(name, email, password)
            if result.get("success"):
                st.success("User registered successfully!")
            else:
                st.error(f"Registration failed: {result.get('message')}")
        else:
            st.warning("Please fill in all fields.")

# Tab 2: Place Order
with tab2:
    st.header("Place an Order")
    user_id = st.text_input("User ID")
    parcel_weight = st.number_input("Parcel Weight (kg)", min_value=0.1, step=0.1)
    parcel_size = st.text_input("Parcel Size (e.g., Small, Medium, Large)")
    destination = st.text_input("Destination Country")
    
    if st.button("Place Order"):
        if user_id and parcel_weight > 0 and parcel_size and destination:
            result = place_order(user_id, parcel_weight, parcel_size, destination)
            if result.get("success"):
                st.success(f"Order placed successfully! Order ID: {result.get('order_id')}")
            else:
                st.error(f"Order failed: {result.get('message')}")
        else:
            st.warning("Please fill in all fields.")

# Footer
st.markdown("---")
st.markdown("**Shipping App** | Powered by Streamlit and FastAPI")
