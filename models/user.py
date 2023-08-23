import json

def create_user(user_data):
    # Crear un nuevo usuario y almacenarlo en el archivo JSON
    users = []
    try:
        with open('models/users.json', 'r') as file:
            users = json.load(file)
    except:
        # Si el archivo esta vacio o no contiene JSON valido, crear una lista vacia
        users = []
    # Verificar si el nombre de usuario o correo electronico ya estan en uso
    for user in users:
        if user['username'] == user_data['username']:
            return {'error': 'El nombre de usuario ya está en uso'}
        if user['mail'] == user_data['mail']:
            return {'error': 'El correo electrónico ya está en uso'}
    # Asignar un ID unico al usuario
    user_data['id'] = str(len(users) + 1)
    user_data['rol'] = 'user'
    user_data['permisos_pedidos'] = False
    user_data['activo'] = True

    users.append(user_data)
    with open('models/users.json', 'w') as file:
        json.dump(users, file)
    return user_data


def read_user_by_ID(user_id):
    try:
        # Leer los datos de un usuario a partir de su ID
        with open('models/users.json', 'r') as file:
            users = json.load(file)
            for user in users:
                if user['id'] == str(user_id):
                    #devuelvo al usuario pero sin su contraseña
                    usuario_sin_pass = user.copy()
                    del usuario_sin_pass['password']
                    return usuario_sin_pass
            return None
    except:
        return {'error': 'Error al cargar el archivo JSON'}

def read_user_by_USERNAME(user_name):
    try:
        # Leer los datos de un usuario a partir de su ID
        with open('models/users.json', 'r') as file:
            users = json.load(file)
            for user in users:
                if user['username'] == str(user_name):
                    return user
            return None
    except:
        return {'error': 'Error al cargar el archivo JSON'}

def read_users(per_page, page):
    try:
        # Leer los datos de un usuario a partir de su ID
        with open('models/users.json', 'r') as file:
            users = json.load(file)
            start = (int(page) - 1) * int(per_page)
            end = int(page) * int(per_page)
            users_paginated = users[start:end]
            for user in users_paginated:
                #devuelvo al usuario pero sin su contraseña
                del user['password']
            return users_paginated
    except:
        return {'error': 'Error al cargar el archivo JSON'}

def update_user(user_id, user_data):
    try:
        # Actualizar los datos de un usuario a partir de su ID
        with open('models/users.json', 'r') as file:
            users = json.load(file)
            for user in users:
                if user['id'] == str(user_id):
                    # Verificar si el nombre de usuario o correo electronico ya estan en uso por otro usuario
                    for other_user in users:
                        if other_user['id'] != str(user_id):
                            if user_data.get('username') is not None and other_user['username'] == user_data['username']:
                                return {'error': 'El nombre de usuario ya está en uso'}
                            if user_data.get('mail') is not None and other_user['mail'] == user_data['mail']:
                                return {'error': 'El correo electrónico ya está en uso'}
                    # Actualizar los datos del usuario
                    if(user_data.get('username') is not None):
                        user['username'] = user_data['username']
                    if(user_data.get('mail') is not None):
                        user['mail'] = user_data['mail']
                    if user_data.get('password') is not None:
                        user['password'] = user_data['password']
                    if(user_data.get('rol') is not None):
                        user['rol'] = user_data['rol']
                    if(user_data.get('permisos_pedidos') is not None):
                        user['permisos_pedidos'] = user_data['permisos_pedidos']
                    else:
                        user['permisos_pedidos'] = False
                    if('activo' in user_data and user_data.get('activo') is not None):
                        user['activo'] = user_data['activo']
                    else:
                        user['activo'] = True
                    break
        with open('models/users.json', 'w') as file:
            json.dump(users, file)
        
        return {'message': 'Cambios realizados con exito'}
    except:
        return {'error': 'Error al cargar el archivo JSON'}


def delete_user(user_id):
    try:
        # Eliminar un usuario a partir de su ID
        with open('models/users.json', 'r') as file:
            users = json.load(file)
            found = False
            for user in users:
                if user['id'] == str(user_id):
                    users.remove(user)
                    found = True
                    break
        if not found:
            return {'error': 'Usuario no encontrado'}
        with open('models/users.json', 'w') as file:
            json.dump(users, file)
        return user
    except:
        return {'error': 'Error al cargar el archivo JSON'}


# Usuario ADMIN
def obtain_permissions():
    try:
        # Leer los datos de un usuario a partir de su ID
        with open('models/users.json', 'r') as file:
            users = json.load(file)
            users_admin = []
            for user in users:
                if user['permisos_pedidos'] == True and user['rol'] == 'user':
                    users_admin.append(user)
            return users_admin
    except:
        return {'error': 'Ningun usuario solicito permisos.'}
    

def grant_permissions(user_id):
    try:
        # Actualizar los datos de un usuario a partir de su ID
        with open('models/users.json', 'r') as file:
            users = json.load(file)
            for user in users:
                if user['id'] == str(user_id):
                    user['rol'] = 'admin'
                    user['permisos_pedidos'] = False
                    break
        with open('models/users.json', 'w') as file:
            json.dump(users, file)
        return user
    except:
        return {'error': 'Error al cargar el archivo JSON'}