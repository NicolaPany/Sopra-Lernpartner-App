from server.bo.Profil import Profil
from server.db.Mapper import Mapper

class ProfilMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result=[]
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Profil")
        profil_daten = cursor.fetchall()

        for (profil_id, hochschule, studiengang, semester, lernfaecher, selbsteinschaetzung, person_id) in profil_daten:
            profil = Profil()
            profil.set_id(profil_id)
            profil.set_hochschule(hochschule)
            profil.set_studiengang(studiengang)
            profil.set_semester(semester)
            profil.set_lernfaecher(lernfaecher)
            profil.set_selbsteinschaetzung(selbsteinschaetzung)
            profil.set_person(person_id)
            result.append(profil)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result