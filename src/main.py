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
    'alter': fields.Integer(attribute='_alter', description='Alter einer Person'),
    'geschlecht': fields.String(attribute='_geschlecht', description='Geschlecht einer Person'),
    'semester': fields.String(attribute='_semester', description='Semester einer Person'),
    'studiengang': fields.String(attribute='_studiengang', description='Studiengang einer Person'),
    'lerngruppe': fields.String(attribute='_lerngruppe', description='Lerngruppe einer Person'),
    'google_user_id': fields.String(attribute='_google_user_id', description='Google user ID einer Person'),
    'email': fields.String(attribute='_email', description='E-Mail-Adresse einer Person'),
    'profil': fields.Integer(attribute='_profil', description='Profil ID einer Person'),
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

""" Server läuft auf localhost:5000 bzw. 127.0.0.1:5000 """
if __name__ == '__main__':
    app.run(debug=True)