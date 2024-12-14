from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'Patients'
    patient_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    middle_name = db.Column(db.String(45), nullable=True)
    last_name = db.Column(db.String(45), nullable=False)
    date_of_birth = db.Column(db.String(45), nullable=True)
    gender = db.Column(db.String(45), nullable=True)
    address = db.Column(db.String(45), nullable=True)

class Staff(db.Model):
    __tablename__ = 'Staff'
    staff_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    middle_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45), nullable=False)
    data_of_birth = db.Column(db.String(45), nullable=False)
    gender = db.Column(db.String(45))
    qualifications = db.Column(db.String(45), nullable=False)

class Appointment(db.Model):
    __tablename__ = 'Appointments'
    appointment_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('Patients.patient_id'), nullable=False)
    Staff_staff_id = db.Column(db.Integer, db.ForeignKey('Staff.staff_id'), nullable=False)
    date_time_of_appointment = db.Column(db.DateTime, nullable=False)

class MedicationType(db.Model):
    __tablename__ = 'medication_types'
    medication_type_code = db.Column(db.Integer, primary_key=True)
    medication_type_name = db.Column(db.String(225), nullable=False)
    medication_type_description = db.Column(db.String(225), nullable=False)

class Medication(db.Model):
    __tablename__ = 'Medication'
    medication_id = db.Column(db.Integer, primary_key=True)
    medication_type_code = db.Column(db.Integer, db.ForeignKey('medication_types.medication_type_code'), nullable=False)
    medication_unit_cost = db.Column(db.Integer)
    medication_name = db.Column(db.String(255), nullable=False)
    medication_description = db.Column(db.String(255), nullable=False)

class PatientMedication(db.Model):
    __tablename__ = 'Patients_Medecation'
    patients_medication_id = db.Column(db.Integer, primary_key=True)
    Medication_medication_id = db.Column(db.Integer, db.ForeignKey('Medication.medication_id'), nullable=False)
    Patients_patient_id = db.Column(db.Integer, db.ForeignKey('Patients.patient_id'), nullable=False)
    date_time_administered = db.Column(db.String(225), nullable=False)
    dosage = db.Column(db.String(225), nullable=False)
    comments = db.Column(db.String(225))
