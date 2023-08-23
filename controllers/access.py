import jwt
from werkzeug.security import check_password_hash, generate_password_hash
from models.user import read_user_by_USERNAME

#Clave secreta
SECRET_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlBydWViYSJ9.GzIP24UO58gmBs4nTMdPh79Zdomtw3JVUQxPv0dQDiE'

# Autenticacion de usuarios
def login(user, password):
    #Verifico si el nombre de usuario y la contraseña son correctos 
    #comparando la contraseña almacenada con check_password_hash
    if user:
        return check_password_hash(user['password'], password)
    else:
        return False

# Gestion de Tokens.
def generate_token(id):
    payload = {'id': id}
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verify_token(id, token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['id'] == id
    except:
        return False

# Encripto password
def encrypt_password(password):
    return generate_password_hash(password)
