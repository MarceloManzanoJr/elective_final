from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/health_care'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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
        return {
            "patient_id": self.patient_id,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "date_of_birth": self.date_of_birth.strftime("%Y-%m-%d"),
            "address": self.address,
        }
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