from flask import Blueprint, request, jsonify
from models import db, Patient
from schemas import PatientSchema

patients_bp = Blueprint('patients', __name__)
patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)

@patients_bp.route('/patients', methods=['GET'])
def get_all_patients():
    patients = Patient.query.all()
    return jsonify(patients_schema.dump(patients))

@patients_bp.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    patient = Patient.query.get_or_404(id)
    return jsonify(patient_schema.dump(patient))

@patients_bp.route('/patients', methods=['POST'])
def create_patient():
    data = request.json
    try:
        patient = patient_schema.load(data)
        new_patient = Patient(**patient)
        db.session.add(new_patient)
        db.session.commit()
        return jsonify(patient_schema.dump(new_patient)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@patients_bp.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    data = request.json
    patient = Patient.query.get_or_404(id)
    try:
        for key, value in data.items():
            setattr(patient, key, value)
        db.session.commit()
        return jsonify(patient_schema.dump(patient))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@patients_bp.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return '', 204
