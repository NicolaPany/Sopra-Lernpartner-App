from server.bo.BusinessObject import BusinessObject


class Profil(BusinessObject):

    def __init__(self):
        super().__init__()
        self._hochschule = None
        """Hochschule, an der eine Person studiert"""
        self._studiengang = None
        """Studiengang einer Person"""
        self._semester = 0
        """Semester einer Person"""
        self._lernfaecher = []
        """Liste aller Lernfaecher, die zum Profil gehören"""
        self._selbsteinschaetzung= 0
        """Selbsteinschätzung einer Person von 1-5"""
        self._person = None
        """Person ID des Profils"""

    def get_hochschule(self):
        """Auslesen der Hochschule"""
        return self._hochschule
    def set_hochschule(self, hochschule):
        """Setzen der Hochschule"""
        self._hochschule = hochschule


    def get_studiengang(self):
        """Auslesen des Studiengangs"""
        return self._studiengang
    def set_studiengang(self, studiengang):
        """Setzen des Studiengangs"""
        self._studiengang = studiengang


    def get_semester(self):
        """Auslesen des Semesters"""
        return self._semester
    def set_semester(self, value):
        """Setzen des Semesters"""
        self._semester = value


    def get_lernfaecher(self):
        """Auslesen der Lernfächer"""
        return self._lernfaecher

    def set_lernfaecher(self, lernfaecher):
        """Setzen der Lernfächer"""
        self._lernfaecher = lernfaecher


    def get_selbsteinschaetzung(self):
        """Auslesen der Selbsteinschätzung"""
        return self._selbsteinschaetzung

    def set_selbsteinschaetzung(self, value):
        """Setzen der Selbsteinschätzung"""
        self._selbsteinschaetzung = value


    def get_person(self):
        """Auslesen einer Person"""
        return self._person

    def set_person(self, value):
        """Setzen einer Person"""
        self._person = value