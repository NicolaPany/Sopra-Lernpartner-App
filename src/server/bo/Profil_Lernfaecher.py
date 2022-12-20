from server.bo import BusinessObject as bo


class Profil_Lernfaecher (bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._lerngruppe_id = 0
        """ID der Lerngruppe"""
        self._profil_id = 0
        """Profil ID einer Person"""

    def get_lerngruppe_id(self):
        """Auslesen der Lerngruppe"""
        return self._lerngruppe_id

    def set_lerngruppe_id(self, value):
        """Setzen der Lerngruppe"""
        self._lerngruppe_id = value

    def get_profil_id(self):
        """Auslesen des Profils"""
        return self._profil_id

    def set_profil_id(self, value):
        """Setzen eines Profils"""
        self._profil_id = value



    def from_dict(dictionary=dict()) -> object:
        """Umwandeln eines Python dict() in Profil_Lernfaecher()."""
        obj = Profil_Lernfaecher()
        obj.set_lerngruppe_id(dictionary["lerngruppe_id"])
        obj.set_profil_id(dictionary["profil_id"])

        return obj