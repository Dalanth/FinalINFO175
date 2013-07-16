# -*- coding: utf-8 -*-
import sqlite3
import controller
from PySide.QtCore import QDir, QFileInfo
from PySide.QtGui import QGraphicsPixmapItem, QPixmap, QImage

def add_animal(common,cientific,data,id_type):
    """
    Agrega un nuevo animal a la base de datos
    """
    success = False
    con = controller.connect()
    c = con.cursor()
    values = [common,cientific,data,id_type]
    query = """INSERT INTO animal (nombre_comun, nombre_cientifico, datos, fk_id_tipo) VALUES(?,?,?,?)"""
    try:
        result = c.execute(query, values)
        success = True
        con.commit()
    except sqlite3.Error as e:
        success = False
        print "Error: ", e.args[0]
    con.close()
    return success

def get_id_type(tipo):
    """
    Obtiene el id del tipo
    """
    con = controller.connect()
    c = con.cursor()
    query = """SELECT id_tipo FROM tipo WHERE nombre=?"""
    c.execute(query, [tipo])
    id_tipo = c.fetchone()
    result = id_tipo[0]
    con.close()
    return result

def get_id_animal(animal):
    """
    Obtiene el id del animal
    """
    con = controller.connect()
    c = con.cursor()
    query = """SELECT id_animal FROM animal WHERE nombre_comun=?"""
    c.execute(query, [animal])
    id_animal = c.fetchone()
    result = id_animal[0]
    con.close()
    return result

def add_image_dir(animal,path):
    """
    Agrega la imagen a la base de datos
    """
    con = controller.connect()
    c = con.cursor()
    pos = 0
    name = ""
    while path[pos] != ".":
        name = name + path[pos]
        pos += 1
    format = ""
    while pos <= len(path)-1:
        format = format + path[pos]
        pos += 1
    query = """INSERT INTO imagen (ubicacion,formato,fk_id_animal) VALUES(?,?,?)"""
    c.execute(query,[name,format,animal])
    con.commit()
    con.close

def get_image_pix(id_animal):
    """
    Carga la imagen ya almacenada en la base de datos
    """
    con = controller.connect()
    c = con.cursor()
    query = """SELECT ubicacion, formato FROM imagen WHERE fk_id_animal=?"""
    c.execute(query,[id_animal])
    result = c.fetchone()
    if result:
        path = result[0]
        format = result[1]
        image = QDir.currentPath()+"/images/"+path+format
        pixMap = QPixmap(image)
        return pixMap

def get_root_image(path):
    """
    Carga la imagen desde la ruta solicitada sin almacenarla en la base de datos
    """
    pixMap = QPixmap(path)
    return pixMap

def get_image(id_animal):
    con = controller.connect()
    c = con.cursor()
    query = """SELECT ubicacion, formato FROM imagen WHERE fk_id_animal=?"""
    c.execute(query,[id_animal])
    image = c.fetchone()
    return image

def edit_animal(id_animal,common,cientific,data,id_type):
    """
    Add a new product to the table 'product' on the database
    """
    success = False
    con = controller.connect()
    c = con.cursor()
    values = [common,cientific,data,id_type,id_animal]
    query = """UPDATE animal SET nombre_comun=?, nombre_cientifico =?,
            datos=?, fk_id_tipo=? WHERE id_animal=?"""
    try:
        result = c.execute(query, values)
        success = True
        con.commit()
    except sqlite3.Error as e:
        success = False
        print "Error: ", e.args[0]
    con.close()
    return success

def del_image(path):
    """
    Borra la imagen de un animal
    """
    success = False
    con = controller.connect()
    c = con.cursor()
    pos = 0
    name = ""
    if path != "":
        while path[pos] != ".":
            name = name + path[pos]
            pos += 1
        query = """DELETE FROM imagen WHERE ubicacion=?"""
        try:
            c.execute(query,[name])
            con.commit()
            success = True
        except sqlite3.Error as e:
            success = False
            print "Error:", e.args[0]
        con.close()
        return success
    else:
        return success

def no_image():
    """
    Si no existe imagen carga una por defecto
    """
    path = QDir.currentPath() + "/images/noimage.jpg"
    pixMap = QPixmap(path)
    return pixMap

def search_image(id_animal, Ifile):
    """Busca imagen de un animal
    """
    success = False
    con = controller.connect()
    c = con.cursor()
    query = """SELECT ubicacion, formato FROM imagen WHERE fk_id_animal =?"""
    c.execute(query,[id_animal])
    result = c.fetchone()
    try:
        if not result:
            success = True
    except:
        print "asdfasdf"
        success = False
    return success
