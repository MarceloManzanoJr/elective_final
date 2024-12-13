from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/health_center'
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