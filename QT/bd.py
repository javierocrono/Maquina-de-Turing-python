#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('producto.db')
    con.row_factory = sqlite3.Row
    return con

def obtener(filtro):
    if filtro == "0":
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

    def insertar(cod, nombre, desc, col, prec, fk):
        exito = False
        conn = sqlite3.connect("producto.db")
        c = conn.cursor()
        query = """INSERT INTO Producto (codigo, nombre, descripcion, color,
        precio, fk_id_marca)
        VALUES (?, ?, ?, ?, ?, ?)"""
        valores = [cod, nombre, desc, col, prec, fk]
        try:
            c.execute(query, valores)
            conn.commit()
            exito = True
        except sqlite3.Error as e:
            exito = False
            print "Error:", e.args[0]
        conn.close()
        return exito


    def eliminar(cod):
        exito = False
        conn = sqlite3.connect("producto.db")
        c = conn.cursor()
        query = """DELETE from Producto WHERE codigo = ?"""

        try:
            exito = True
            c.execute(query, [cod])
            conn.commit()
        except qlite3.Error as e:
            exito = False
            print "Error", e.args[0]
        conn.close()
        return exito