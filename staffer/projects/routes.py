from flask import Blueprint, abort, jsonify, request
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

@projects.route("/project/create", methods=['POST'])
@requires_auth('post:project')
def create_project(payload):
    
    data = request.get_json()
    tag = data.get('tag')
    name = data.get('name')
    advisor_id = data.get('advisor_id')
    manager_id = data.get('manager_id')
    director_id = data.get('director_id')

    project = Project(tag=tag, name=name, advisor_id=advisor_id, manager_id=manager_id, director_id=director_id)
    project.insert()

    proj = Project.query.filter_by(tag=tag).first()

    return jsonify({
        'success': True,
        'name': proj.name,
        'tag': proj.tag,
        'advisor_id': proj.advisor_id,
        'manager_id': proj.manager_id,
        'director_id': proj.director_id
    })