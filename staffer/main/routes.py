from flask import Blueprint, jsonify, redirect, request, Response
from staffer.utils.auth import build_auth_login

main = Blueprint('main', __name__)

@main.route('/')
def home():

    return jsonify({
        'success': True 
    })


@main.route('/login')
def login():
    
    auth0_login_path = build_auth_login()

    return redirect(auth0_login_path)  


@main.route('/callback')
def callback():

    url = request.url
    token = request.args.get('access_token')


    return jsonify({
        'success': True,
        'url': url,
        'token': token
    })