from models.user import create_user, read_user_by_ID, read_user_by_USERNAME, update_user, delete_user, obtain_permissions,grant_permissions,read_users
from controllers.access import encrypt_password

# CRUD de usuarios
def create_user_controller(user_data):
    #encripto la password
    user_data['password'] = encrypt_password(user_data['password'])
    user = create_user(user_data)
    return user

#Read one
def read_user_by_ID_controller(user_id):
    user = read_user_by_ID(user_id)
    return user

#Read many
def read_users_controller(per_page,page):
    users = read_users(per_page,page)
    return users

def read_user_by_USERNAME_controller(user_name):
    user = read_user_by_USERNAME(user_name)
    return user

def update_user_controller(user_id, user_data):
    if(user_data.get('password') is not None):
        user_data['password'] = encrypt_password(user_data['password'])
    user = update_user(user_id, user_data)
    return user

def delete_user_controller(user_id):
    user = delete_user(user_id)
    return user

# Solicitud de permisos de ADMIN
def request_permissions_controller(user_id):
    user = read_user_by_ID(user_id)
    user['permisos_pedidos'] = True
    user = update_user(user_id, user)
    return user

# Usuario ADMIN
def obtain_permissions_controller():
    users = obtain_permissions()
    return users

def grant_permissions_controller(user_id):
    return grant_permissions(user_id)