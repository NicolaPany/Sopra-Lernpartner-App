from server.bo.Lernfaecher import Lernfaecher
from server.db.Mapper import Mapper

class LernfaecherMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result=[]
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Lernfaecher")
        lernfaecher_daten = cursor.fetchall()

        for (lernfach_id, lernfachname) in lernfaecher_daten:
            lernfaecher = Lernfaecher()
            lernfaecher.set_id(lernfach_id)
            lernfaecher.set_lernfachname(lernfachname)
            result.append(lernfaecher)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result