# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('producto.db')
    con.row_factory = sqlite3.Row
    return con

def obtener():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM  producto"
    resultado = c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto