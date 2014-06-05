#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sqlite3


def crear_productoBD(db_name):
    #crea la base de datos 'producto' la cual consta de 2 tablas
    #la table Marca y la tabla Producto
    conn = sqlite3.connect('producto.db')
    c = conn.cursor()
    query = """CREATE TABLE Marca(
        id_marca integer  primary key AUTOINCREMENT,
        nombre text,
        descripcion text,
        pais text)"""
    c.execute(query)
    query = """CREATE TABLE Producto(
        codigo text primary key,
        nombre text,
        descripcion text,
        color text,
        precio integer)
        """
    c.execute(query)



def agregar_marca(name, desc, pais):
    #metodo para agregar marcas nuevas a la tabla de productos del a base de datos
    exito = False
    conn = sqlite3.connect("producto.db")
    c = conn.cursor()
    query = """ INSERT INTO Marca (nombre, descripcion, pais) VALUES (?, ?, ?)"""
    valores = [name, desc, pais]
    try:
        c.execute(query, valores)
        conn.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    conn.close()
    return exito


def agregar_producto(cod, nombre, desc, col, prec):
    #metodo para agregar productos nuevos a la tabla productos de la base de datos
    exito = False
    conn = sqlite3.connect("producto.db")
    c = conn.cursor()
    query = """INSERT INTO Producto (codigo, nombre, descripcion, color, precio)
    VALUES (?, ?, ?, ?, ?)"""
    valores = [cod, nombre, desc, col, prec]
    try:
        c.execute(query, valores)
        conn.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito


def inicializa_BD():
    #para inicializar la base de datos con algunos datos
    agregar_marca("Nike", "marca de zapatillas", "Taiwan")
    agregar_marca("HP", "Hewlett-Packard, empresa de tecnologia", "EEUU")
    agregar_marca("Dell", """ compañía multinacional estadounidense establecida en Round Rock que desarrolla,
         fabrica, vende y da soporte a computadoras personales""", "EEUU")
    agregar_marca("Puma", "Empresa fabricante de ropa y calzado deportivo", "Alemania")
    agregar_marca("Samsung", "Empresa dedicada a la industria electronica", "Corea del Sur")
    agregar_producto("001", "taza", "tazon para el regalon", "rojo", "1900")
    agregar_producto("002","Samsung Galaxy Grand", "Celular marca Samsung", "negro", "200000")
    agregar_producto("003", "Samsung Galaxy S3","Celular", "negro", "150000")
    agregar_producto("004", "Samsung Galaxy s4", "Celular", "blaco", "210000")
    agregar_producto("005", "zapatillas", "zapatillas Nike", "rojas", "54990")
    agregar_producto("006", "Hp Pavilon", "Notebook HP Pavilon 15", "gris", "459000")
    agregar_producto("007", "Poleron", "Poleron Puma", "gris", "25990")


if __name__ == "__main__":
    db_name = 'producto.db'
    if not os.path.exists(db_name):
        crear_productoBD(db_name)
        inicializa_BD()

    conn = sqlite3.connect("producto.db")
    c = conn.cursor()

    #for row in c.execute("SELECT * FROM Marca"):
        #print row
    #for row in c.execute("SELECT precio FROM Producto"):
    #    print row

    #x = (c.execute("""SELECT precio FROM Producto WHERE codigo = "001" """)).fetchone()


