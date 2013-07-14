# -*- coding: utf-8 -*-
import sqlite3
import controller
from PySide.QtCore import QDir, QFileInfo
from PySide.QtGui import QGraphicsPixmapItem, QPixmap

def get_id_type(tipo):
    #Obtiene el id del tipo
    con = controller.connect()
    c = con.cursor()
    query = """SELECT id_tipo FROM tipo WHERE nombre=?"""
    c.execute(query, [tipo])
    id_tipo = c.fetchone()
    result = id_tipo[0]
    con.close()
    return result

def get_id_animal(animal):
    #Obtiene el id del animal
    con = controller.connect()
    c = con.cursor()
    query = """SELECT id_animal FROM animal WHERE nombre_comun=?"""
    c.execute(query,[animal])
    id_animal = c.fetchone()
    result = id_animal[0]
    con.close()
    return result

def add_image_dir(animal,dire):
    #Agrega imagen a la base de datos
    #No relaciona la imagen con ningun animal ARREGLEN PORFA!
    con = controller.connect()
    c = con.cursor()
    pos = 0
    path = ""
    while dire[pos] != ".":
        path = path + dire[pos]
        pos += 1
    format = ""
    while pos <= len(dire)-1:
        format = format + dire[pos]
        pos += 1
    print (path+format)
    query = """INSERT INTO imagen (ubicacion,formato,fk_id_animal) VALUES(?,?,?)"""
    c.execute(query,[path,format,animal])
    con.commit()
    con.close

def get_image_pix():
    #Retorna la imagen almacenada en un PixMapItem para ser usada en una QGraphicsScene
    #Actualmente solo reterna la imagen de id_imagen = 4 pero puede ser arreglada para que
    #funcione con cualquier imagen de la base de datos con facilidad siempre y cuando se arregle
    #el problema de la funcion que se encuentra sobre esta ARREGLEN PORFA!!
    con = controller.connect()
    c = con.cursor()
    query = "SELECT ubicacion, formato, fk_id_animal FROM imagen"
    c.execute(query)
    result = c.fetchone()
    path = result[0]
    format = result[1]
    key = result[2]
    #print (QDir.currentPath()+"/Imagenes/"+path+format)
    image = QDir.currentPath()+"/Imagenes/"+path+format
    pixMap = QPixmap(image)
    item = QGraphicsPixmapItem(pixMap)
    return item
