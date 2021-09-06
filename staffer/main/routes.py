from flask import Blueprint, jsonify, redirect, request, Response
from staffer.utils.auth import build_auth_login

main = Blueprint('main', __name__)

@main.route('/', methods=['Get'])
def home():

    return jsonify({
        'success': True 
    })


@main.route('/login', methods=['Get'])
def login():
    
    auth0_login_path = build_auth_login()

    return redirect(auth0_login_path)  


@main.route('/callback', methods=['Get'])
def callback():

    data = request.get_json()

    return jsonify(data)