# -*- coding: utf-8 -*-

import sqlite3

def connect():
    #Connect with the database
    con = sqlite3.connect("data.db")
    con.row_factory = sqlite3.Row
    return con

def addType():
    #Name
    #type
    #Id

def addAnimal():
    #Common Name
    #Scientific Name
    #Data
    #fk_id Type

def editAnimal():

    #Edit the above
    
def addAnimalPhoto():
    #id_imagen
    #Location
    #Format
    #Resolution
    #fk_id Animal
    
def getData():
    #Gets Data from the database for display
    
