import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def connect_sql_server():
    server = os.getenv("server")
    database = os.getenv("database")
    driver = os.getenv("driver")
    Trusted_Connection = os.getenv("Trusted_Connection", "yes")
    connection_string = f"mssql+pyodbc://{server}/{database}?driver={driver.replace(' ', '+')}&Trusted_Connection={Trusted_Connection}"
    engine = create_engine(connection_string)
    
    return engine.connect()