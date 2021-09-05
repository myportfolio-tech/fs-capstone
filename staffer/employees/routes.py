from flask import Blueprint, jsonify
from staffer.models import Employee
from staffer.utils.utils import process_employee_results

employees = Blueprint('employee', __name__)


@employees.route('/employees', methods=['GET'])
def get_all_employees():
    
    all_employees = Employee.query.all()
    print(all_employees)
    employees = process_employee_results(all_employees)
    
    return jsonify({
        'success': True,
        'employees': employees,
        'total': len(employees)
    })