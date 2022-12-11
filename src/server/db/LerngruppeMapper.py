from server.bo.Lerngruppe import Lerngruppe
from server.db.Mapper import Mapper

class LerngruppeMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result=[]
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Lerngruppe")
        lerngruppe_daten = cursor.fetchall()

        for (lerngruppe_id, gruppenname, teilnehmer) in lerngruppe_daten:
            lerngruppe = Lerngruppe()
            lerngruppe.set_id(lerngruppe_id)
            lerngruppe.set_gruppenname(gruppenname)
            lerngruppe.set_teilnehmer(teilnehmer)
            result.append(lerngruppe)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result

    def find_by_id(self, id):
        """ Wir suchen eine Lerngruppe mit der jeweiligen ID """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM Lerngruppe WHERE lerngruppe_id={0}".format(id)
        cursor.execute(command)
        lerngruppe_daten = cursor.fetchall()

        try:
            (lerngruppe_id, gruppenname, teilnehmer) = lerngruppe_daten[0]
            lerngruppe = Lerngruppe()
            lerngruppe.set_id(lerngruppe_id)
            lerngruppe.set_gruppenname(gruppenname)
            lerngruppe.set_teilnehmer(teilnehmer)
            result = lerngruppe
        except IndexError:
            """ Tritt auf, wenn es beim SELECT-Aufruf kein Ergebnis liefert, sondern lerngruppe_daten leer ist """
            result = None

        self._cnx.commit()
        cursor.close()
        print(result)
        return result