from server.bo.NamedBusinessObject import NamedBusinessObject


class Person(NamedBusinessObject):

    def __init__(self):
        super().__init__()
        self._vorname = None
        """Vorname einer Person"""
        self._alter = 0
        """Alter einer Person"""
        self._geschlecht = None
        """Geschlecht der Person"""
        self._semester = 0
        """Semester einer Person"""
        self._studiengang = None
        """Studiengang einer Person"""
        self._lerngruppe = False
        """Info, ob die Person interessiert ist an einer Lerngruppe"""
        self._google_user_id = None
        """Google User ID der Person"""
        self._email = None
        """E-Mail einer Person"""
        self._profil = None
        """Profil ID einer Person"""

    def get_vorname(self):
        """Auslesen des Vornamens"""
        return self._vorname

    def set_vorname(self, vorname):
        """Setzen des Vornamens"""
        self._vorname = vorname

    def get_alter(self):
        """Auslesen des Alters"""
        return self._alter

    def set_alter(self, alter):
        """Setzen des Alters"""
        self._alter = alter

    def get_geschlecht(self):
        """Auslesen des Geschlechts"""
        return self._geschlecht

    def set_geschlecht(self, geschlecht):
        """Setzen des Geschlechts"""
        self._geschlecht = geschlecht

    def get_semester(self):
        """Auslesen des Semesters"""
        return self._semester

    def set_semester(self, value):
        """Setzen des Semesters"""
        self._semester = value

    def get_studiengang(self):
        """Auslesen des Studiengangs"""
        return self._studiengang

    def set_studiengang(self, value):
        """Setzen des Studiengangs"""
        self._studiengang = value

    def get_lerngruppe(self):
        """Auslesen, ob Interesse an einer Lerngruppe besteht"""
        return self._lerngruppe

    def set_lerngruppe(self, value):
        """Setzen, ob Interesse an einer Lerngruppe besteht"""
        self._lerngruppe = value

    def get_google_user_id(self):
        """ Auslesen der Google User ID"""
        return self._google_user_id

    def set_google_user_id(self, value):
        """ Setzen der Google User ID"""
        self._google_user_id = value

    def get_email(self):
        """ Auslesen der E-Mail-Adresse"""
        return self._email

    def set_email(self, value):
        """ Setzen der E-Mail-Adresse"""
        self._email = value

    def get_profil(self):
        """Auslesen des Profils"""
        return self._profil

    def set_profil(self, value):
        """Setzen eines Profils"""
        self._profil = value
