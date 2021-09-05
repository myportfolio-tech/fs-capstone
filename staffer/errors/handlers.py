from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(auth_error):

    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not Found"
    }), 404


@errors.app_errorhandler(400)
def error_400(auth_error):

    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400


@errors.app_errorhandler(403)    
def error_403(auth_error):

    return jsonify({
        "success": False,
        "error": 403,
        "message": "Forbiden"
    }), 403


@errors.app_errorhandler(405)    
def error_405(auth_error):

    return jsonify({
        "success": False,
        "error": 405,
        "message": "Method Not Allowed"
    }), 405


@errors.app_errorhandler(500)
def error_500(auth_error):

    return jsonify({
        "success": False, 
        "error": auth_error.status_code,
        "message": auth_error.error['description']
    }), auth_error.status_code