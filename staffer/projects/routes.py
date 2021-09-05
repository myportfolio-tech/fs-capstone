from flask import Blueprint,abort
from staffer.models import Project
from staffer.utils.utils import json_projects_results, json_project
from staffer.utils.auth import requires_auth

projects = Blueprint('projects', __name__)


@projects.route('/projects', methods=['GET'])
def get_all_projects():
    
    all_projects = Project.query.all()
    
    return json_projects_results(all_projects)


@projects.route("/project/<int:proj_id>", methods=['GET'])
@requires_auth('get:project')
def get_project(payload, proj_id):
    
    proj = Project.query.get_or_404(proj_id)
    if proj is None:
        abort(404)

    return json_project(proj)