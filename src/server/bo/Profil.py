from server.bo.BusinessObject import BusinessObject


class Profil(BusinessObject):

    def __init__(self):
        super().__init__()
        self._gruppe = False
        """Info, ob Profil zu einer Gruppe gehört"""
        self._lernfaecher = []
        """Liste aller Lernfaecher, die zum Profil gehören"""
        self._lernvorlieben_id = None
        """Lernvorlieben ID des Profils"""

    def get_gruppe(self):
        """Auslesen der Gruppe"""
        return self._gruppe

    def set_gruppe(self, gruppe_neu):
        """Setzen der Gruppe"""
        self._gruppe = gruppe_neu

    def get_lernfaecher(self):
        """Auslesen der Lernfächer"""
        return self._lernfaecher

    def set_lernfaecher(self, lernfach_neu):
        """Setzen der Lernfächer"""
        self._lernfaecher = lernfach_neu

    def get_lernvorlieben_id(self):
        """Auslesen der Lernfächer"""
        return self._lernvorlieben_id

    def set_lernvorlieben_id(self, lernvorlieben_id):
        """Setzen der Lernfächer"""
        self._lernvorlieben_id = lernvorlieben_id