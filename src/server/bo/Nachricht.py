from server.bo import BusinessObject as bo


class Nachricht(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._nachricht_id = 0
        """Die ID der Nachricht"""
        self._nachricht_text = ""
        """Der Text, den eine Nachricht beinhaltet"""

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

    def from_dict(dictionary=dict()) -> object:
        """Umwandeln eines Python dict() in eine Nachricht()."""
        obj = Nachricht()
        obj.set_id(dictionary["id"])
        obj.set_nachricht_text(dictionary["nachricht_text"])

        return obj