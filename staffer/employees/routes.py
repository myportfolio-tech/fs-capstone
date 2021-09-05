from flask import Blueprint, jsonify, abort
from staffer.models import Employee
from staffer.utils.utils import process_employee_results

employees = Blueprint('employee', __name__)


@employees.route('/employees', methods=['GET'])
def get_all_employees():
    
    all_employees = Employee.query.all()
    employees = process_employee_results(all_employees)
    
    return employees

@employees.route("/employee/<int:emp_id>", methods=['GET', 'POST'])
def employee(emp_id):
    
    emp = Employee.query.get_or_404(emp_id)
    if emp is None:
        abort(404)
    employee = process_employee_results(emp)
    
    return employee
