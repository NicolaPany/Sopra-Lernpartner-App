from server.bo.Gruppenteilnahme import Gruppenteilnahme
from server.db.Mapper import Mapper

class GruppenteilnahmeMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result=[]
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Gruppenteilnahme")
        gruppenteilnahme_daten = cursor.fetchall()

        for (gruppenteilnahme_id, status, profil_id, lerngruppe_id) in gruppenteilnahme_daten:
            gruppenteilnahme = Gruppenteilnahme()
            gruppenteilnahme.set_id(gruppenteilnahme_id)
            gruppenteilnahme.set_status(status)
            gruppenteilnahme.set_profil_id(profil_id)
            gruppenteilnahme.set_lerngruppe_id(lerngruppe_id)
            result.append(gruppenteilnahme)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result