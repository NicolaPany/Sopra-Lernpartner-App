from server.bo.Person import Person
from server.db.Mapper import Mapper


class PersonMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result=[]
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Person")
        personen_daten = cursor.fetchall()

        for (id, name, vorname, lebensjahre, geschlecht, semester, studiengang, lerngruppe, google_user_id, email, profil_id) in personen_daten:
            person = Person()
            person.set_id(id)
            person.set_name(name)
            person.set_vorname(vorname)
            person.set_lebensjahre(lebensjahre)
            person.set_geschlecht(geschlecht)
            person.set_semester(semester)
            person.set_studiengang(studiengang)
            person.set_lerngruppe(lerngruppe)
            person.set_google_user_id(google_user_id)
            person.set_email(email)
            person.set_profil(profil_id)
            result.append(person)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result
