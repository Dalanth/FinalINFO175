# -*- coding: utf-8 -*-

import sqlite3

def connect():
    #Connect with the database
    con = sqlite3.connect("data.db")
    con.row_factory = sqlite3.Row
    return con

def addType():
    x=1
    #Name
    #type
    #Id

def addAnimal():
    x=1
    #Common Name
    #Scientific Name
    #Data
    #fk_id Type

def editAnimal():

    #Edit the above
    x=1
    
def addAnimalPhoto():
    #id_imagen
    #Location
    #Format
    #Resolution
    #fk_id Animal
    x=1
    
def getData():
    #Gets Data from the database for display
    x=1
    
