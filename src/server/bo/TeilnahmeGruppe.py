from server.bo import BusinessObject as bo


class TeilnahmeGruppe(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._teilnehmer = None
        """Teilnehmer der Gruppe"""
        self._lerngruppe = 0
        """Lerngruppe der Teilnehmer"""

    def get_teilnehmer(self):
        """Auslesen des Teilnehmers"""
        return self._teilnehmer

    def set_teilnehmer(self, teilnehmer):
        """setzten des Teilnehmers"""
        self._teilnehmer = teilnehmer

    def get_lerngruppe(self):
        """Auslesen der Lerngruppe"""
        return self._lerngruppe

    def set_lerngruppe(self, lerngruppe):
        """setzten der neuen Lerngruppe"""
        self._lerngruppe = lerngruppe