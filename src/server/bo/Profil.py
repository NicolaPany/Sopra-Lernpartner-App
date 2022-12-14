from server.bo.NamedBusinessObject import NamedBusinessObject


class Profil(NamedBusinessObject):

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


    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Profil()."""
        obj = Profil()
        obj.set_id(dictionary["id"])
        obj.set_hochschule(dictionary["hochschule"])
        obj.set_studiengang(dictionary["studiengang"])
        obj.set_semester(dictionary["semester"])
        obj.set_lernfaecher(dictionary["lernfaecher"])
        obj.set_selbsteinschaetzung(dictionary["selbsteinschaetzung"])

        return obj