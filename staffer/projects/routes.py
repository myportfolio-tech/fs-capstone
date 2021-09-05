from flask import Blueprint, jsonify
from staffer.models import Project
from staffer.utils.utils import process_project_results

projects = Blueprint('projects', __name__)


@projects.route('/projects', methods=['GET'])
def get_all_projects():
    
    all_projects = Project.query.all()
    projects = process_project_results(all_projects)
    
    return projects