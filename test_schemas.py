import pytest
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import date, datetime


app = Flask(__name__)
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


@pytest.fixture(scope='function')
def test_client():

    with app.app_context():
        db.create_all()

   
        client = app.test_client()


        patient = Patient(
            id=1,
            first_name="John",
            middle_name="Michael",
            last_name="Doe",
            date_of_birth=date(1985, 6, 15),
            gender="Male",
            address="999 Pine Street"
        )
        db.session.add(patient)
        db.session.commit()
        yield client
        db.session.remove()
        db.drop_all()


@app.route('/api/patients', methods=['GET'])
def get_all_patients():
    patients = Patient.query.all()
    patients_data = [serialize_patient(p) for p in patients]
    return json.dumps({'data': patients_data})


@app.route('/api/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    new_patient = Patient(
        first_name=data['first_name'],
        middle_name=data['middle_name'],
        last_name=data['last_name'],
        date_of_birth=data['date_of_birth'],
        gender=data['gender'],
        address=data['address']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify(serialize_patient(new_patient)), 201


@app.route('/api/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    patient = Patient.query.get(id)
    if not patient:
        return jsonify({'message': 'Patient not found'}), 404

    data = request.get_json()
    patient.first_name = data['first_name']
    patient.middle_name = data['middle_name']
    patient.last_name = data['last_name']
    patient.date_of_birth = data['date_of_birth']
    patient.gender = data['gender']
    patient.address = data['address']

    db.session.commit()
    return jsonify(serialize_patient(patient))


@app.route('/api/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    patient = Patient.query.get(id)
    if not patient:
        return jsonify({'message': 'Patient not found'}), 404

    db.session.delete(patient)
    db.session.commit()
    return jsonify({'message': 'Patient deleted'}), 200


def test_get_all_patients(test_client):
    """Test the GET /api/patients endpoint."""
    response = test_client.get('/api/patients')
    assert response.status_code == 200

    data = json.loads(response.data)
    assert 'data' in data
    assert isinstance(data['data'], list)

    assert len(data['data']) == 1
    patient = data['data'][0]
    assert patient['id'] == 1
    assert patient['first_name'] == "John"
    assert patient['last_name'] == "Doe"
    assert patient['date_of_birth'] == "1985-06-15"

def test_delete_patient(test_client):
    """Test the DELETE /api/patients endpoint."""
    response = test_client.delete('/api/patients/1')
    assert response.status_code == 200

    response = test_client.get('/api/patients')
    data = json.loads(response.data)
    assert len(data['data']) == 0 


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

def test_get_patients_edge_cases(test_client):
    patient = Patient(
        id=4,
        first_name="",
        middle_name=None,
        last_name="Doe",
        date_of_birth=None,
        gender="Other",
        address=""
    )
    db.session.add(patient)
    db.session.commit()

    response = test_client.get('/api/patients')
    data = json.loads(response.data)
    
if __name__ == '__main__':
    pytest.main([__file__])
