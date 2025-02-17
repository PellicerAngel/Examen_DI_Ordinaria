import os
import sqlite3
import pytest
from main import UserApp
from PySide6.QtWidgets import QApplication
import pytest

def test_afegir(qtbot):
    """Inicializa la aplicación, realiza la prueba y limpia la base de datos."""
    test_db = "test_users.db"
    if os.path.exists(test_db):
        os.remove(test_db)
    
    conn = sqlite3.connect(test_db)
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )''')
    conn.close()
    
    app = UserApp()  # No pasamos db_path
    app.db.conn = sqlite3.connect(test_db)  # Sobrescribimos la conexión
    app.db.cursor = app.db.conn.cursor()
    qtbot.addWidget(app)
    
    # Prueba de añadir usuario
    app.db.add_user("UsuarioPrueba", "contraseña123", "Usuari")
    app.load_users()
    assert app.table.rowCount() == 1
    
    app.close()
    os.remove(test_db)

def test_rm(qtbot):
    
    test_db = "test_users.db"
    # if os.path.exists(test_db):
    #     os.remove(test_db)
    
    conn = sqlite3.connect(test_db)
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )''')
    conn.close()
    
    app = UserApp()  # No pasamos db_path
    app.db.conn = sqlite3.connect(test_db)  # Sobrescribimos la conexión
    app.db.cursor = app.db.conn.cursor()
    qtbot.addWidget(app)
    
    app.db.add_user("UsuarioPrueba", "contraseña123", "Usuari")
    app.load_users()
    assert app.table.rowCount() == 1

    # Prueba de añadir usuario
    app.db.delete_user("1")
    app.load_users()
    assert app.table.rowCount() == 0
    
    app.close()
    os.remove(test_db)

def test_modificar(qtbot):
    """Inicializa la aplicación, realiza la prueba y limpia la base de datos."""
    test_db = "test_users.db"
    if os.path.exists(test_db):
        os.remove(test_db)

    conn = sqlite3.connect(test_db)
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )''')
    conn.close()

    app = UserApp()  # No pasamos db_path
    app.db.conn = sqlite3.connect(test_db)  # Sobrescribimos la conexión
    app.db.cursor = app.db.conn.cursor()
    qtbot.addWidget(app)
    #
    app.db.add_user("UsuarioPrueba", "contraseña123", "Usuari")
    app.load_users()
    assert app.table.rowCount() == 1
    app.db.update_user(1,"UsuarioPrueba2", "contraseña1234", "Usuari")
    app.load_users()
    assert app.table.item(0, 0).text() == "UsuarioPrueba2"
    assert app.table.item(0, 1).text() == "contraseña1234"
    assert app.table.item(0, 2).text() == "Usuari"

    app.close()
    os.remove(test_db)