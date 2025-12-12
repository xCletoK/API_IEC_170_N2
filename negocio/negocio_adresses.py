import requests
from prettytable import PrettyTable
from datos import insertar_objeto
from modelo.modelos import Address


def crear_direccion_db(calle, departamento, ciudad, codigo_postal, geolocalizacion):
    direccion = Address(
        street=calle,
        suite=departamento,
        city=ciudad,
        zipcode=codigo_postal,
        geoId=geolocalizacion
    )
    try:
        id_direccion = insertar_objeto(direccion)
        return id_direccion
    except Exception as error:
        print(f'Error al guardar la dirección: {error}')