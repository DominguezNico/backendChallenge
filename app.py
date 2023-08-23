from flask import Flask
from views.user import create_user_route, read_user_route_by_ID, update_user_route, delete_user_route, obtain_permissions_route, grant_permissions_route,request_permissions_route,read_users_route,delete_user_logico_route
from views.access import login_route, puedopasar_route


app = Flask(__name__)

# Autenticacion de usuarios
@app.route('/login', methods=['POST'])
def login():
    return login_route()

@app.route('/puedopasar', methods=['GET'])
def puedopasar():
    return puedopasar_route()

# CRUD de usuarios:
# Create
@app.route('/user', methods=['POST'])
def create_user():
    return create_user_route()
# Read one
@app.route('/user/<user_id>', methods=['GET'])
def read_user(user_id):
    return read_user_route_by_ID(user_id)

# Read many
@app.route('/users', methods=['GET'])
def read_users():
    return read_users_route()

# Update
@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    return update_user_route(user_id)

# Delete (Logico)
@app.route('/user/<user_id>', methods=['PATCH'])
def delete_user_logico(user_id):
    return delete_user_logico_route(user_id)


# Delete (Permanente)
@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete_user_route(user_id)

# Solicitar permisos de Admin
@app.route('/user/solicitarPermisos/<user_id>', methods=['POST'])
def request_permissions(user_id):
    return request_permissions_route(user_id)

# Admin
@app.route('/admin/obtenerPermisos', methods=['GET'])
def obtain_permissions():
    return obtain_permissions_route()

@app.route('/admin/darPermisos/<user_id>', methods=['POST'])
def grant_permissions(user_id):
    return grant_permissions_route(user_id)


# ----------------------------------------------
if __name__ == '__main__':
    app.run()
