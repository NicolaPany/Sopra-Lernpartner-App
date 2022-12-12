from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from Administration import Administration

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
    'person': fields.Integer(attribute='_person', description='Person ID des Profils'),
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
})

nachricht = api.inherit('Nachricht', bo, {
    'nachricht_text': fields.String(attribute='_nachricht_text', description='Der Text, den eine Nachricht beinhaltet'),
    'person_id': fields.Integer(attribute='_person_id', description='Die ID der Person, die die Nachricht sendet'),
    'konversation_id': fields.Integer(attribute='_konversation_id', description='Die ID der zugehörigen Konversation'),
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
@lernpartnerapp.route('/profile')
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

@lernpartnerapp.route("/profile/<int:profil_id>")
@lernpartnerapp.param("profil_id", "Die Id des gewünschten Profils")
class ProfilByIdOperations(Resource):
    @lernpartnerapp.marshal_with(profil)
    def get(self, profil_id):
        """ Auslesen der Profil Instanz.
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


""" Server läuft auf localhost:5000 bzw. 127.0.0.1:5000 """
if __name__ == '__main__':
    app.run(debug=True)