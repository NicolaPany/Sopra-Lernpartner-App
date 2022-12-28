from server.bo.Profil_Lernfaecher import Profil_Lernfaecher
from server.db.Mapper import Mapper

class Profil_LernfaecherMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result=[]
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Profil_Lernfaecher")
        profil_lernfaecher_daten = cursor.fetchall()

        for (profil_id, lernfach_id) in profil_lernfaecher_daten:
            profil_lernfaecher = Profil_Lernfaecher()
            profil_lernfaecher.set_profil_id(profil_id)
            profil_lernfaecher.set_lernfach_id(lernfach_id)
            result.append(profil_lernfaecher)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result