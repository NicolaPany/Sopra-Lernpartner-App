from server.bo.Person import Person

from server.db.PersonMapper import PersonMapper

class Administration(object):

    def __init__(self):
        pass

    def create_person(self, name, vorname, lebensjahre, geschlecht, semester, studiengang, lerngruppe, google_user_id, email, profil_id):
        """Eine Person anlegen"""

        person = Person()
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
        person.set_id(1)

        with PersonMapper() as mapper:
            return mapper.insert(person)

    def get_all_persons(self):
        """Alle Personen auslesen"""
        with PersonMapper() as mapper:
            return mapper.find_all()

