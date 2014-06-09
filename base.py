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
        precio integer,
        fk_id_marca integer,
        FOREIGN KEY (fk_id_marca) REFERENCES Marca (id_marca))
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


def consulta_mnombre_nombre(name):
    #Funcion para consultar por una marca segun nombre
    #retorna el Pk ID de la marca
    conn = sqlite3.connect("producto.db")
    c = conn.cursor()
    query = """SELECT id_marca FROM Marca WHERE nombre LIKE '%"""+name+"""%'"""
    r = (c.execute(query).fetchall())
    if r == None:
        r="Elemento no encontrado"
    return r



def agregar_producto(cod, nombre, desc, col, prec, fk):
    #metodo para agregar productos nuevos a la tabla productos de la base de datos
    exito = False
    conn = sqlite3.connect("producto.db")
    c = conn.cursor()
    query = """INSERT INTO Producto (codigo, nombre, descripcion, color, precio, fk_id_marca)
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


def consultar_pnombre_nombre(name):
    #consultar por un producto segun nombre
    conn = sqlite3.connect("producto.db")
    c = conn.cursor()
    query = """SELECT * FROM Producto WHERE nombre LIKE '%"""+name+"""%'"""
    r = (c.execute(query).fetchall())
    if r == None:
        r="Elemento no encontrado"
    return r

def consultar_pnombre_marca(marca):
    #funcion que retorna una tupla con todos los datos de los productos cuya
    #fk_id_marca sea la correspondiente al parametro de entrada
    conn = sqlite3.connect("producto.db")
    c = conn.cursor()
    query = """SELECT * FROM Producto WHERE fk_id_marca LIKE '%"""+marca+"""%'"""
    r = (c.execute(query).fetchall())
    if r == None:
        r="Elemento no encontrado"
    return r


def inicializa_BD():
    #para inicializar la base de datos con algunos datos
    agregar_marca("Nike", "marca de zapatillas", "Taiwan")
    agregar_marca("HP", "Hewlett-Packard, empresa de tecnologia", "EEUU")
    agregar_marca("Dell", "multinacional fabrica, vende y da soporte", "EEUU")
    agregar_marca("Puma", "fabricante de ropa y calzado deportivo", "Alemania")
    agregar_marca("Samsung", "industria electronica", "Corea del Sur")
    agregar_producto("001", "Hp Pavilion g4", "Notebook Hp Pavilion g4-1281la", "negro", "200990","2")
    agregar_producto("002","Samsung Galaxy Grand", "Celular marca Samsung", "negro", "200000","5")
    agregar_producto("003", "Samsung Galaxy S3","Celular", "negro", "150000", "5")
    agregar_producto("004", "Samsung Galaxy s4", "Celular", "blaco", "210000", "5")
    agregar_producto("005", "zapatillas", "zapatillas Nike", "rojas", "54990", "1")
    agregar_producto("006", "Hp Pavilion 15", "Notebook HP Pavilon 15", "gris", "459000", "2")
    agregar_producto("007", "Poleron", "Poleron Puma", "gris", "25990", "4")
    agregar_producto("008", "Dell ms", "Notebook Dell MS", "azul", "450990", "3")

def editar_producto(id_prod, cod, name, desc, color, prec, id_marca):
    #Funcion para editar los productos de la base de datos
    #recibe como parametros de entrada el id del producto que quiere editar
    #tambien recibe todos los parametros necesarios para editar los valores del producto
    exito = False
    conn = sqlite3.connect("producto.db")
    c = conn.cursor()
    valores = [cod, name, desc, color, prec, id_marca,id_prod]
    query = """ UPDATE Producto SET codigo = ?,
    nombre = ?,
    descripcion = ?,
    color = ?,
    precio = ?,
    fk_id_marca = ? WHERE codigo = ?"""
    try:
        c.execute(query, valores)
        conn.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    conn.close()
    return exito


def eliminar_producto(cod):
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


if __name__ == "__main__":
    db_name = 'producto.db'
    if not os.path.exists(db_name):
        crear_productoBD(db_name)
        inicializa_BD()

    conn = sqlite3.connect("producto.db")
    c = conn.cursor()

    for row in c.execute("SELECT * FROM Marca"):
        print row
    for row in c.execute("SELECT * FROM Producto"):
        print row
    #x = (c.execute("""SELECT precio FROM Producto WHERE codigo = "001" """)).fetchone()
    r=consulta_mnombre_nombre("Sam")
    print r
    f = consultar_pnombre_nombre("samsung")
    print f