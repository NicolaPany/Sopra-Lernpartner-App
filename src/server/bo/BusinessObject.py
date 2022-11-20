from abc import ABC
import datetime


class BusinessObject(ABC):

    def __init__(self):
        self._id = 0
        self._erstellungszeit = datetime.datetime.now()

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_erstellungszeit(self):
        return self._erstellungszeit
