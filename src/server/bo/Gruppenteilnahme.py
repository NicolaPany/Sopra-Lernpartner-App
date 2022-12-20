from server.bo import BusinessObject as bo


class Gruppenteilnahme (bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._gruppenteilnahme_id = 0
        """ID der Gruppenteilnahme"""
        self._status = None
        """Status der Teilnahme"""
        self._profil_id = 0
        """Profil ID einer Person"""
        self._lerngruppe_id = 0
        """ID der Lerngruppe"""

    def get_gruppenteilnahme_id(self):
        """Auslesen der Gruppenteilnahme-ID"""
        return self._gruppenteilnahme_id

    def set_gruppenteilnahme_id(self, value):
        """Setzen der Gruppenteilnahme-ID"""
        self._gruppenteilnahme_id = value

    def get_status(self):
        """Auslesen des Status"""
        return self._status

    def set_status(self, status):
        """Setzen des Status"""
        self._status = status

    def get_profil_id(self):
        """Auslesen des Profils"""
        return self._profil_id

    def set_profil_id(self, value):
        """Setzen eines Profils"""
        self._profil_id = value

    def get_lerngruppe_id(self):
        """Auslesen der Lerngruppe"""
        return self._lerngruppe_id

    def set_lerngruppe_id(self, value):
        """Setzen der Lerngruppe"""
        self._lerngruppe_id = value


    def from_dict(dictionary=dict()) -> object:
        """Umwandeln eines Python dict() in eine Gruppenteilnahme()."""
        obj = Gruppenteilnahme()
        obj.set_id(dictionary["id"])
        obj.set_profil_id(dictionary["profil_id"])
        obj.set_lerngruppe_id(dictionary["lerngruppe_id"])

        return obj