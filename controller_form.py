# -*- coding: utf-8 -*-
import sqlite3
import controller
from PySide.QtCore import QDir, QFileInfo
from PySide.QtGui import QGraphicsPixmapItem, QPixmap

def get_id_type(tipo):
    #Obtiene el tipo del animal
    con = controller.connect()
    c = con.cursor()
    query = """SELECT id_tipo FROM tipo WHERE nombre=?"""
    c.execute(query, [tipo])
    id_tipo = c.fetchone()
    result = id_tipo[0]
    con.close()
    return result

def add_image_dir(dire):
    #Agrega imagen a la base de datos
    #No relaciona la imagen con ningun animal ARREGLEN PORFA!
    con = controller.connect()
    c = con.cursor()
    direccion = (QDir.currentPath()+"/Imagenes/"+dire)
    query = "INSERT INTO imagen (ubicacion) VALUES(?) "
    c.execute(query,[direccion])
    con.commit()
    con.close

def get_image_pix():
    #Retorna la imagen almacenada en un PixMapItem para ser usada en una QGraphicsScene
    #Actualmente solo reterna la imagen de id_imagen = 4 pero puede ser arreglada para que
    #funcione con cualquier imagen de la base de datos con facilidad siempre y cuando se arregle
    #el problema de la funcion que se encuentra sobre esta ARREGLEN PORFA!!
    con = controller.connect()
    c = con.cursor()
    query = "SELECT ubicacion FROM imagen"
    c.execute(query)
    result = c.fetchone()
    direccion = result[0]
    print (direccion)
    pixMap = QPixmap(direccion)
    item = QGraphicsPixmapItem(pixMap)
    return item