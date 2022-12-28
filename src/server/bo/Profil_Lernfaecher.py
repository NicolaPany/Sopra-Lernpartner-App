from server.bo import BusinessObject as bo


class Profil_Lernfaecher (bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._profil_id = 0
        """Profil ID einer Person"""
        self._lernfach_id = 0
        """ID des Lernfaches"""

    def get_profil_id(self):
        """Auslesen des Profils"""
        return self._profil_id

    def set_profil_id(self, value):
        """Setzen eines Profils"""
        self._profil_id = value

    def get_lernfach_id(self):
        """Auslesen des Lernfaches"""
        return self._lernfach_id

    def set_lernfach_id(self, value):
        """Setzen des Lernfaches"""
        self._lernfach_id = value

    def from_dict(dictionary=dict()) -> object:
        """Umwandeln eines Python dict() in Profil_Lernfaecher()."""
        obj = Profil_Lernfaecher()
        obj.set_profil_id(dictionary["profil_id"])
        obj.set_lernfach_id(dictionary["lerngruppe_id"])

        return obj