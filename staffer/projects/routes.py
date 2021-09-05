from flask import Blueprint,abort
from staffer.models import Project
from staffer.utils.utils import process_project_results, get_project

projects = Blueprint('projects', __name__)


@projects.route('/projects', methods=['GET'])
def get_all_projects():
    
    all_projects = Project.query.all()
    projects = process_project_results(all_projects)
    
    return projects


@projects.route("/project/<int:emp_id>", methods=['GET'])
def employee(emp_id):
    
    proj = Project.query.get_or_404(emp_id)
    if proj is None:
        abort(404)
    project = get_project(proj)
    
    return project