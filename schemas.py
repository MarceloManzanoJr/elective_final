from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
from datetime import datetime
from dotenv import load_dotenv
from functools import wraps
from marshmallow import Schema, fields, ValidationError
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
import os

load_dotenv()

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/health_center'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_secret_key')  # Replace with a strong secret key
app.config['DEBUG'] = True
app.config['JWT_ERROR_MESSAGE_KEY'] = "msg"

db = SQLAlchemy(app)
jwt = JWTManager(app)

class Patient(db.Model):
    __tablename__ = 'patients'
    patient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45), nullable=False)
    middle_name = db.Column(db.String(45), nullable=True)
    last_name = db.Column(db.String(45), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        if isinstance(self.date_of_birth, str):
         self.date_of_birth = datetime.strptime(self.date_of_birth, "%Y-%m-%d")

        return {
            "patient_id": self.patient_id,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "date_of_birth": self.date_of_birth.strftime("%Y-%m-%d"),
            "address": self.address,
        }
class PatientSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    gender = fields.Str(required=True, validate=lambda x: x in ['Male', 'Female'])
    date_of_birth = fields.Date(required=True)
    address = fields.Str()

patient_schema = PatientSchema()

def role_required(required_role):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            if claims.get('role') != required_role:
                return jsonify({"error": "Access forbidden"}), HTTPStatus.FORBIDDEN
            return fn(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == 'Marcelo' and password == 'manzano':
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": "admin"}
        )
        return jsonify(access_token=access_token), HTTPStatus.OK

    return jsonify({"error": "Invalid credentials"}), HTTPStatus.UNAUTHORIZED



@app.route("/api/patients", methods=["GET"])
def get_patients():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    patients = Patient.query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "success": True,
        "data": [patient.to_dict() for patient in patients.items],
        "total": patients.total,
        "page": patients.page,
        "pages": patients.pages
    }), HTTPStatus.OK

@app.route("/api/patients/<int:patient_id>", methods=["GET"])
def get_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify(
            {
                "success": False, 
                "error": "Patient not found"
            }
        ), HTTPStatus.NOT_FOUND
    
    return jsonify(
        {
            "success": True, 
            "data": patient.to_dict()
        }
    ), HTTPStatus.OK

@app.route("/api/patients", methods=["POST"])
def create_patient():
    try:
        data = request.get_json()
    except Exception:
        return jsonify({
            "success": False,
            "error": "Invalid JSON format."
        }), HTTPStatus.BAD_REQUEST
    
    required_fields = ["first_name", "last_name", "gender", "date_of_birth"]
    for field in required_fields:
        if field not in data:
            return jsonify(
                {
                    "success": False,
                    "error": f"Missing required field: {field}",
                }
            ), HTTPStatus.BAD_REQUEST

    if data['gender'] not in ['Male', 'Female']:
        return jsonify({
            "success": False,
            "error": "Invalid value for 'gender'. Allowed values are 'Male' or 'Female'."
        }), HTTPStatus.BAD_REQUEST

    try:
        date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({
            "success": False,
            "error": "Invalid date format for 'date_of_birth'. Expected 'YYYY-MM-DD'."
        }), HTTPStatus.BAD_REQUEST

    new_patient = Patient(
        first_name=data['first_name'],
        middle_name=data.get('middle_name', None),
        last_name=data['last_name'],
        gender=data['gender'], 
        date_of_birth=date_of_birth,
        address=data.get('address', None)
    )

    db.session.add(new_patient)
    db.session.commit()

    return jsonify(
        {
            "success": True,
            "data": new_patient.to_dict(),
        }
    ), HTTPStatus.CREATED

@app.route("/api/patients/<int:patient_id>", methods=["PUT"])
def update_patient(patient_id):
    patient = Patient.query.get(patient_id)

    if patient is None: 
        return jsonify(
            {
                "success": False,
                "error":"Patient not found"
            }
        ), HTTPStatus.NOT_FOUND
    
    try:
        data = request.get_json()
    except Exception:
        return jsonify({
            "success": False,
            "error": "Invalid JSON format."
        }), HTTPStatus.BAD_REQUEST

    update_fields = ["first_name", "middle_name", "last_name", "gender", "date_of_birth", "address"]
    for key in update_fields:
        if key in data:
            if key == 'date_of_birth':
                try:
                    setattr(patient, key, datetime.strptime(data[key], '%Y-%m-%d').date())
                except ValueError:
                    return jsonify({
                        "success": False,
                        "error": "Invalid date format for 'date_of_birth'. Expected 'YYYY-MM-DD'."
                    }), HTTPStatus.BAD_REQUEST
            else:
                setattr(patient, key, data[key])
    
    db.session.commit()

    return jsonify(
        {
            "success": True,
            "data": patient.to_dict()
        }
    ), HTTPStatus.OK

@app.route("/api/patients/<int:patient_id>", methods=["DELETE"])
def delete_patient(patient_id):
    patient = Patient.query.get(patient_id)

    if patient is None: 
        return jsonify(
            {
                "success": False, 
                "error": "Patient not found."
            }
        ), HTTPStatus.NOT_FOUND
    
    db.session.delete(patient)
    db.session.commit()

    return jsonify(
        {
            "success": True,
            "data": "Patient deleted successfully."
        }
    ), HTTPStatus.OK

@app.errorhandler(404)
def not_found(error):
    return jsonify(
        {
            "success": False,
            "error": "Resource not found"
        }
    ), HTTPStatus.NOT_FOUND

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify(
        {
            "success": False,
            "error": "Internal Server Error"
        }
    ), HTTPStatus.INTERNAL_SERVER_ERROR

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)