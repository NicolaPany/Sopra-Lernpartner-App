import mysql.connector as connector
from contextlib import AbstractContextManager
from abc import ABC


class Mapper(AbstractContextManager, ABC):

    def __init__(self):
        self._cnx = None

    def __enter__(self):
        """Wird ausgeführt, sobald die Klasse mit dem "with" Befehl aufgerufen wird"""


        """Es soll eine Verbindung zur Datenbank erstellt werden"""
        self._cnx = connector.connect(user='root', password='sopragruppe8-ws23',
                                          host='127.0.0.1',
                                          database='Sopra-LernApp', auth_plugin='mysql_native_password')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Wird ausgeführt, sobald die Befehle, die mit "with" ausgeführt werden, beendet werden"""

        """ Wir trennen die Datenbankverbindung"""
        self._cnx.close()