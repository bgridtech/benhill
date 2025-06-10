from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor
import os

username = os.getenv('username_supabase_ben')
password = os.getenv('password_supabase_ben')

app = Flask(__name__)
CORS(app)

# Database connection settings
DB_CONFIG = {
    "user": f"{username}",
    "password": f"{password}",
    "host": "aws-0-ap-southeast-1.pooler.supabase.com",
    "port": "5432",
    "dbname": "postgres"
}

def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.OperationalError as e:
        print(f"Database connection error: {e}")
        return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

