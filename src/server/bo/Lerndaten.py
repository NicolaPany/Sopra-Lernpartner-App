from server.bo.BusinessObject import BusinessObject


class Lerndaten(BusinessObject):

    def __init__(self):
        super().__init__()
        self._tageszeit = None
        """Präferierte Tageszeit, zu der gelernt wird"""
        self._tage = None
        """Präferierte Tage, an denen gelernt wird"""
        self._frequenz = 0
        """Frequenz der Lerntage"""
        self._lernort = None
        """Präferierter Ort, an dem gelernt wird"""
        self._lernart = None
        """Auf welche Art am liebsten gelernt wird (online/offline)"""
        self._gruppengroesse_min = 0
        """Mindestanzahl der gewünschten Gruppenmitglieder"""
        self._gruppengroesse_max = 0
        """Maximale Anzahl der gewünschten Gruppenmitglieder"""
        self._vorkenntnisse = None
        """Eigene Beurteilung der Vorkenntnisse (sehr gut, gut, mittel, schlecht, sehr schlecht)"""
        self._extrovertiertheit = None
        """Eigene Beurteilung der Extrovertiertheit (sehr, mittel, schwach)"""
        self._profil_id = None
        """Profil ID einer Person"""

    def get_tageszeit(self):
        """Auslesen der Tageszeit"""
        return self._tageszeit

    def set_tageszeit(self, tageszeit):
        """Setzen der Tageszeit"""
        self._tageszeit = tageszeit

    def get_tage(self):
        """Auslesen der Tage"""
        return self._tage

    def set_tage(self, tage):
        """Setzen der Tage"""
        self._tage = tage

    def get_frequenz(self):
        """Auslesen der Frequenz"""
        return self._frequenz

    def set_frequenz(self, value):
        """Setzen der Frequenz"""
        self._frequenz = value

    def get_lernort(self):
        """Auslesen des Lernorts"""
        return self._lernort

    def set_lernort(self, lernort):
        """Setzen des Lernorts"""
        self._lernort = lernort

    def get_lernart(self):
        """Auslesen der Lernart"""
        return self._lernart

    def set_lernart(self, lernart):
        """Setzen der Lernart"""
        self._lernart = lernart

    def get_gruppengroesse_min(self):
        """Auslesen der mindesten Gruppengröße"""
        return self._gruppengroesse_min

    def set_gruppengroesse_min(self, value):
        """Setzen der minimalen Gruppengröße"""
        self._gruppengroesse_min = value

    def get_gruppengroesse_max(self):
        """Auslesen der maximalen Gruppengröße"""
        return self._gruppengroesse_max

    def set_gruppengroesse_max(self, value):
        """Setzen der maximalen Gruppengröße"""
        self._gruppengroesse_max = value

    def get_vorkenntnisse(self):
        """Auslesen der Vorkenntnisse"""
        return self._vorkenntnisse

    def set_vorkenntnisse(self, vorkenntnisse):
        """Setzen der Vorkenntnisse"""
        self._vorkenntnisse = vorkenntnisse

    def get_extrovertiertheit(self):
        """Auslesen der Extrovertiertheit"""
        return self._extrovertiertheit

    def set_extrovertiertheit(self, extrovertiertheit):
        """Setzen der Extrovertiertheit"""
        self._extrovertiertheit = extrovertiertheit

    def get_profil_id(self):
        """Auslesen des Profils"""
        return self._profil_id

    def set_profil_id(self, profil_id):
        """Setzen des Profils"""
        self._profil_id = profil_id

    def from_dict(dictionary=dict()) -> object:
        """Umwandeln eines Python dict() in Lerndaten()."""
        obj = Lerndaten()
        obj.set_id(dictionary["id"])
        obj.set_tageszeit(dictionary["tageszeit"])
        obj.set_tage(dictionary["tage"])
        obj.set_frequenz(dictionary["frequenz"])
        obj.set_lernort(dictionary["lernort"])
        obj.set_lernart(dictionary["lernart"])
        obj.set_gruppengroesse_min(dictionary["gruppengroesse_min"])
        obj.set_gruppengroesse_max(dictionary["gruppengroesse_max"])
        obj.set_vorkenntnisse(dictionary["vorkenntnisse"])
        obj.set_extrovertiertheit(dictionary["extrovertiertheit"])
        obj.set_profil_id(dictionary["profil_id"])
        return obj
