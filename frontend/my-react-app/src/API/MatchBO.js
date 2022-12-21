import BusinessObject from './BusinessObject';

export default class MatchBO extends BusinessObject{

	constructor(match_id, suchende_person_id, quote, lernfach, match_profil_id){
        super();
        this.match_id = match_id;
        this.suchende_person_id = suchende_person_id;
        this.quote = quote;
        this.lernfach = lernfach;
        this.match_profil_id = match_profil_id;
    }

    getmatch_id(){
        return this.match_id;
    }

    setmatch_id(match_id){
        this.match_id = match_id;
    }

    getsuchende_person_id(){
        return this.suchende_person_id;
    }

    setsuchende_person_id(suchende_person_id){
        this.status = suchende_person_id;
    }

    getquote(){
        return this.quote;
    }

    setquote(quote){
        this.quote = quote;
    }

    getlernfach(){
        return this.lernfach;
    }

    setlernfach(lernfach){
        this.lernfach = lernfach;
    }

    getmatch_profil_id(){
        return this.match_profil_id;
    }

    setmatch_profil_id(match_profil_id){
        this.match_profil_id = match_profil_id;
    }

}