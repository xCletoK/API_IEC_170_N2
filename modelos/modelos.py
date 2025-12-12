from sqlalchemy import ForeingKey, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Geo():
    __table_name__ = "geos"
    id = Column(Integer, primary_key=True)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)


class Address():
    __table_name__ = "addresses"
    id = Column(Integer, primary_key=True)
    street = Column(String(30), nullable=False)
    suite = Column(String(15), nullable=False)
    city = Column(String(20), nullable=False)
    zipcode = Column(String(15), nullable=False)
    geoID = Column(Integer, ForeingKey("geos.id"), nullable=False)


class Company():
    __table_name__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    catchPhrase = Column(String(100), nullable=False)
    bs = Column(String(100), nullable=False)


class User():
    __table_name__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    username = Column(String(15), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(15), nullable=False)
    website = Column(String(255), nullable=False)
    addressId = Column(Integer, ForeingKey("adresses.id"), nullable=False)
    companyId = Column(Integer, ForeingKey("companies.id"), nullable=False)


class Post():
    __table_name__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    body = Column(String(255), nullable=False)
    userId = Column(Integer, ForeingKey("users.id"), nullable=False)


class Usuario():
    __table_name__ = "usuarios"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    username = Column(String(15), nullable=False)
    email = Column(String(255), nullable=False)
    contrasena = Column(String(255), nullable=False)