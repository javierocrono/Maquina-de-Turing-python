#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('producto.db')
    con.row_factory = sqlite3.Row
    return con

def obtener(filtro):
    if filtro == "all":
        con = conectar()
        c = con.cursor()
        query = "SELECT * FROM  producto"
        resultado = c.execute(query)
        producto = resultado.fetchall()
        con.close()
        return producto
    else:
        con = conectar()
        c = con.cursor()
        query = "SELECT * FROM producto WHERE fk_id_marca=" + filtro
        resultado = c.execute(query)
        producto = resultado.fetchall()
        con.close()
        return producto