# -*- coding: utf-8 -*-

import sqlite3

def add_animal(nombre,nombrec,datos,tipo):
    #Add a new product to the table 'product' on the database
    success = False
    con = connect()
    c = con.cursor()
    values = [nombre,nombrec,datos,tipo]
    query = "INSERT INTO product (nombre_comun, nombre_cientifico, datos, fk_id_tipo) VALUES(?,?,?,?)"
    try:
        result = c.execute(query, values)
        success = True
        con.commit()
    except sqlite3.Error as e:
        success = False
        print "Error: ", e.args[0]
    con.close()
    return success

def connect():
    #Connect with the database
    con = sqlite3.connect("data.db")
    con.row_factory = sqlite3.Row
    return con
    
def get_animal(nombre_comun):
    #Gets Data from the database for display
    con = connect()
    c = con.cursor()
    query = "SELECT * FROM animal WHERE nombre_comun = ?"
    result = c.execute(query, [nombre_comun])
    animal = result.fetchone()
    con.close()
    return animal

def get_animals():
    con = connect()
    c = con.cursor()
    query = """SELECT id_animal, nombre_comun FROM animal"""
    result = c.execute(query)
    animals = result.fetchall()
    con.close()
    return animals

def get_type(nombre):
    con=connect()
    c=con.cursor()
    query="SELECT fk_id_tipo FROM animal WHERE nombre_comun=?"
    result=c.execute(query,[nombre])
    tipo=result.fetchone()
    print(tipo[0])
    query="SELECT nombre FROM tipo WHERE id_tipo=?"
    result=c.execute(query,[tipo[0]])
    tipo=result.fetchone()
    print(tipo[0])
    return tipo

def get_types():
    con = connect()
    c = con.cursor()
    query = """SELECT id_tipo, nombre FROM tipo"""
    result = c.execute(query)
    types = result.fetchall()
    con.close()
    return types
