from server.bo.BusinessObject import BusinessObject


class Lernfach(BusinessObject):

    def __init__(self):
        super().__init__()
        self._lernfachname = None
        """Bezeichnung des Lernfachs"""

    def get_lernfachname(self):
        """Auslesen des Namens des Lernfachs"""
        return self._lernfachname

    def set_lernfachname(self, lernfachname):
        """Setzen des Namens des Lernfachs"""
        self._lernfachname = lernfachname
