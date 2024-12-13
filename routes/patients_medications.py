from flask import Blueprint, request, jsonify
from models import db, PatientsMedication
from schemas import PatientsMedicationSchema

# Define the blueprint
patients_medications_bp = Blueprint('patients_medications', __name__)

# Initialize schemas
patients_medication_schema = PatientsMedicationSchema()
patients_medications_schema = PatientsMedicationSchema(many=True)

# GET: Fetch all patients-medications records
@patients_medications_bp.route('/patients_medications', methods=['GET'])
def get_patients_medications():
    patients_medications = PatientsMedication.query.all()
    return jsonify(patients_medications_schema.dump(patients_medications))

# GET: Fetch a single patient-medication record by ID
@patients_medications_bp.route('/patients_medications/<int:id>', methods=['GET'])
def get_patient_medication(id):
    patient_medication = PatientsMedication.query.get_or_404(id)
    return jsonify(patients_medication_schema.dump(patient_medication))

# POST: Add a new patient-medication record
@patients_medications_bp.route('/patients_medications', methods=['POST'])
def add_patient_medication():
    data = request.get_json()
    try:
        new_record = PatientsMedication(
            Medication_medication_id=data['Medication_medication_id'],
            Patients_patient_id=data['Patients_patient_id'],
            date_time_administered=data['date_time_administered'],
            dosage=data['dosage'],
            comments=data.get('comments')
        )
        db.session.add(new_record)
        db.session.commit()
        return jsonify(patients_medication_schema.dump(new_record)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# PUT: Update an existing patient-medication record
@patients_medications_bp.route('/patients_medications/<int:id>', methods=['PUT'])
def update_patient_medication(id):
    patient_medication = PatientsMedication.query.get_or_404(id)
    data = request.get_json()
    try:
        patient_medication.Medication_medication_id = data['Medication_medication_id']
        patient_medication.Patients_patient_id = data['Patients_patient_id']
        patient_medication.date_time_administered = data['date_time_administered']
        patient_medication.dosage = data['dosage']
        patient_medication.comments = data.get('comments')
        db.session.commit()
        return jsonify(patients_medication_schema.dump(patient_medication))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# DELETE: Delete a patient-medication record
@patients_medications_bp.route('/patients_medications/<int:id>', methods=['DELETE'])
def delete_patient_medication(id):
    patient_medication = PatientsMedication.query.get_or_404(id)
    try:
        db.session.delete(patient_medication)
        db.session.commit()
        return jsonify({"message": "Patient-medication record deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
