from server.bo.Chatteilnahme import Chatteilnahme
from server.db.Mapper import Mapper

class ChatteilnahmeMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result=[]
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Chatteilnahme")
        chatteilnahme_daten = cursor.fetchall()

        for (chatteilnahme_id, profil_id, konversation_id) in chatteilnahme_daten:
            chatteilnahme = Chatteilnahme()
            chatteilnahme.set_id(chatteilnahme_id)
            chatteilnahme.set_profil_id(profil_id)
            chatteilnahme.set_konversation_id(konversation_id)
            result.append(chatteilnahme)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result