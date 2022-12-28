from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from Administration import Administration
from server.bo.Konversation import Konversation
from server.bo.Chatteilnahme import Chatteilnahme
from server.bo.Gruppenteilnahme import Gruppenteilnahme
from server.bo.Lerndaten import Lerndaten
from server.bo.Lernfaecher import Lernfaecher
from server.bo.Lerngruppe import Lerngruppe
from server.bo.Nachricht import Nachricht
from server.bo.Person import Person
from server.bo.Profil import Profil
from server.bo.Profil_Lernfaecher import Profil_Lernfaecher
from server.bo.Match import Match

""" Wir erstellen ein "Flask-Objekt" """
app = Flask(__name__)

""" Wir wählen einen Prefix (namens "lernapp") aus welcher für CORS freigegeben wird. """
CORS(app, ressources=r'/lernapp/*')

""" Mithilfe von Flask-Restx wird die Datenstruktur aufgebaut """
api = Api(app, version='1.0', title="Lernpartnerapp API")

""" Namespaces definieren"""
lernpartnerapp = api.namespace("lernapp", desription="Funktionen der LernPartner WebApp")

bo = api.model("BusinessObject", {
    "id": fields.String(attribute="_id", description="Id"),
})

nbo = api.inherit('NamedBusinessObject', bo, {
    'name': fields.String(attribute='_name', description='Name des BusinessObjects'),
})

person = api.inherit('Person', bo, {
    'vorname': fields.String(attribute='_vorname', description='Vorname einer Person'),
    'alter': fields.Integer(attribute='_lebensjahre', description='Alter einer Person'),
    'geschlecht': fields.String(attribute='_geschlecht', description='Geschlecht einer Person'),
    'lerngruppe': fields.String(attribute='_lerngruppe', description='Lerngruppe einer Person'),
    'google_user_id': fields.String(attribute='_google_user_id', description='Google user ID einer Person'),
    'email': fields.String(attribute='_email', description='E-Mail-Adresse einer Person'),
    'profil': fields.Integer(attribute='_profil', description='Profil ID einer Person'),
})

profil = api.inherit('Profil', bo, {
    'hochschule': fields.String(attribute='_hochschule', description='Hochschule, an der eine Person studiert'),
    'studiengang': fields.String(attribute='_studiengang', description='Studiengang einer Person'),
    'semester': fields.Integer(attribute='_semester', description='Semester einer Person'),
    'lernfaecher': fields.String(attribute='_lernfaecher', description='Lernfaecher einer Person'),
    'selbsteinschaetzung': fields.Integer(attribute='_selbsteinschaetzung', description='Selbsteinschätzung der Person'),
})

lerndaten = api.inherit('Lerndaten', bo, {
    'tageszeit': fields.String(attribute='_tageszeit', description='Präferierte Tageszeit, zu der gelernt wird'),
    'tage': fields.String(attribute='_tage', description='Präferierte Tage, an denen gelernt wird'),
    'frequenz': fields.Integer(attribute='_frequenz', description='Frequenz der Lerntage'),
    'lernort': fields.String(attribute='_lernort', description='Präferierter Ort, an dem gelernt wird'),
    'lernart': fields.String(attribute='_lernart', description='Auf welche Art am liebsten gelernt wird (online/offline)'),
    'gruppengroesse_min': fields.Integer(attribute='_gruppengroesse_min', description='Mindestanzahl der gewünschten Gruppenmitglieder'),
    'gruppengroesse_max': fields.Integer(attribute='_gruppengroesse_max', description='Maximale Anzahl der gewünschten Gruppenmitglieder'),
    'vorkenntnisse': fields.String(attribute='_vorkenntnisse', description='Eigene Beurteilung der Vorkenntnisse (sehr gut, gut, mittel, schlecht, sehr schlecht)'),
    'extrovertiertheit': fields.String(attribute='_extrovertiertheit', description='Eigene Beurteilung der Extrovertiertheit (sehr, mittel, schwach)'),
    'profil': fields.Integer(attribute='_profil', description='Profil ID einer Person'),
})

lerngruppe = api.inherit('Lerngruppe', bo, {
    'gruppenname': fields.String(attribute='_gruppenname', description='Name der Lerngruppe'),
    'teilnehmer': fields.String(attribute='_teilnehmer', description='Teilnehmer der Lerngruppe'),
})

konversation = api.inherit('Konversation', bo, {
    'anfragestatus': fields.String(attribute='_anfragestatus', description='Der Anfragestatus der Konversation, sprich, haben beide Teilnehmer die Chatanfrage bestätigt'),
    'nachricht': fields.Integer(attribute='_nachricht', description='ID einer Nachricht'),
})

nachricht = api.inherit('Nachricht', bo, {
    'nachricht_text': fields.String(attribute='_nachricht_text', description='Der Text, den eine Nachricht beinhaltet'),

})

chatteilnahme = api.inherit('Chatteilnahme', bo, {
    'profil': fields.Integer(attribute='_profil', description='Profil ID einer Person'),
    'konversation': fields.Integer(attribute='_konversation', description='ID der Konversation'),
})

gruppenteilnahme = api.inherit('Gruppenteilnahme', bo, {
    'status': fields.String(attribute='_status', description='Status der Teilnahme'),
    'profil': fields.Integer(attribute='_profil', description='Profil ID einer Person'),
    'lerngruppe': fields.Integer(attribute='_lerngruppe', description='ID der Lerngruppe'),
})

lernfaecher = api.inherit('Lernfaecher', bo, {
    'lernfachname': fields.String(attribute='_lernfachname', description='Name des Lernfaches'),
})

profil_lernfaecher = api.inherit('Profil_Lernfaecher', bo, {
    'profil': fields.Integer(attribute='_profil', description='Profil ID einer Person'),
    'lernfach': fields.Integer(attribute='_lernfach', description='ID des Lernfaches'),
})

match = api.inherit('Match', bo, {
    'match_id': fields.Integer(attribute='_match_id', description='ID des Matches'),
    'suchende_person_id': fields.Integer(attribute='_suchende_person_id', description='ID der suchenden Person'),
    'quote': fields.Integer(attribute='_quote', description='Übereinstimmungsquote'),
    'lernfach': fields.String(attribute='_lernfach', description='Lernfach nach dem gesucht wird'),
    'match_profil_id': fields.Integer(attribute='_match_profil_id', description='ID der gematchten Person'),
})

"""Person"""
@lernpartnerapp.route('/personen')
@lernpartnerapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class PersonenOperations(Resource):
    @lernpartnerapp.marshal_list_with(person)
    def get(self):
        """Auslesen aller Personen-Objekte.
        Sollten keine Personen-Objekte verfügbar sein,
        so wird eine leere Sequenz zurückgegeben."""

        adm = Administration()
        personen = adm.get_all_persons()
        return personen


@lernpartnerapp.route("/personen/<int:person_id>")
@lernpartnerapp.param("person_id", "Die Id der gewünschten Person")
class PersonByIdOperations(Resource):
    @lernpartnerapp.marshal_with(person)
    def get(self, person_id):
        """ Auslesen der Person Instanz.
        Das zu auslesende Objekt wird anhand der id bestimmt
        """
        adm = Administration()
        person = adm.get_person_by_id(person_id)
        return person

    def delete(self, person_id):
        """Löschen einer Person Instanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        person = adm.delete_person_by_person_id(person_id)
        return person


"""Profil"""
@lernpartnerapp.route('/profil')
@lernpartnerapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ProfilOperations(Resource):
    @lernpartnerapp.marshal_list_with(profil)
    def get(self):
        """Auslesen aller Profil-Objekte.
        Sollten keine Profil-Objekte verfügbar sein,
        so wird eine leere Sequenz zurückgegeben."""

        adm = Administration()
        profile = adm.get_all_profile()
        return profile

    @lernpartnerapp.marshal_with(profil, code=201)
    @lernpartnerapp.expect(profil)
    def post(self):
        """ Profil Instanz erstellen """
        adm = Administration()
        """ Wir setzen den api.payload in die from_dict Methode ein und erstellen damit ein Profil, indem wir die 
        Attribute aus den Werten von api.payload setzen. profil_object = Profil-Objekt """
        profil_object = Profil.from_dict(api.payload)

        if profil_object is not None:
            """ Wir erstellen in Administration eine Projekt mithilfe der Daten vom api.payload """
            c = adm.create_profil(profil_object.get_hochschule(), profil_object.get_studiengang(),
                                  profil_object.get_semester(), profil_object.get_lernfaecher(),
                                  profil_object.get_selbsteinschaetzung())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500

@lernpartnerapp.route("/profil/<int:profil_id>")
@lernpartnerapp.param("profil_id", "Die Id des gewünschten Profils")
class ProfilByIdOperations(Resource):
    @lernpartnerapp.marshal_with(profil)
    def get(self, profil_id):
        """ Auslesen der Profil-Instanz.
        Das zu auslesende Objekt wird anhand der id bestimmt
        """
        adm = Administration()
        profil = adm.get_profil_by_id(profil_id)
        return profil

    def delete(self, profil_id):
        """Löschen einer Profil Instanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        profil = adm.delete_profil_by_profil_id(profil_id)
        return profil

    @lernpartnerapp.marshal_with(profil)
    @lernpartnerapp.expect(profil, validate=True)
    def put(self, profil_id):
        """ Profil Instanz updaten """
        adm = Administration()
        profil_object = Profil.from_dict(api.payload)

        if profil_object is not None:
            """Hierdurch wird die id des zu überschreibenden Profil-Objekts gesetzt.
            """
            profil_object.set_id(profil_id)
            adm.update_profil(profil_object)
            return '', 200
        else:
            return '', 500


"""Lerndaten"""
@lernpartnerapp.route('/lerndaten')
@lernpartnerapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class LerndatenOperations(Resource):
    @lernpartnerapp.marshal_list_with(lerndaten)
    def get(self):
        """Auslesen aller Lerndaten-Objekte.
        Sollten keine Lerndaten-Objekte verfügbar sein,
        so wird eine leere Sequenz zurückgegeben."""

        adm = Administration()
        lerndaten = adm.get_all_lerndaten()
        return lerndaten



"""Lerngruppe"""
@lernpartnerapp.route('/lerngruppe')
@lernpartnerapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class LerngruppeOperations(Resource):
    @lernpartnerapp.marshal_list_with(lerngruppe)
    def get(self):
        """Auslesen aller Lerngruppen-Objekte.
        Sollten keine Lerngruppen-Objekte verfügbar sein,
        so wird eine leere Sequenz zurückgegeben."""

        adm = Administration()
        lerngruppe = adm.get_all_lerngruppe()
        return lerngruppe

@lernpartnerapp.route("/lerngruppe/<int:lerngruppe_id>")
@lernpartnerapp.param("lerngruppe_id", "Die Id der gewünschten Lerngruppe")
class LerngruppeByIdOperations(Resource):
    @lernpartnerapp.marshal_with(lerngruppe)
    def get(self, lerngruppe_id):
        """ Auslesen der Lerngruppen Instanz.
        Das zu auslesende Objekt wird anhand der id bestimmt
        """
        adm = Administration()
        lerngruppe = adm.get_lerngruppe_by_id(lerngruppe_id)
        return lerngruppe



"""Konversation"""
@lernpartnerapp.route('/konversation')
@lernpartnerapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class KonversationOperations(Resource):
    @lernpartnerapp.marshal_list_with(konversation)
    def get(self):
        """Auslesen aller Konversations-Objekte.
        Sollten keine Konversations-Objekte verfügbar sein,
        so wird eine leere Sequenz zurückgegeben."""

        adm = Administration()
        konversation = adm.get_all_konversation()
        return konversation

    @lernpartnerapp.marshal_with(konversation, code=201)
    @lernpartnerapp.expect(konversation)
    def post(self):
        """ Konversation Instanz erstellen """
        adm = Administration()
        """ Wir setzen den api.payload in die from_dict Methode ein und erstellen damit eine Konversation, indem wir 
        ihre Attribute aus den Werten von api.payload setzen. konversation_object = Konversation-Objekt """
        konversation_object = Konversation.from_dict(api.payload)

        if konversation_object is not None:
            """ Wir erstellen in Administration eine Konversation mithilfe der Daten des api.payload """
            c = adm.create_konversation(konversation_object.get_anfragestatus(), konversation_object.get_nachricht_id())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500

        """Noch nicht ganz fertig"""







@lernpartnerapp.route("/konversation/<int:konversation_id>")
@lernpartnerapp.param("konversation_id", "Die Id der gewünschten Konversation")
class KonversationByIdOperations(Resource):
    @lernpartnerapp.marshal_with(konversation)
    def get(self, konversation_id):
        """ Auslesen der Konversation Instanz.
        Das zu auslesende Objekt wird anhand der id bestimmt
        """
        adm = Administration()
        konversation = adm.get_konversation_by_id(konversation_id)
        return konversation

    def delete(self, konversation_id):
        """Löschen einer Konversation Instanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        konversation = adm.delete_konversation_by_konversation_id(konversation_id)
        return konversation

    @lernpartnerapp.marshal_with(konversation)
    @lernpartnerapp.expect(konversation, validate=True)
    def put(self, konversation_id):
        """ Konversation Instanz updaten """
        adm = Administration()
        konversation_object = Konversation.from_dict(api.payload)

        if konversation_object is not None:
            """Hierdurch wird die id des zu überschreibenden Konversations-Objekts gesetzt.
            """
            konversation_object.set_id(konversation_id)
            adm.update_konversation(konversation_object)
            return '', 200
        else:
            return '', 500


"""Nachricht"""
@lernpartnerapp.route('/nachricht')
@lernpartnerapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class NachrichtOperations(Resource):
    @lernpartnerapp.marshal_list_with(nachricht)
    def get(self):
        """Auslesen aller Nachrichten-Objekte.
        Sollten keine Nachrichten-Objekte verfügbar sein,
        so wird eine leere Sequenz zurückgegeben."""

        adm = Administration()
        nachricht = adm.get_all_nachricht()
        return nachricht


"""Chatteilnahme"""
@lernpartnerapp.route('/chatteilnahme')
@lernpartnerapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ChatteilnahmeOperations(Resource):
    @lernpartnerapp.marshal_list_with(chatteilnahme)
    def get(self):
        """Auslesen aller Chatteilnahme-Objekte.
        Sollten keine Chatteilnahme-Objekte verfügbar sein,
        so wird eine leere Sequenz zurückgegeben."""

        adm = Administration()
        chatteilnahme = adm.get_all_chatteilnahme()
        return chatteilnahme



"""Gruppenteilnahme"""
@lernpartnerapp.route('/gruppenteilnahme')
@lernpartnerapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class GruppenteilnahmeOperations(Resource):
    @lernpartnerapp.marshal_list_with(gruppenteilnahme)
    def get(self):
        """Auslesen aller Gruppenteilnahme-Objekte.
        Sollten keine Gruppenteilnahme-Objekte verfügbar sein,
        so wird eine leere Sequenz zurückgegeben."""

        adm = Administration()
        gruppenteilnahme = adm.get_all_gruppenteilnahme()
        return gruppenteilnahme


"""Lernfaecher"""
@lernpartnerapp.route('/lernfaecher')
@lernpartnerapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class LernfaecherOperations(Resource):
    @lernpartnerapp.marshal_list_with(lernfaecher)
    def get(self):
        """Auslesen aller Lernfaecher-Objekte.
        Sollten keine Lernfaecher-Objekte verfügbar sein,
        so wird eine leere Sequenz zurückgegeben."""

        adm = Administration()
        lernfaecher = adm.get_all_lernfaecher()
        return lernfaecher


"""Profil_Lernfaecher"""
@lernpartnerapp.route('/profil_lernfaecher')
@lernpartnerapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class Profil_LernfaecherOperations(Resource):
    @lernpartnerapp.marshal_list_with(profil_lernfaecher)
    def get(self):
        """Auslesen aller Profil_Lernfaecher-Objekte.
        Sollten keine Profil_Lernfaecher-Objekte verfügbar sein,
        so wird eine leere Sequenz zurückgegeben."""

        adm = Administration()
        profil_lernfaecher = adm.get_all_profil_lernfaecher()
        return profil_lernfaecher


"""Match"""
@lernpartnerapp.route('/match')
@lernpartnerapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class MatchOperations(Resource):
    @lernpartnerapp.marshal_list_with(match)
    def get(self):
        """Auslesen aller Match-Objekte.
        Sollten keine Match-Objekte verfügbar sein,
        so wird eine leere Sequenz zurückgegeben."""

        adm = Administration()
        match = adm.get_all_match()
        return match


""" Server läuft auf localhost:5000 bzw. 127.0.0.1:5000 """
if __name__ == '__main__':
    app.run(debug=True)