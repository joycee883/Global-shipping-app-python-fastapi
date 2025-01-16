import streamlit as st
import requests

st.title("Shipping App")

# User Registration
st.header("Register")
name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
if st.button("Register"):
    response = requests.post("http://127.0.0.1:8000/register", json={"name": name, "email": email, "password": password})
    st.write(response.json())

# Place an Order
st.header("Place Order")
user_id = st.number_input("User ID", min_value=1)
parcel_size = st.number_input("Parcel Size (in cubic meters)", min_value=0.0)
parcel_weight = st.number_input("Parcel Weight (in kg)", min_value=0.0)
destination_country = st.text_input("Destination Country")
if st.button("Place Order"):
    response = requests.post("http://127.0.0.1:8000/place_order", json={
        "user_id": user_id,
        "parcel_size": parcel_size,
        "parcel_weight": parcel_weight,
        "destination_country": destination_country
    })
    st.write(response.json())
