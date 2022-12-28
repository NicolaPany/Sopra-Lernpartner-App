from server.bo.Match import Match
from server.db.Mapper import Mapper


"""Unfertig"""
class MatchMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result=[]
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Match")
        match_daten = cursor.fetchall()

        for (match_id, suchende_person_id, quote, lernfach, match_profil_id) in match_daten:
            match = Match()
            match.set_id(match_id)
            match.set_suchende_person_id(suchende_person_id)
            match.set_quote(quote)
            match.set_lernfach(lernfach)
            match.set_match_profil_id(match_profil_id)
            result.append(match)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result