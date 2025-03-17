import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_db():
    try:
        db = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
            port=3306, # Añadimos el puerto 3306
        )
        yield db
    finally:
        db.close()