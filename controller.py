# -*- coding: utf-8 -*-

import sqlite3

def connect():
    """
    Conecta la base de datos con el programa
    """
    #Connect with the database
    con = sqlite3.connect("data.db")
    con.row_factory = sqlite3.Row
    return con

def delete(animal):
    """
    Borra el animal seleccionado
    """
    success = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM animal WHERE nombre_comun=?"
    try:
        c.execute(query, [animal])
        con.commit()
        success = True
    except sqlite3.Error as e:
        success = False
        print "Error:", e.args[0]
    con.close()
    return success

def get_animal(nombre_comun):
    """
    Obtiene un animal
    """
    #Gets Data from the database for display
    con = connect()
    c = con.cursor()
    query = """SELECT * FROM animal WHERE nombre_comun=?"""
    result = c.execute(query, [nombre_comun])
    animal = result.fetchone()
    con.close()
    return animal

def get_animals():
    """
    Obtiene todos los animales
    """
    con = connect()
    c = con.cursor()
    query = """SELECT id_animal, nombre_comun FROM animal"""
    result = c.execute(query)
    animals = result.fetchall()
    con.close()
    return animals

def get_animals_by_type(id_tipo):
    """
    Obtiene los animales por tipo
    """
    con = connect()
    c = con.cursor()
    query = """SELECT a.id_animal, a.nombre_comun, b.nombre as 'tipos'
            FROM animal a, tipo b WHERE a.fk_id_tipo = b.id_tipo
            AND a.fk_id_tipo = ?"""
    result = c.execute(query, [id_tipo])
    animals = result.fetchall()
    con.close()
    return animals

def get_animals_name():
    """
    Obtiene los animales por nombre
    """
    con = connect()
    c = con.cursor()
    query = """SELECT * FROM animal"""
    result = c.execute(query)
    animals = result.fetchall()
    wordlist = []
    for row in range(len(animals)):
        for word in range(1,5):
            wordlist.append(str(animals[row][word]))
    types = get_types()
    con.close()
    return wordlist

def search_animal(word):
    """
    Busca animales por palabra, incluye todos los parametros
    """
    con = connect()
    c = con.cursor()
    query = """SELECT a.id_animal, a.nombre_comun, a.nombre_cientifico, a.datos, b.nombre as 'tipos'
            FROM animal a, tipo b WHERE a.fk_id_tipo = b.id_tipo
            AND (a.nombre_comun LIKE '%'||?||'%' OR a.nombre_cientifico LIKE '%'||?||'%' OR a.datos
                LIKE '%'||?||'%')"""

    result = c.execute(query, [word, word, word])
    animals = result.fetchall()
    con.close()
    return animals

def get_type(nombre):
    """
    Obtiene un tipo de animal
    """
    con = connect()
    c = con.cursor()
    query = """SELECT fk_id_tipo FROM animal WHERE nombre_comun=?"""
    result = c.execute(query,[nombre])
    tipo = result.fetchone()
    #print(tipo[0])
    query = """SELECT nombre FROM tipo WHERE id_tipo=?"""
    result = c.execute(query,[tipo[0]])
    tipo = result.fetchone()
    #print(tipo[0])
    return tipo

def get_types():
    """
    Obtiene varios tipos de animales
    """
    con = connect()
    c = con.cursor()
    query = """SELECT id_tipo, nombre FROM tipo"""
    result = c.execute(query)
    types = result.fetchall()
    con.close()
    return types
