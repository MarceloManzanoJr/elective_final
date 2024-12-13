from flask import Blueprint, request, jsonify
from models import db, Medication
from schemas import MedicationSchema

# Define the blueprint
medications_bp = Blueprint('medications', __name__)

# Initialize schemas
medication_schema = MedicationSchema()
medications_schema = MedicationSchema(many=True)

# GET: Fetch all medications
@medications_bp.route('/medications', methods=['GET'])
def get_medications():
    medications = Medication.query.all()
    return jsonify(medications_schema.dump(medications))

# GET: Fetch a single medication by ID
@medications_bp.route('/medications/<int:id>', methods=['GET'])
def get_medication(id):
    medication = Medication.query.get_or_404(id)
    return jsonify(medication_schema.dump(medication))

# POST: Add a new medication
@medications_bp.route('/medications', methods=['POST'])
def add_medication():
    data = request.get_json()
    try:
        new_medication = Medication(
            medication_type_code=data['medication_type_code'],
            medication_unit_cost=data.get('medication_unit_cost'),
            medication_name=data['medication_name'],
            medication_description=data['medication_description']
        )
        db.session.add(new_medication)
        db.session.commit()
        return jsonify(medication_schema.dump(new_medication)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# PUT: Update an existing medication
@medications_bp.route('/medications/<int:id>', methods=['PUT'])
def update_medication(id):
    medication = Medication.query.get_or_404(id)
    data = request.get_json()
    try:
        medication.medication_type_code = data['medication_type_code']
        medication.medication_unit_cost = data.get('medication_unit_cost')
        medication.medication_name = data['medication_name']
        medication.medication_description = data['medication_description']
        db.session.commit()
        return jsonify(medication_schema.dump(medication))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# DELETE: Delete a medication
@medications_bp.route('/medications/<int:id>', methods=['DELETE'])
def delete_medication(id):
    medication = Medication.query.get_or_404(id)
    try:
        db.session.delete(medication)
        db.session.commit()
        return jsonify({"message": "Medication deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
