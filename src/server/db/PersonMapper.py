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

        for (person_id, name, vorname, lebensjahre, geschlecht, lerngruppe, google_user_id, email, profil_id) in personen_daten:
            person = Person()
            person.set_id(person_id)
            person.set_name(name)
            person.set_vorname(vorname)
            person.set_lebensjahre(lebensjahre)
            person.set_geschlecht(geschlecht)
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

    def find_by_id(self, id):
        """ Wir suchen die Person mit der jeweiligen ID """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM Person WHERE person_id={0}".format(id)
        cursor.execute(command)
        person_daten = cursor.fetchall()

        try:
            (person_id, name, vorname, lebensjahre, geschlecht, lerngruppe, google_user_id, email, profil_id) = person_daten[0]
            person = Person()
            person.set_id(person_id)
            person.set_name(name)
            person.set_vorname(vorname)
            person.set_lebensjahre(lebensjahre)
            person.set_geschlecht(geschlecht)
            person.set_lerngruppe(lerngruppe)
            person.set_google_user_id(google_user_id)
            person.set_email(email)
            person.set_profil(profil_id)
            result = person
        except IndexError:
            """ Tritt auf, wenn es beim SELECT-Aufruf kein Ergebnis liefert, sondern personen_daten leer ist """
            result = None

        self._cnx.commit()
        cursor.close()
        print(result)
        return result
