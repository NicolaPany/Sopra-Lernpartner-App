from server.bo.NamedBusinessObject import NamedBusinessObject


class Lerngruppe(NamedBusinessObject):

    def __init__(self):
        super().__init__()
        self.gruppenname = None
        """Name der Lerngruppe"""
        self._teilnehmer = None
        """Teilnehmer der Lerngruppe"""

    def get_gruppenname(self):
        """Auslesen des Gruppennamens"""
        return self._gruppenname

    def set_gruppenname(self, gruppenname):
        """Setzen des Gruppennamens"""
        self._gruppenname = gruppenname

    def get_teilnehmer(self):
        """Auslesen der Gruppenteilnehmer"""
        return self._teilnehmer

    def set_teilnehmer(self, teilnehmer):
        """Setzen der Gruppenteilnehmer"""
        self._teilnehmer = teilnehmer

