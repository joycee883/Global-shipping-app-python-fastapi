# Global Shipping App

## Project Description
The **Global Shipping App** is a comprehensive solution for a shipping company, Big Bag, that allows customers to book and ship parcels globally. The app integrates modern technologies like **Streamlit** for the frontend, **FastAPI** for the backend, and **MySQL** for the database to provide a seamless and efficient user experience. It calculates shipping charges based on parcel size, weight, and destination country, and ensures compliance with country-specific shipping rules.

---

## Features

- **User Registration**: Customers can create an account to use the platform.
- **Shipping Charge Calculation**: Dynamic calculation of shipping charges based on parcel details.
- **Order Placement**: Customers can place an order after accepting the calculated charges.
- **Compliance with Rules**: Each country's specific shipping rules (max size, weight, banned items, etc.) are enforced.
- **API Documentation**: Auto-generated API documentation using FastAPI's Swagger UI.

---

## Tech Stack

1. **Frontend**: [Streamlit](https://streamlit.io/)
2. **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
3. **Database**: [MySQL](https://www.mysql.com/)

---

## Project Structure

```
├── main.py                 # FastAPI backend logic
├── frontend/               # Streamlit frontend files
├── database/               # SQL scripts and database initialization
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Installation and Setup

### Prerequisites

- Python 3.8+
- MySQL Server

### Steps to Run the Application

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/global-shipping-app.git
   cd global-shipping-app
   ```

2. **Set Up the Database**
   - Create a MySQL database and name it `shipping_db`.
   - Run the SQL scripts in the `database/` folder to initialize tables (`users`, `orders`, etc.).

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Backend**
   ```bash
   uvicorn main:app --reload
   ```
   - Visit the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

5. **Run the Frontend**
   ```bash
   streamlit run frontend/app.py
   ```
   - Access the frontend at [http://localhost:8501](http://localhost:8501).

---

## API Endpoints

| Method | Endpoint       | Description               |
|--------|----------------|---------------------------|
| POST   | `/register`    | Register a new user.      |
| POST   | `/place_order` | Place a shipping order.   |

---

## Example Workflow

1. A customer registers on the site.
2. They input parcel details (size, weight, destination).
3. The app calculates shipping charges based on the inputs and country-specific rules.
4. The customer confirms the order.
5. The order is stored in the database and can be tracked.

---

## Key Design Decisions

1. **Streamlit for Frontend**: Chosen for its simplicity and ability to quickly build interactive web apps.
2. **FastAPI for Backend**: Selected for its high performance and automatic API documentation.
3. **MySQL for Database**: Used for structured data storage and easy integration.

---

## Future Enhancements

- Add user authentication.
- Implement support for banned item checks.
- Integrate payment gateway for order confirmation.
- Add tracking functionality for orders.
- Include country-specific custom duty calculations.

