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

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))
    address = db.Column(db.String(255))
def serialize_patient(patient):
    return {
        'id': patient.id,
        'first_name': patient.first_name,
        'middle_name': patient.middle_name,
        'last_name': patient.last_name,
        'date_of_birth': str(patient.date_of_birth),
        'gender': patient.gender,
        'address': patient.address,
    }

@app.route('/api/patients', methods=['GET'])
def test_get_all_patients():
    patients = Patient.query.all()
    patients_data = [serialize_patient(p) for p in patients]
    return jsonify({'data': patients_data})

@pytest.fixture(scope='module')
def test_client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Add sample data
            patient = Patient(
                id=1,
                first_name="John",
                middle_name="Michael",
                last_name="Doe",
                date_of_birth="1985-06-15",
                gender="Male",
                address="999 Pine Street"
            )
            db.session.add(patient)
            db.session.commit()
            yield client
            db.session.remove()
            db.drop_all()

# Test cases
def test_get_patients(test_client):
    """Test the GET /api/patients endpoint."""
    response = test_client.get('/api/patients')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    assert isinstance(data['data'], list)
    if data['data']:
        assert data['data'][0]['id'] == 1
        assert data['data'][0]['first_name'] == "John"

def test_get_patients_empty_db(test_client):
    """Test the GET /api/patients endpoint with an empty database."""
    db.session.query(Patient).delete()
    db.session.commit()

    response = test_client.get('/api/patients')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert 'data' in data
    assert isinstance(data['data'], list)
    assert len(data['data']) == 0

def test_get_patients_with_multiple_entries(test_client):
    """Test the GET /api/patients endpoint with multiple patients."""
    patients = [
        Patient(
            id=2,
            first_name="Alice",
            middle_name="J.",
            last_name="Smith",
            date_of_birth="1990-05-20",
            gender="Female",
            address="123 Oak Street"
        ),
        Patient(
            id=3,
            first_name="Bob",
            middle_name="A.",
            last_name="Jones",
            date_of_birth="1975-09-15",
            gender="Male",
            address="456 Maple Avenue"
        ),
    ]
    db.session.add_all(patients)
    db.session.commit()

    response = test_client.get('/api/patients')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert len(data['data']) == 3
    assert any(p['first_name'] == "Alice" for p in data['data'])