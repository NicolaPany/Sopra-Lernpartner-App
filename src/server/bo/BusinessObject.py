from abc import ABC
import datetime


class BusinessObject(ABC):

    def __init__(self):
        self._id = 0
        self._erstellungszeit = datetime.datetime.now()

    def get_id(self):
        """Auslesen der ID"""
        return self._id

    def set_id(self, value):
        """Setzen der ID"""
        self._id = value

    def get_erstellungszeit(self):
        """Auslesen der Erstellungszeit"""
        return self._erstellungszeit
