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

        for (konversation_id, anfragestatus, nachricht_id) in konversation_daten:
            konversation = Konversation()
            konversation.set_id(konversation_id)
            konversation.set_anfragestatus(anfragestatus)
            konversation.set_nachricht_id(nachricht_id)
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
            (konversation_id, anfragestatus, nachricht_id) = konversation_daten[0]
            konversation = Konversation()
            konversation.set_id(konversation_id)
            konversation.set_anfragestatus(anfragestatus)
            konversation.set_nachricht_id(nachricht_id)
            result = konversation
        except IndexError:
            """ Tritt auf, wenn es beim SELECT-Aufruf kein Ergebnis liefert, sondern konversation_daten leer ist """
            result = None

    def delete(self, konversation):
        """Löschen der Daten eines Konversations-Objekts aus der Datenbank.

        :param konversation das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM Konversation WHERE konversation_id={}".format(konversation)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return konversation

    def update(self, konversation):
        """Überschreiben eines Konversation-Objekts in die Datenbank.
        :param konversation das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()
        command = "UPDATE Konversation " + "SET anfragestatus=%s + SET nachricht_id=%s WHERE konversation_id=%s"
        data = (konversation.get_anfragestatus(), konversation.get_nachricht_id(), konversation.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def insert(self, konversation):
        """ Einfügen eines neuen Konversation-Objekts in die Datenbank.
        parameter: Konversation Instanz, die in der Datenbank gespeichert werden soll
        return: Die Konversation Instanz mit korrigierter bzw. inkrementierter ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(konversation_id) AS maxid FROM Konversation ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            konversation.set_id(maxid[0] + 1)

        """ Hier wird die Konversation Instanz in die Datenbank mit Hilfe des Insert Befehl gespeichert """
        command = "INSERT INTO Konversation (konversation_id, anfragestatus, nachricht_id) VALUES (%s,%s,%s)"
        data = (konversation.get_id(), konversation.get_anfragestatus(), konversation.get_nachricht_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return konversation

        self._cnx.commit()
        cursor.close()
        print(result)
        return result