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
            lerngruppe.set_gruppenname(gruppenname)
            lerngruppe.set_teilnehmer(teilnehmer)
            result.append(lerngruppe)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result