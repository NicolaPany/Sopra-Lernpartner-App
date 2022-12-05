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

    def find_by_id(self, id):
        """ Wir suchen ein Profil mit der jeweiligen ID """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM Profil WHERE profil_id={0}".format(id)
        cursor.execute(command)
        profil_daten = cursor.fetchall()

        try:
            (profil_id, hochschule, studiengang, semester, lernfaecher, selbsteinschaetzung, person_id) = profil_daten[0]
            profil = Profil()
            profil.set_id(profil_id)
            profil.set_hochschule(hochschule)
            profil.set_studiengang(studiengang)
            profil.set_semester(semester)
            profil.set_lernfaecher(lernfaecher)
            profil.set_selbsteinschaetzung(selbsteinschaetzung)
            profil.set_person(person_id)
            result = profil
        except IndexError:
            """ Tritt auf, wenn es beim SELECT-Aufruf kein Ergebnis liefert, sondern profil_daten leer ist """
            result = None

        self._cnx.commit()
        cursor.close()
        print(result)
        return result