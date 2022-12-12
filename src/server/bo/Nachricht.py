from server.bo import BusinessObject as bo


class Nachricht(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._nachricht_id = 0
        """Die ID der Nachricht"""
        self._nachricht_text = ""
        """Der Text, den eine Nachricht beinhaltet"""
        self._person_id = 0
        """Die ID der Person, die die Nachricht sendet"""
        self._konversation_id = 0
        """Die ID der zugehörigen Konversation"""

    def get_nachricht_id(self):
        """Auslesen der Nachrichten-ID"""
        return self._nachricht_id

    def set_nachricht_id(self, value):
        """Setzen der Nachrichten-ID"""
        self._nachricht_id = value

    def get_nachricht_text(self):
        """Auslesen des Texts einer Nachricht"""
        return self._nachricht_text

    def set_nachricht_text(self, text):
        """Setzen des Texts einer Nachricht"""
        self._nachricht_text = text

    def get_person_id(self):
        """Auslesen des Senders der Nachricht"""
        return self._person_id

    def set_person_id(self, person_id):
        """Setzen des Senders der Nachricht"""
        self._person_id = person_id

    def get_konversation_id(self):
        """Auslesen der zugehörigen Konversation der Nachricht"""
        return self._konversation_id

    def set_konversation_id(self, konversation_id):
        """Setzen der zugehörigen Konversation der Nachricht"""
        self._konversation_id = konversation_id