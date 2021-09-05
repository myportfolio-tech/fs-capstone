from flask import Blueprint,abort
from staffer.models import Project
from staffer.utils.utils import process_project_results, get_project
from staffer.utils.auth import requires_auth

projects = Blueprint('projects', __name__)


@projects.route('/projects', methods=['GET'])
def get_all_projects():
    
    all_projects = Project.query.all()
    projects = process_project_results(all_projects)
    
    return projects


@projects.route("/project/<int:proj_id>", methods=['GET'])
@requires_auth('get:project')
def get_project(payload, proj_id):
    
    proj = Project.query.get_or_404(proj_id)
    if proj is None:
        abort(404)
    project = get_project(proj)
    
    return project