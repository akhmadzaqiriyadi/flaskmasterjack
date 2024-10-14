from flask_mysqldb import MySQL
from flask import Flask

def init_db(app: Flask):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'randusari'
    app.config['MYSQL_DB'] = 'flask_db'

    # Inisialisasi MySQL
    mysql = MySQL(app)
    return mysql
