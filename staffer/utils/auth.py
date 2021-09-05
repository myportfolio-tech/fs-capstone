import json
from flask import request, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen
import os


AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
ALGORITHMS = os.environ.get('ALGORITHMS')
API_AUDIENCE = os.environ.get('AUTH0_AUDIENCE')
AUTH0_AUDIENCE = os.environ.get('AUTH0_AUDIENCE')
AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID')
AUTH0_CALLBACK_URL = os.environ.get('AUTH0_CALLBACK_URL')

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

def get_token_auth_header():
    
    auth = request.headers.get('Authorization', None)


    if not auth:
        abort(401, {
            'code': 'authorization_header_missing',
            'description': 'Authorization header is expected.'
        })
        # raise AuthError({
        #     'code': 'authorization_header_missing',
        #     'description': 'Authorization header is expected.'
        # }, 401)
   
    parts = auth.split()   
    token = parts[1]

    # print('TOKEN')
    # print(token)

    return token

def check_permissions(permission, payload):
    
    if 'permissions' not in payload:
        abort(400, {
                    'code': 'invalid_claims',
                    'description': 'Permissions not included in JWT.'
                    })
                        # raise AuthError({
                        #     'code': 'invalid_claims',
                        #     'description': 'Permissions not included in JWT.'
                        # }, 400)

    if permission not in payload['permissions']:
        abort(403, {
            'code': 'unauthorized',
            'description': 'Permission not found.'
        })
        # raise AuthError({
        #     'code': 'unauthorized',
        #     'description': 'Permission not found.'
        # }, 403)
    
    return True

def verify_decode_jwt(token):
    
    # GET THE PUBLIC KEY FROM AUTH0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())

    # GET THE DATA IN THE HEADER
    unverified_header = jwt.get_unverified_header(token)
    
    # CHOOSE OUR KEY
    rsa_key = {}
    if 'kid' not in unverified_header:
        abort(401, {
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        })
        # raise AuthError({
        #     'code': 'invalid_header',
        #     'description': 'Authorization malformed.'
        # }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    
    # Finally, verify!!!
    if rsa_key:
        try:
            # USE THE KEY TO VALIDATE THE JWT
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            abort(401)
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            abort(401, {
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            })
            # raise AuthError({
            #     'code': 'invalid_claims',
            #     'description': 'Incorrect claims. Please, check the audience and issuer.'
            # }, 401)
        except Exception:
            abort(400, {
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            })
            # raise AuthError({
            #     'code': 'invalid_header',
            #     'description': 'Unable to parse authentication token.'
            # }, 400)
    raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
            }, 400)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)

            check_permissions(permission, payload)   
            
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator


def build_auth_login():

    auth_path = f'https://{AUTH0_DOMAIN}/authorize?audience={AUTH0_AUDIENCE}&response_type=token&client_id={AUTH0_CLIENT_ID}&redirect_uri={AUTH0_CALLBACK_URL}'
    return auth_path