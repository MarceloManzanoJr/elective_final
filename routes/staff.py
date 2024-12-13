from flask import Blueprint, request, jsonify
from models import db, Staff
from schemas import StaffSchema

staff_bp = Blueprint('staff', __name__)
staff_schema = StaffSchema()
staffs_schema = StaffSchema(many=True)

@staff_bp.route('/staff', methods=['GET'])
def get_staff():
    staff = Staff.query.all()
    return jsonify(staffs_schema.dump(staff))


