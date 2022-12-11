from server.bo.NamedBusinessObject import NamedBusinessObject


class Lerngruppe(NamedBusinessObject):

    def __init__(self):
        super().__init__()
        self.lerngruppe_id = 0
        """ID der Lerngruppe"""
        self.gruppenname = None
        """Name der Lerngruppe"""
        self._teilnehmer = None
        """Teilnehmer der Lerngruppe"""


    def get_lerngruppe_id(self):
        """Auslesen der Gruppen-ID"""
        return self._lerngruppe_id

    def set_lerngruppe_id(self, value):
        """Setzen der Gruppen-ID"""
        self._lerngruppe_id = value

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

