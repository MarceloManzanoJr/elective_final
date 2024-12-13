from flask import Blueprint
from .patients import patients_bp
from .staff import staff_bp
from .appointments import appointments_bp
from .medications import medications_bp
from .patients_medications import patients_medications_bp

# List of blueprints to be registered in app.py
blueprints = [
    patients_bp,
    staff_bp,
    appointments_bp,
    medications_bp,
    patients_medications_bp,
]
