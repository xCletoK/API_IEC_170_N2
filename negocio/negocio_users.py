import requests
from prettytable import PrettyTable
from modelo.modelos import User
from datos import insertar_objeto, obtener_user_name


def obtener_users_api(url):
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ["N°", "Nombre", "Nombre Usuario", "Email", "Latitud"]
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        listado_usuarios = respuesta.json()
        for usuario in listado_usuarios:
            tabla_usuarios.add_row([
                usuario['id'],
                usuario['name'],
                usuario['username'],
                usuario['email'],
                usuario['address']["geo"]['lat']])
        print(tabla_usuarios)


def crear_user_api(url):
    url = "https://jsonplaceholder.typicode.com/users"
    nombre = input("Ingrese el nombre del usuario: ")
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    correo = input("Ingrese el correo electrónico: ")
    telefono = input("Ingrese el teléfono: ")
    sitio_web = input("Ingrese el sitio web: ")

    user = {
    "name": nombre,
    "username": nombre_usuario,
    "email": correo,
    "phone": telefono,
    "website": sitio_web
    }

    respuesta = requests.post(url, data=user)
    print(respuesta.text)


def modificar_user_api(url):
    id_user = input("Ingrese el ID del usuario a modificar: ")
    url = "https://jsonplaceholder.typicode.com/users/" + id_user
    nombre = input("Ingrese el nuevo nombre del usuario: ")
    nombre_usuario = input("Ingrese el nuevo nombre de usuario: ")
    correo = input("Ingrese el nuevo correo electrónico: ")
    telefono = input("Ingrese el nuevo teléfono: ")
    sitio_web = input("Ingrese el nuevo sitio web: ")

    user = {
    "name": nombre,
    "username": nombre_usuario,
    "email": correo,
    "phone": telefono,
    "website": sitio_web
    }

    respuesta = requests.put(url, data=user)
    print(respuesta.text)


def eliminar_user_api(url):
    respuesta = requests.delete(url)
    print(respuesta.text)


def buscar_user_db_name(nombre):
    if nombre != '':
        user = obtener_user_name(nombre)
        if user != None:
            return user

def guardar_user_db(nombre, nombre_usuario, correo, telefono, sitio_web, direccion_id, compania_id):
    usuario = User(
        name=nombre,
        username=nombre_usuario,
        email=correo,
        phone=telefono,
        website=sitio_web,
        addressId=direccion_id,
        companyId=compania_id
    )
    user = buscar_user_db_name(nombre)
    if not user:
        try:
            id_usuario = insertar_objeto(usuario)
            return id_usuario
        except Exception as error:
            print(f'Error al guardar el usuario: {error}')
    else:
        print('Usuario ya existe, no será agregado.')

def crear_user_db(nombre, nombre_usuario, correo, telefono, sitio_web, direccion_id, compania_id):
    usuario = User(
        name=nombre,
        username=nombre_usuario,
        email=correo,
        phone=telefono,
        website=sitio_web,
        addressId=direccion_id,
        companyId=compania_id
    )
    try:
        id_usuario = insertar_objeto(usuario)
        return id_usuario
    except Exception as error:
        print(f'Error al guardar el usuario: {error}')

def modificar_user_db(usuario, nombre, nombre_usuario, correo, telefono, sitio_web, direccion_id, compania_id):
    from datos.conexion import sesion
    try:
        usuario.name = nombre
        usuario.username = nombre_usuario
        usuario.email = correo
        usuario.phone = telefono
        usuario.website = sitio_web
        usuario.addressId = direccion_id
        usuario.companyId = compania_id
        sesion.commit()
        print("El usuario se ha modificado correctamente.")
    except Exception as error:
        sesion.rollback()
        print(f"Error al modificar el usuario: {error}")
    finally:
        sesion.close()


def eliminar_user_db(usuario):
    from datos.conexion import sesion
    try:
        sesion.delete(usuario)
        sesion.commit()
        print("El usuario se ha eliminado correctamente.")
    except Exception as error:
        sesion.rollback()
        print(f"Error al eliminar el usuario: {error}")
    finally:
        sesion.close()
=======
import requests

def obtener_usuarios_api(url):
    respuesta = requests.get(url)
    if respuesta.status_code==200:
        print(respuesta)
