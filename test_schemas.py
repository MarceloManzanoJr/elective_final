from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from unittest.mock import patch
import pytest

# Initialize the Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/health_center'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TESTING'] = True

db = SQLAlchemy(app)