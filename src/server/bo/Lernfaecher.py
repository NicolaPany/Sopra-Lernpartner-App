from server.bo.BusinessObject import BusinessObject


class Lernfaecher(BusinessObject):

    def __init__(self):
        super().__init__()
        self._lernfach_id = 0
        """ID des Lernfachs"""
        self._lernfachname = None
        """Bezeichnung des Lernfachs"""

    def get_lernfach_id(self):
        """Auslesen der Lernfach-ID"""
        return self._lernfach_id

    def set_lernfach_id(self, value):
        """Setzen der Lernfach-ID"""
        self._lernfach_id = value

    def get_lernfachname(self):
        """Auslesen des Namens des Lernfachs"""
        return self._lernfachname

    def set_lernfachname(self, lernfachname):
        """Setzen des Namens des Lernfachs"""
        self._lernfachname = lernfachname

    def from_dict(dictionary=dict()) -> object:
        """Umwandeln eines Python dict() in Lernfaecher()."""
        obj = Lernfaecher()
        obj.set_id(dictionary["id"])
        obj.set_lernfachname(dictionary["lernfachname"])

        return obj