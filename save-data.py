import os
import psycopg2
import json
from dotenv import load_dotenv
from datetime import datetime, date
from decimal import Decimal

load_dotenv()

def db_connect():
  conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
  )
  return conn


def load_data_db(query: str):
  conn = db_connect()
  print("[DB CONNECTION] (open)")
  with conn.cursor() as cursor:
    cursor.execute(query)
    data = cursor.fetchall()
    rows = [desc[0] for desc in cursor.description]
  print(f"QUERY EXECUTED: {query}")
  data_dict = [dict(zip(rows, row)) for row in data]
  conn.close()
  print("[DB CONNECTION] (close) \n")
  return data_dict


def custom_serializer(obj):
  if isinstance(obj, (datetime, date)):
    return obj.isoformat()
  if isinstance(obj, Decimal):
    return float(obj)
  raise TypeError(f"Type {type(obj)} is not serializable")

def save_as_json(data, file_path):
  os.makedirs('./data', exist_ok=True)
  full_path = os.path.join('./data', file_path)
  with open(full_path, 'w') as file:
    json.dump(data, file, indent=4, default=custom_serializer)

if __name__ == "__main__":
  data_for_seller = load_data_db("SELECT * FROM gold_sales_for_seller")
  save_as_json(data_for_seller, "data_for_seller.json")
  print("Data saved successfully on data_for_seller.json \n \n")
  
  data_seven_days = load_data_db("SELECT * FROM gold_sales_seven_days")
  save_as_json(data_seven_days, "data_seven_days.json")
  print("Data saved successfully on data_seven_days.json \n")
