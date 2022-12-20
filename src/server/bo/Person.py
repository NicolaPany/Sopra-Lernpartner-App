from server.bo.NamedBusinessObject import NamedBusinessObject


class Person(NamedBusinessObject):

    def __init__(self):
        super().__init__()
        self._vorname = None
        """Vorname einer Person"""
        self._lebensjahre = 0
        """Alter einer Person"""
        self._geschlecht = None
        """Geschlecht der Person"""
        self._lerngruppe = False
        """Info, ob die Person interessiert ist an einer Lerngruppe"""
        self._google_user_id = None
        """Google User ID der Person"""
        self._email = None
        """E-Mail einer Person"""
        self._profil_id = None
        """Profil ID einer Person"""

    def get_vorname(self):
        """Auslesen des Vornamens"""
        return self._vorname

    def set_vorname(self, vorname):
        """Setzen des Vornamens"""
        self._vorname = vorname

    def get_lebensjahre(self):
        """Auslesen des Alters"""
        return self._lebensjahre

    def set_lebensjahre(self, lebensjahre):
        """Setzen des Alters"""
        self._alter = lebensjahre

    def get_geschlecht(self):
        """Auslesen des Geschlechts"""
        return self._geschlecht

    def set_geschlecht(self, geschlecht):
        """Setzen des Geschlechts"""
        self._geschlecht = geschlecht

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

    def get_profil_id(self):
        """Auslesen des Profils"""
        return self._profil_id

    def set_profil_id(self, value):
        """Setzen eines Profils"""
        self._profil_id = value

    def from_dict(dictionary=dict()) -> object:
        """Umwandeln eines Python dict() in eine Person()."""
        obj = Person()
        obj.set_id(dictionary["id"])
        obj.set_name(dictionary["nachname"])
        obj.set_vorname(dictionary["vorname"])
        obj.set_lebensjahre(dictionary["lebensjahre"])
        obj.set_geschlecht(dictionary["geschlecht"])
        obj.set_lerngruppe(dictionary["lerngruppe"])
        obj.set_google_user_id(dictionary["google_user_id"])
        obj.set_email(dictionary["email"])
        obj.set_profil_id(dictionary["profil_id"])

        return obj