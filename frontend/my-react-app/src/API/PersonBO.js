import NamedBusinessObject from "./NamedBusinessObject";

export default class PersonBO extends NamedBusinessObject{

    constructor(person_id, vorname, lebensjahre, geschlecht, lerngruppe, google_user_id, email, profil_id){
        super()
        this.person_id = person_id;
        this.vorname = vorname;
        this.lebensjahre = lebensjahre;
        this.geschlecht = geschlecht;
        this.lerngruppe = lerngruppe;
        this.google_user_id = google_user_id;
        this.email = email;
        this.profil_id = profil_id;
    }

    getperson_id(){
        return this.person_id;
    }

    setperson_id(person_id){
        this.person_id = person_id;
    }

    getvorname(){
        return this.vorname;
    }

    setvorname(vorname){
        this.vorname = vorname;
    }

    getlebensjahre(){
        return this.lebensjahre;
    }

    setlebensjahre(lebensjahre){
        this.lebensjahre = lebensjahre;
    }

    getgeschlecht(){
        return this.geschlecht;
    }

    setgeschlecht(geschlecht){
        this.geschlecht = geschlecht;
    }

    getlerngruppe(){
        return this.lerngruppe;
    }

    setlerngruppe(lerngruppe){
        this.lerngruppe = lerngruppe;
    }

    getgoogle_user_id(){
        return this.google_user_id;
    }

    setgoogle_user_id(google_user_id){
        this.google_user_id = google_user_id;
    }

    getemail(){
        return this.email;
    }

    setemail(email){
        this.email = email;
    }

    getprofil_id(){
        return this.profil_id;
    }

    setprofil_id(profil_id){
        this.profil_id = profil_id;
    }

}