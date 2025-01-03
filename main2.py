# main.py
from fastapi import FastAPI
from psycopg2 import connect, OperationalError

app = FastAPI()

def get_db_connection():
    try:
        # Connect to PostgreSQL
        conn = connect(
            host="localhost",
            port="5432",
            database="postgres",  # Replace with your DB name
            user="postgres",      # Replace with your DB user
            password="postgres"  # Replace with your DB password
        )
        return conn
    except OperationalError as e:
        print("Unable to connect to the database:", e)
        return None

@app.get("/db-status")
async def check_db_status():
    conn = get_db_connection()
    if conn is None:
        return {"status": "failure", "message": "Unable to connect to PostgreSQL database"}
    
    # If connection is successful, close and return success
    conn.close()
    return {"status": "success", "message": "Connected to PostgreSQL database successfully"}
