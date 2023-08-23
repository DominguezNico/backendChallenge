from flask import request
from controllers.user import create_user_controller, read_user_by_ID_controller, update_user_controller, delete_user_controller, read_user_by_USERNAME_controller,obtain_permissions_controller,grant_permissions_controller,request_permissions_controller,read_users_controller
from controllers.access import verify_token, login


# CRUD de usuarios
def create_user_route():
    try:
        user_data = request.json
        user_data["username"]=str(user_data["username"])
        user_data["mail"]=str(user_data["mail"])
        user_data["password"]=str(user_data["password"])

        if(user_data["mail"] == "" or user_data["username"] == "" or user_data["password"] == ""):
            return {'error': 'Faltan datos.'}
        
        if(user_data["mail"].find("@") == -1):
            return {'error': 'Mail invalido.'}
        
        user = create_user_controller(user_data)
        return user
    except:
        return {'error': 'verificar campos de request.'}

#Read one
def read_user_route_by_ID(user_id):
    try:
        id=str(user_id)
        user = read_user_by_ID_controller(id)
        return user
    except:
        return {'error': 'verificar campos de request.'}

#Read many
def read_users_route():
    try:
        if(request.args.get('per_page') is None or request.args.get('per_page') == ''):
            per_page=10
        else:
            per_page= request.args.get('per_page')
        if(request.args.get('page') is None or  request.args.get('page') == ''):
            page=1
        else:
            page= request.args.get('page')

        users = read_users_controller(per_page,page)
        return users
    except:
        return {'error': 'verificar campos de request.'}

def update_user_route(user_id):
    try:
        user_data = request.json
        token = request.headers.get('Authorization')

        if(user_data.get('username') is not None):
            user_data["username"]=str(user_data["username"])
        if(user_data.get('mail') is not None):
            user_data["mail"]=str(user_data["mail"])
            if(user_data["mail"].find("@") == -1):
                return {'error': 'Mail invalido.'}
        if(user_data.get('password') is not None):
            user_data["password"]=str(user_data["password"])
        if('rol' in user_data):
            del user_data['rol']
        if('permisos_pedidos' in user_data):
            del user_data['permisos_pedidos']

        if verify_token(user_id, token):
            user = update_user_controller(user_id, user_data)
            return user
        else:
            return {'error': 'Token no valido.'}
    except:
        return {'error': 'verificar campos de request.'}

# Delete (Logico)
def delete_user_logico_route(user_id):
    try:
        id=str(user_id)
        token = request.headers.get('Authorization')
        if verify_token(id, token):
            user_data = read_user_by_ID_controller(id)
            user_data["activo"]=False
            user = update_user_controller(id, user_data)
            return user
        else:
            return {'error': 'Token no valido.'}
    except:
        return {'error': 'verificar campos de request.'}

# Delete (Permanente)
def delete_user_route(user_id):
    try:
        id=str(user_id)
        token = request.headers.get('Authorization')
        if verify_token(id, token):
            user = delete_user_controller(id)
            return user
        else:
            return {'error': 'Token no valido.'}
    except:
        return {'error': 'verificar campos de request.'}
    
    
# Solicitud de permisos de ADMIN
def request_permissions_route(user_id):
    try:
        token = request.headers.get('Authorization')
        if verify_token(user_id, token):
            if(request_permissions_controller(user_id)):
                return {'message': 'Permisos solicitados.'}
        else:
            return {'error': 'Token no valido.'}
    except:
        return {'error': 'verificar campos de request.'}


# Usuario ADMIN
def obtain_permissions_route():
    try:
        user_data = request.json
        token = request.headers.get('Authorization')
        username=str(user_data["username"])
        password =  str(user_data["password"])


        user_admin = read_user_by_USERNAME_controller(username)

        if(not login(user_admin,password)):
            return {'message': "usuario o contraseña incorrectos"}
        
        if(user_admin["rol"] != "admin"):
            return {'message': "usuario no es admin"}

        if verify_token(user_admin["id"], token):
            users = obtain_permissions_controller()
            return users
        else:
            return {'error': 'Token no valido.'}
    except:
        return {'error': 'verificar campos de request.'}


def grant_permissions_route(user_id):
    try:
        user_data = request.json
        token = request.headers.get('Authorization')

        username=str(user_data["username"])
        password =  str(user_data["password"])

        user_admin = read_user_by_USERNAME_controller(username)

        if(not login(user_admin,password)):
            return {'message': "usuario o contraseña incorrectos"}
        
        if(user_admin["rol"] != "admin"):
            return {'message': "usuario no es admin"}

        if verify_token(user_admin["id"], token):
            if(grant_permissions_controller(user_id)):
                return {'message': 'Permisos otorgados.'}
        else:
            return {'error': 'Token no valido.'}
    except:
        return {'error': 'verificar campos de request.'}