#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def conectar():
    con = sqlite3.connect('usuarios.db')
    con.row_factory = sqlite3.Row
    return con


def existe(nombre):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM usuarios WHERE user='" + nombre + "'"
    resultado = c.execute(query)
    usuarios = resultado.fetchall()
    con.close()
    #print usuarios
    return usuarios


def crear(nombre, contrasenia):
    con = conectar()
    c = con.cursor()
    query = "INSERT INTO Usuarios(user, pass) VALUES ('"+ nombre +"', '" + contrasenia + "')"
    c.execute(query)
    con.commit()
    con.close()
    print "agregado"
