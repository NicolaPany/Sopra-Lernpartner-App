from server.bo.Konversation import Konversation
from server.db.Mapper import Mapper

class KonversationMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result=[]
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Konversation")
        konversation_daten = cursor.fetchall()

        for (konversation_id, anfragestatus) in konversation_daten:
            konversation = Konversation()
            konversation.set_id(konversation_id)
            konversation.set_anfragestatus(anfragestatus)
            result.append(konversation)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result


    def find_by_id(self, id):
        """ Wir suchen eine Konversation mit der jeweiligen ID """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM Konversation WHERE konversation_id={0}".format(id)
        cursor.execute(command)
        konversation_daten = cursor.fetchall()

        try:
            (konversation_id, anfragestatus) = konversation_daten[0]
            konversation = Konversation()
            konversation.set_id(konversation_id)
            konversation.set_anfragestatus(anfragestatus)
            result = konversation
        except IndexError:
            """ Tritt auf, wenn es beim SELECT-Aufruf kein Ergebnis liefert, sondern konversation_daten leer ist """
            result = None

        self._cnx.commit()
        cursor.close()
        print(result)
        return result