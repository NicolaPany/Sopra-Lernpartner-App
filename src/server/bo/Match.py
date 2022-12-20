from server.bo import BusinessObject as bo


class Match (bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._match_id = 0
        """ID des Matches"""
        self._suchende_person_id = 0
        """ID der suchenden Person"""
        self._quote = 0
        """Übereinstimmungsquote"""
        self._lernfach = None
        """Lernfach nach dem gesucht wird"""
        self._match_profil_id = 0
        """ID der gematchten Person"""

    def get_match_id(self):
        """Auslesen der Match-ID"""
        return self._match_id

    def set_match_id(self, value):
        """Setzen der Match-ID"""
        self._match_id = value

    def get_suchende_person_id(self):
        """Auslesen der Person-ID"""
        return self._suchende_person_id

    def set_suchende_person_id(self, value):
        """Setzen der Person-ID"""
        self._suchende_person_id = value

    def get_quote(self):
        """Auslesen der Matchingquote"""
        return self._quote

    def set_quote(self, value):
        """Setzen der Matchingquote"""
        self._match_quote = value

    def get_lernfach(self):
        """Auslesen des Lernfaches"""
        return self._lernfach

    def set_lernfach(self, lernfach):
        """"Setzen des Lernfaches"""
        self._lernfach = lernfach

    def get_match_profil_id(self):
        """Auslesen der gematchten ID"""
        return self._match_profil_id

    def set_match_profil_id(self, value):
        """Setzen der gematchten ID"""
        self._match_profil_id = value


    def from_dict(dictionary=dict()) -> object:
        """Umwandeln eines Python dict() in ein Match()."""
        obj = Match()
        obj.set_id(dictionary["id"])
        obj.set_suchende_person_id(dictionary["suchende_person_id"])
        obj.set_quote(dictionary["quote"])
        obj.set_lernfach(dictionary["lernfach"])
        obj.set_match_profil_id(dictionary["match_profil_id"])

        return obj