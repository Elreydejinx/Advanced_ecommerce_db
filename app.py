from flask import Flask
import psycopg2
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    conn = psycopg2.connect(app.config['DATABASE_URL'])
    return conn

@app.route('/')
def home():
    return "Welcome to the E-commerce API!"

@app.route('/api/example', methods=['GET'])
def example_endpoint():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    app.run()
