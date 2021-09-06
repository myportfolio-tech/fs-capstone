from flask import Blueprint, abort, jsonify, request
from staffer.models import Employee
from staffer.utils.utils import json_employees_results, json_employee
from staffer.utils.auth import requires_auth

employees = Blueprint('employee', __name__)


@employees.route('/employees', methods=['GET'])
def get_all_employees():
    
    all_employees = Employee.query.all()

    return json_employees_results(all_employees)


@employees.route("/employee/<int:emp_id>", methods=['GET'])
@requires_auth('get:employee')
def get_employee(payload, emp_id):
    
    emp = Employee.query.get_or_404(emp_id)
    if emp is None:
        abort(404)

    return json_employee(emp)


@employees.route("/employee/create", methods=['POST'])
@requires_auth('post:employee')
def create_employee(payload):
    
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    department = data.get('department')

    employee = Employee(username=username, email=email, department=department)
    employee.insert()

    emp = Employee.query.filter_by(email=email).first()

    return json_employee(emp)


@employees.route("/employee/<int:emp_id>/delete", methods=['DELETE'])
@requires_auth('delete:employee')
def delete_employee(payload, emp_id):

    emp = Employee.query.get_or_404(emp_id)
    if emp is None:
        abort(404)
    
    emp.delete()

    return jsonify({
        'success': True,
        'emp_id': emp_id
    })