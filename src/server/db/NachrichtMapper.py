from server.bo.Nachricht import Nachricht
from server.db.Mapper import Mapper

class NachrichtMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result=[]
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Nachricht")
        nachricht_daten = cursor.fetchall()

        for (nachricht_id, nachricht_text, person_id, konversation_id) in nachricht_daten:
            nachricht = Nachricht()
            nachricht.set_id(nachricht_id)
            nachricht.set_nachricht_text(nachricht_text)
            nachricht.set_person_id(person_id)
            nachricht.set_konversation_id(konversation_id)
            result.append(nachricht)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result