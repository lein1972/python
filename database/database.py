# database/database.py
users = []  # Simulación de una base de datos en memoria

def add_user(user):
    users.append(user)

def get_user(username):
    return next((u for u in users if u["username"] == username), None)

def get_users():
    return users