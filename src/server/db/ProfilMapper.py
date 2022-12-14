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


    def insert(self, profil):
        """ Einfügen eines neuen Profil-Objekts in die Datenbank.
        parameter: Profil Instanz, die in der Datenbank gespeichert werden soll
        return: Die Profil Instanz mit korrigierter bzw. inkrementierter ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(profil_id) AS maxid FROM Profil ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            profil.set_id(maxid[0] + 1)


        """ Hier wird die Profil Instanz in die Datenbank mit Hilfe des Insert Befehls gespeichert """
        command = "INSERT INTO Profil (profil_id, hochschule, studiengang, semester, lernfaecher, selbsteinschaetzung, person_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = (profil.get_id(), profil.get_hochschule(), profil.get_studiengang(), profil.get_semester(),
                profil.get_lernfaecher(), profil.get_selbsteinschaetzung(), profil.get_person())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return profil


    def update(self, profil):
        """Wiederholtes Schreiben eines Profil-Objekts in die Datenbank.
        :param profil das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE Profil " + "SET hochschule=%s, studiengang=%s, semester=%s, lernfaecher=%s, selbsteinschaetzung=%s, person_id=%s WHERE profil_id=%s"
        data = (profil.get_hochschule(), profil.get_studiengang(), profil.get_semester(),
                profil.get_lernfaecher(), profil.get_selbsteinschaetzung(), profil.get_person(), profil.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()


    def delete(self, profil):
        """Löschen der Daten eines Profil-Objekts aus der Datenbank.
        :param profil das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM Profil WHERE profil_id={}".format(profil)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return profil