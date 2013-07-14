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
    c.execute(query, [animal])
    id_animal = c.fetchone()
    result = id_animal[0]
    con.close()
    return result

def add_image_dir(animal,dire):
    #Agrega la imagen a la base de datos
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
    #print (path+format)
    query = """INSERT INTO imagen (ubicacion,formato,fk_id_animal) VALUES(?,?,?)"""
    c.execute(query,[path,format,animal])
    con.commit()
    con.close

def get_image_pix(id_animal):
    #Carga la imagen ya almacenada en la base de datos
    con = controller.connect()
    c = con.cursor()
    query = """SELECT ubicacion, formato FROM imagen WHERE fk_id_animal = ?"""
    c.execute(query,[id_animal])
    result = c.fetchone()
    path = result[0]
    format = result[1]
    image = QDir.currentPath()+"/Imagenes/"+path+format
    pixMap = QPixmap(image)
    item = QGraphicsPixmapItem(pixMap)
    return item

def get_root_image(now):
    #Carga la imagen desde la ruta actual sin almacenarla en la base de datos
    pixMap = QPixmap(now)
    item = QGraphicsPixmapItem(pixMap)
    return item
