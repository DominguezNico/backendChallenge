from flask import request
from controllers.access import generate_token, verify_token, login
from controllers.user import read_user_by_USERNAME_controller

def login_route():
    try:
        username = request.json['username']
        password = request.json['password']
        user = read_user_by_USERNAME_controller(username)
        if login(user, password):
            token = generate_token(user["id"])
            return {'token': token}
        else:
            return {'error': 'Usuario o contraseña invalidos'}
    except:
        return {'error': 'verificar campos de request.'}
    
def puedopasar_route():
    try:
        username = request.args.get('user')
        token = request.headers.get('Authorization')
        user = read_user_by_USERNAME_controller(username)
        if verify_token(user["id"], token):
            return {'puedopasar': True}
        else:
            return {'puedopasar': False}
    except:
        return {'error': 'verificar campos de request.'}