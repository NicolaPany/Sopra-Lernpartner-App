from abc import ABC
import datetime


class BusinessObject(ABC):

    def __init__(self):
        self._id = 0
        self._erstellungszeit = datetime.datetime.now()
        self._name = None

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_erstellungszeit(self):
        return self._erstellungszeit

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
