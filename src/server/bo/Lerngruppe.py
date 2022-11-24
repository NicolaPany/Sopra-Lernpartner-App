from server.bo.NamedBusinessObject import NamedBusinessObject


class Lerngruppe(NamedBusinessObject):

    def __init__(self):
        super().__init__()
        self._gruppenprofil = None
        """Profil (ID) der Lerngruppe"""

    def get_gruppenprofil(self):
        """Auslesen eines Gruppenprofils"""
        return self._gruppenprofil

    def set_gruppenprofil(self, gruppenprofil):
        """Setzen eines Gruppenprofils"""
        self._gruppenprofil = gruppenprofil
