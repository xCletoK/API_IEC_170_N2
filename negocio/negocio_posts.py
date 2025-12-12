import requests
from prettytable import PrettyTable
from modelo.modelos import Post
from datos import insertar_objeto


def obtener_posts_api(url):
    tabla_posts = PrettyTable()
    tabla_posts.field_names = ["N° Usuario", "N°", "Título", "Cuerpo"]
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        listado_posts = respuesta.json()
        for usuario in listado_posts:
            tabla_posts.add_row([
                usuario['userId'],
                usuario['id'],
                usuario['title'],
                usuario['body']])
        print(tabla_posts)


def crear_post_api(url):
    url = "https://jsonplaceholder.typicode.com/posts"
    user_id = input("Ingrese el ID del usuario: ")
    titulo = input("Ingrese el título del post: ")
    cuerpo = input("Ingrese el cuerpo del post: ")

    post = {
    "userId": user_id,
    "title": titulo,
    "body": cuerpo
    }

    respuesta = requests.post(url, data=post)
    print(respuesta.text)


def modificar_post_api(url):
    id_post = input("Ingrese el ID del post a modificar: ")
    url = "https://jsonplaceholder.typicode.com/posts/" + id_post
    titulo = input("Ingrese el nuevo título del post: ")
    cuerpo = input("Ingrese el nuevo cuerpo del post: ")

    post = {
    "title": titulo,
    "body": cuerpo
    }

    respuesta = requests.put(url, data=post)
    print(respuesta.text)


def eliminar_post_api(url):
    respuesta = requests.delete(url)
    print(respuesta.text)


def crear_post_db(user_id, titulo, cuerpo):
    publicacion = Post(
        userId=user_id,
        title=titulo,
        body=cuerpo
    )
    try:
        id_publicacion = insertar_objeto(publicacion)
        return id_publicacion
    except Exception as error:
        print(f'Error al guardar el post: {error}')