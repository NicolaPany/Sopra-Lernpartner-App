from server.bo import BusinessObject as bo


class Chatteilnahme (bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._chatteilnahme_id = 0
        """ID der Chatteilnahme"""
        self._profil_id = 0
        """Profil ID einer Person"""
        self._konversation_id = 0
        """ID der Konversation"""

    def get_chatteilnahme_id(self):
        """Auslesen der Chatteilnahme-ID"""
        return self._chatteilnahme_id

    def set_chatteilnahme_id(self, value):
        """Setzen der Chatteilnahme-ID"""
        self._chatteilnahme_id = value

    def get_profil_id(self):
        """Auslesen des Profils"""
        return self._profil_id

    def set_profil_id(self, value):
        """Setzen eines Profils"""
        self._profil_id = value

    def get_konversation_id(self):
        """Auslesen der Konversation"""
        return self._konversation_id

    def set_konversation_id(self, value):
        """Setzen der Konversation"""
        self._konversation_id = value


    def from_dict(dictionary=dict()) -> object:
        """Umwandeln eines Python dict() in eine Chatteilnahme()."""
        obj = Chatteilnahme()
        obj.set_id(dictionary["id"])
        obj.set_profil_id(dictionary["profil_id"])
        obj.set_konversation_id(dictionary["konversation_id"])

        return obj