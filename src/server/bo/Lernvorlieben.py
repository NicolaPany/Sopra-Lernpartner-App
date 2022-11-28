from server.bo.BusinessObject import BusinessObject


class Lernvorlieben(BusinessObject):

    def __init__(self):
        super().__init__()
        self._offenheit_id = None
        """ID der Offenheit (Extrovertiert, Introvertiert,..."""
        self._offenheit_bez = None
        """Bezeichnung der Offenheit (Extrovertiert, Introvertiert,..."""
        self._lernort_id = None
        """ID des Lernorts (Online, Offline)"""
        self._lernort_bez = None
        """Bezeichnung des Lernorts (Online, Offline)"""
        self._frequenz_id = None
        """ID der Frequenz der Treffen"""
        self._frequenz_bez = None
        """Bezeichnung der Frequenz der Treffen"""
        self._vorkenntnisse_id = None
        """ID der Vortkenntnisse"""
        self._vorkenntnisse_bez = None
        """Bezeichnung der Vorkenntnisse"""
        self._tage_id = None
        """ID der Tage an denen man lernen will"""
        self._tage_bez = None
        """Bezeichnung der Tage an denen man lernen will"""

    def get_offenheit_id(self):
        return int(self._offenheit_id)

    def set_offenheit_id(self, value):
        self._offenheit_id = value

    def get_offenheit_bez(self):
        return self._offenheit_bez

    def set_offenheit_bez(self, value):
        self._offenheit_bez = value

    def get_lernort_id(self):
        return int(self._lernort_id)

    def set_lernort_id(self, value):
        self._lernort_id = value

    def get_lernort_bez(self):
        return self._lernort_bez

    def set_lernort_bez(self, value):
        self._lernort_bez = value

    def get_frequenz_id(self):
        return int(self._frequenz_id)

    def set_frequenz_id(self, value):
        self._frequenz_id = value

    def get_frequenz_bez(self):
        return self._frequenz_bez

    def set_frequenz_bez(self, value):
        self._frequenz_bez = value

    def get_vorkenntnisse_id(self):
        return int(self._vorkenntnisse_id)

    def set_vorkenntnisse_id(self, value):
        self._vorkenntnisse_id = value

    def get_vorkenntnisse_bez(self):
        return self._vorkenntnisse_bez

    def set_vorkenntnisse_bez(self, value):
        self._vorkenntnisse_bez = value

    def get_tage_id(self):
        return int(self._tage_id)

    def set_tage_id(self, value):
        self._tage_id = value

    def get_tage_bez(self):
        return self._tage_bez

    def set_tage_bez(self, value):
        self._tage_bez = value

