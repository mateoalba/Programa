# autenticacion.py
def autenticar(usuario, contrasena):
    if usuario == "admin" and contrasena == "1234":
        return True
    return False
