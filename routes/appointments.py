from flask import Blueprint, request, jsonify
from models import db, Appointment
from schemas import AppointmentSchema

appointments_bp = Blueprint('appointments', __name__)
appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)

@appointments_bp.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify(appointments_schema.dump(appointments))

# Other CRUD operations similar to patients.py
