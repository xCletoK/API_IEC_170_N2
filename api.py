from negocio.negocio_users import obtener_users_api, crear_user_api, modificar_user_api, eliminar_user_api
from negocio.negocio_posts import obtener_posts_api, crear_post_api, modificar_post_api, eliminar_post_api

# obtener_users_api('https://jsonplaceholder.typicode.com/users')
# obtener_posts_api('https://jsonplaceholder.typicode.com/posts')

url = 'https://jsonplaceholder.typicode.com/users'
url2 = 'https://jsonplaceholder.typicode.com/users/7'
eliminar_user_api(url2)
