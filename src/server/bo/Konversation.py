from server.bo import BusinessObject as bo


class Konversation (bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._konversation_id = 0
        """ID der Konversation"""
        self._anfragestatus = False
        """Der Anfragestatus der Konversation, sprich, haben beide Teilnehmer die Chatanfrage bestätigt"""

    def get_konversation_id(self):
        """Auslesen der Konversations-ID"""
        return self._konversation_id

    def set_konversation_id(self, value):
        """Setzen der Konversations-ID"""
        self._konversation_id = value


    def get_anfragestatus(self):
        """Auslesen des Anfragestatus"""
        return self._anfragestatus

    def set_anfragestatus(self, anfragestatus):
        """"Setzen des Anfragestatus"""
        self._anfragestatus = anfragestatus

    def get_nachricht_id(self):
        """Auslesen der Nachrichten-ID"""
        return self._nachricht_id

    def set_nachricht_id(self, value):
        """Setzen der Nachrichten-ID"""
        self._nachricht_id = value


    def from_dict(dictionary=dict()) -> object:
        """Umwandeln eines Python dict() in eine Konversation()."""
        obj = Konversation()
        obj.set_id(dictionary["id"])
        obj.set_anfragestatus(dictionary["anfragestatus"])
        obj.set_nachricht_id(dictionary["nachricht_id"])

        return obj