from flask import Flask, jsonify
import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from extensions import db
from models import User


load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print(app.config['SQLALCHEMY_DATABASE_URI'])

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/api/login', methods=['GET'])
def index():
    print("Hello world")
    return jsonify(ok=True,message="Hello World") 


if __name__ == '__main__':
    app.run(debug=True,port=5000)