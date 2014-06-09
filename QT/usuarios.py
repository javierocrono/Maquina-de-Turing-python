#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sqlite3

def crea_bd_usuario():
    #metodo que crea la base de datos usuarios para trabajar con el login
    #a su vez tambien crea un super usuario para poder hacer pruebas
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()
    query = """CREATE TABLE Usuarios(
        cod integer primary key AUTOINCREMENT,
        user text,
        pass text)"""
    c.execute(query)
    query = """INSERT INTO Usuarios(user, pass) VALUES ("superuser", "1234")"""
    c.execute(query)
    conn.commit()


if __name__ == "__main__":
    db_name = 'usuarios.db'
    if not os.path.exists(db_name):
        crea_bd_usuario()