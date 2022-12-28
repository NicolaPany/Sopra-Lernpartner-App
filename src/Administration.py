from server.bo.Person import Person
from server.bo.Profil import Profil
from server.bo.Lerndaten import Lerndaten
from server.bo.Lerngruppe import Lerngruppe
from server.bo.Konversation import Konversation
from server.bo.Nachricht import Nachricht
from server.bo.Chatteilnahme import Chatteilnahme
from server.bo.Gruppenteilnahme import Gruppenteilnahme
from server.bo.Lernfaecher import Lernfaecher
from server.bo.Profil_Lernfaecher import Profil_Lernfaecher
from server.bo.Match import Match

from server.db.PersonMapper import PersonMapper
from server.db.ProfilMapper import ProfilMapper
from server.db.LerndatenMapper import LerndatenMapper
from server.db.LerngruppeMapper import LerngruppeMapper
from server.db.KonversationMapper import KonversationMapper
from server.db.NachrichtMapper import NachrichtMapper
from server.db.ChatteilnahmeMapper import ChatteilnahmeMapper
from server.db.GruppenteilnahmeMapper import GruppenteilnahmeMapper
from server.db.LernfaecherMapper import LernfaecherMapper
from server.db.Profil_LernfaecherMapper import Profil_LernfaecherMapper
from server.db.MatchMapper import MatchMapper

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
        person.set_profil_id(profil_id)
        person.set_id(1)

        with PersonMapper() as mapper:
            return mapper.insert(person)

    def get_all_persons(self):
        """Alle Personen auslesen"""
        with PersonMapper() as mapper:
            return mapper.find_all()

    def get_person_by_id(self, person_id):
        """ Wir geben die Person mit der angegebenen ID zurück """
        with PersonMapper() as mapper:
            return mapper.find_by_id(person_id)

    def delete_person_by_person_id(self, person_id):
        """ Wir löschen die Person anhand der angegebenen Personen ID """
        with PersonMapper() as mapper:
            return mapper.delete(person_id)



    def create_profil(self, hochschule, studiengang, semester, lernfaecher, selbsteinschaetzung):
        """Ein Profil anlegen"""

        profil = Profil()
        profil.set_hochschule(hochschule)
        profil.set_studiengang(studiengang)
        profil.set_semester(semester)
        profil.set_lernfaecher(lernfaecher)
        profil.set_selbsteinschaetzung(selbsteinschaetzung)
        profil.set_id(1)

        with ProfilMapper() as mapper:
            return mapper.insert(profil)

    def get_all_profile(self):
        """Alle Profile auslesen"""
        with ProfilMapper() as mapper:
            return mapper.find_all()

    def get_profil_by_id(self, profil_id):
        """ Wir geben das Profil mit der angegebenen ID zurück """
        with ProfilMapper() as mapper:
            return mapper.find_by_id(profil_id)

    def update_profil(self, profil):
        """ Wir aktualisieren die Profil-Daten"""
        with ProfilMapper() as mapper:
            return mapper.update(profil)

    def delete_profil_by_profil_id(self, profil_id):
        """ Wir löschen das Profil anhand der angegebenen Profil-ID """
        with ProfilMapper() as mapper:
            return mapper.delete(profil_id)


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


    def create_lerngruppe(self, gruppenname, teilnehmer):
        """Eine Lerngruppe erstellen"""

        lerngruppe = Lerngruppe()
        lerngruppe.set_gruppenname(gruppenname)
        lerngruppe.set_teilnehmer(teilnehmer)
        lerngruppe.set_id(1)

        with LerngruppeMapper() as mapper:
            return mapper.insert(lerngruppe)

    def get_all_lerngruppe(self):
        """Alle Lerngruppen auslesen"""
        with LerngruppeMapper() as mapper:
            return mapper.find_all()

    def get_lerngruppe_by_id(self, lerngruppe_id):
        """ Wir geben die Lerngruppe mit der angegebenen ID zurück """
        with LerngruppeMapper() as mapper:
            return mapper.find_by_id(lerngruppe_id)


    def create_konversation(self, anfragestatus, nachricht_id):
        """Eine Konversation erstellen"""

        konversation = Konversation()
        konversation.set_anfragestatus(anfragestatus)
        konversation.set_nachricht_id(nachricht_id)
        konversation.set_id(1)

        with KonversationMapper() as mapper:
            return mapper.insert(konversation)

    def get_all_konversation(self):
        """Alle Konversationen auslesen"""
        with KonversationMapper() as mapper:
            return mapper.find_all()

    def get_konversation_by_id(self, konversation_id):
        """ Wir geben die Konversation mit der angegebenen ID zurück """
        with KonversationMapper() as mapper:
            return mapper.find_by_id(konversation_id)

    def delete_konversation_by_konversation_id(self, konversation_id):
        """ Wir löschen die Konversation anhand der angegebenen Konversations-ID """
        with KonversationMapper() as mapper:
            #konversation = self.get_all_konversation()
            return mapper.delete(konversation_id)

    def update_konversation(self, konversation):
        """ Wir aktualisieren die Konversations-Daten"""
        with KonversationMapper() as mapper:
            return mapper.update(konversation)


    def create_nachricht(self, nachricht_text):
        """Eine Nachricht erstellen"""

        nachricht = Nachricht()
        nachricht.set_nachricht_text(nachricht_text)
        nachricht.set_id(1)

        with NachrichtMapper() as mapper:
            return mapper.insert(nachricht)

    def get_all_nachricht(self):
        """Alle Nachrichten auslesen"""
        with NachrichtMapper() as mapper:
            return mapper.find_all()


    def create_chatteilnahme(self, profil_id, konversation_id):
        """Eine Chatteilnahme erstellen"""

        chatteilnahme = Chatteilnahme()
        chatteilnahme.set_profil_id(profil_id)
        chatteilnahme.set_konversation_id(konversation_id)
        chatteilnahme.set_id(1)

        with ChatteilnahmeMapper() as mapper:
            return mapper.insert(chatteilnahme)

    def get_all_chatteilnahme(self):
        """Alle Chatteilnahmen auslesen"""
        with ChatteilnahmeMapper() as mapper:
            return mapper.find_all()


    def create_gruppenteilnahme(self, status, profil_id, lerngruppe_id):
        """Eine Gruppenteilnahme erstellen"""

        gruppenteilnahme = Gruppenteilnahme()
        gruppenteilnahme.set_status(status)
        gruppenteilnahme.set_profil_id(profil_id)
        gruppenteilnahme.set_lerngruppe_id(lerngruppe_id)
        gruppenteilnahme.set_id(1)

        with GruppenteilnahmeMapper() as mapper:
            return mapper.insert(gruppenteilnahme)

    def get_all_gruppenteilnahme(self):
        """Alle Gruppenteilnahmen auslesen"""
        with GruppenteilnahmeMapper() as mapper:
            return mapper.find_all()


    def create_lernfaecher(self, lernfachname):
        """Lernfaecher erstellen"""

        lernfaecher = Lernfaecher()
        lernfaecher.set_lernfachname(lernfachname)
        lernfaecher.set_id(1)

        with LernfaecherMapper() as mapper:
            return mapper.insert(lernfaecher)

    def get_all_lernfaecher(self):
        """Alle Lernfaecher auslesen"""
        with LernfaecherMapper() as mapper:
            return mapper.find_all()


    def create_profil_lernfaecher(self, profil_id, lernfach_id):
        """Profil_Lernfaecher erstellen"""

        profil_lernfaecher = Profil_Lernfaecher()
        profil_lernfaecher.set_profil_id(profil_id)
        profil_lernfaecher.set_lernfach_id(lernfach_id)
        profil_lernfaecher.set_id(1)

        with Profil_LernfaecherMapper() as mapper:
            return mapper.insert(profil_lernfaecher)

    def get_all_profil_lernfaecher(self):
        """Alle Profil_Lernfaecher auslesen"""
        with Profil_LernfaecherMapper() as mapper:
            return mapper.find_all()


    def create_match(self, suchende_person_id, quote, lernfach, match_profil_id):
        """Matches erstellen"""

        match = Match()
        match.set_suchende_person_id(suchende_person_id)
        match.set_quote(quote)
        match.set_lernfach(lernfach)
        match.set_match_profil_id(match_profil_id)
        match.set_id(1)

        with MatchMapper() as mapper:
            return mapper.insert(match)

    def get_all_match(self):
        """Alle Matches auslesen"""
        with MatchMapper() as mapper:
            return mapper.find_all()