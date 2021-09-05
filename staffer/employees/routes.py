from flask import Blueprint, jsonify, abort, request
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