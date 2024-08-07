import pyodbc
import os
class Conn:

    __connection = None
    @staticmethod
    def get_connection():
        if Conn.__connection is None:
            Conn.__connection = Conn()
        return Conn.__connection

    def __init__(self):

        if Conn.__connection is None:
            self.connection = pyodbc.connect('DRIVER={MySQL ODBC 8.3 Unicode Driver};'
                                             'SERVER=127.0.0.1;'
                                             'PORT=3306;'
                                             'DATABASE=crime;'
                                             'USER=root;'
                                             'PASSWORD=dineshsql7;'
                                             'TRUSTED_CONNECTION=Yes;')
            Conn.__connection = self
        else:
            raise Exception("Object is already initialized")
