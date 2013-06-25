# -*- coding: utf-8 -*-

import sqlite3

def connect():
    #Connect with the database
    con = sqlite3.connect("data.db")
    con.row_factory = sqlite3.Row
    return con
