from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

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

""" Server läuft auf localhost:5000 bzw. 127.0.0.1:5000 """
if __name__ == '__main__':
    app.run(debug=True)