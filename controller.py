# -*- coding: utf-8 -*-

import sqlite3

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
