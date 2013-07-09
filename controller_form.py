# -*- coding: utf-8 -*-
import sqlite3
import controller

def get_id_type(tipo):
    con = controller.connect()
    c = con.cursor()
    query = """SELECT id_tipo FROM tipo WHERE nombre=?"""
    c.execute(query, [tipo])
    id_tipo = c.fetchone()
    result = id_tipo[0]
    con.close()
    return result

def add_image_dir(dire):
	con = controller.connect()
	c = con.cursor()
	query = """INSERT INTO imagen (ubicacion) VALUES (?) """
	c.execute(query,[dire])
	con.close