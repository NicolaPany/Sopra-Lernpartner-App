from server.bo.Lerndaten import Lerndaten
from server.db.Mapper import Mapper


class LerndatenMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result=[]
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Lerndaten")
        lerndaten_daten = cursor.fetchall()

        for (lerndaten_id, tageszeit, tage, frequenz, lernort, lernart, gruppengroesse_min, gruppengroesse_max, vorkenntnisse, extrovertiertheit, profil_id) in lerndaten_daten:
            lerndaten = Lerndaten()
            lerndaten.set_id(lerndaten_id)
            lerndaten.set_tageszeit(tageszeit)
            lerndaten.set_tage(tage)
            lerndaten.set_frequenz(frequenz)
            lerndaten.set_lernort(lernort)
            lerndaten.set_lernart(lernart)
            lerndaten.set_gruppengroesse_min(gruppengroesse_min)
            lerndaten.set_gruppengroesse_max(gruppengroesse_max)
            lerndaten.set_vorkenntnisse(vorkenntnisse)
            lerndaten.set_extrovertiertheit(extrovertiertheit)
            lerndaten.set_profil(profil_id)
            result.append(lerndaten)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result