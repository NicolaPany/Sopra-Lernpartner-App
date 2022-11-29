from server.bo.Person import Person
from server.bo.Profil import Profil
from server.bo.Lerndaten import Lerndaten

from server.db.PersonMapper import PersonMapper
from server.db.ProfilMapper import ProfilMapper
from server.db.LerndatenMapper import LerndatenMapper

class Administration(object):

    def __init__(self):
        pass

    def create_person(self, name, vorname, lebensjahre, geschlecht, lerngruppe, google_user_id, email, profil_id):
        """Eine Person anlegen"""

        person = Person()
        person.set_name(name)
        person.set_vorname(vorname)
        person.set_lebensjahre(lebensjahre)
        person.set_geschlecht(geschlecht)
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


    def create_profil(self, hochschule, studiengang, semester, lernfaecher, selbsteinschaetzung, id):
        """Ein Profil anlegen"""

        profil = Profil()
        profil.set_hochschule(hochschule)
        profil.set_studiengang(studiengang)
        profil.set_semester(semester)
        profil.set_lernfaecher(lernfaecher)
        profil.set_selbsteinschaetzung(selbsteinschaetzung)
        profil.set_person(id)
        profil.set_id(1)

        with ProfilMapper() as mapper:
            return mapper.insert(profil)

    def get_all_profile(self):
        """Alle Profile auslesen"""
        with ProfilMapper() as mapper:
            return mapper.find_all()


    def create_lerndaten(self, tageszeit, tage, frequenz, lernort, lernart, gruppengroesse_min, gruppengroesse_max, vorkenntnisse, extrovertiertheit, profil_id):
        """Lerndaten anlegen"""

        lerndaten = Lerndaten()
        lerndaten.set_tageszeit(tageszeit)
        lerndaten.set_tage(tage)
        lerndaten.set_frequenz(frequenz)
        lerndaten.set_lernort(lernort)
        lerndaten.set_lernart(lernart)
        lerndaten.set_gruppengroesse_min(gruppengroesse_min)
        lerndaten.set_gruppengroesse_max(gruppengroesse_max)
        lerndaten.set_vorkenntnisse(vorkenntnisse)
        lerndaten.set_extrovertiertheit(extrovertiertheit)
        lerndaten.set_profil(profil_id)
        lerndaten.set_id(1)

        with LerndatenMapper() as mapper:
            return mapper.insert(lerndaten)

    def get_all_lerndaten(self):
        """Alle Lerndaten auslesen"""
        with LerndatenMapper() as mapper:
            return mapper.find_all()