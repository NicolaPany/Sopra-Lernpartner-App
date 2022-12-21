import BusinessObject from "./BusinessObject";

export default class ProfilBO extends BusinessObject{
    constructor(hochschule, studiengang, semester, lernfaecher, selbsteinschaetzung, person){
        super();
        this.hochschule = hochschule;
        this.studiengang = studiengang;
        this.semester = semester;
        this.lernfaecher = lernfaecher;
        this.selbsteinschaetzung = selbsteinschaetzung;
    }

    get_hochschule(){
        return this.hochschule;
    }

    set_hochschule(hochschule){
        this.hochschule = hochschule;
    }

    get_studiengang(){
        return this.studiengang;
    }

    set_studiengang(studiengang){
        this.studiengang = studiengang;
    }

    get_semester(){
        return this.semester;
    }

    set_semester(semester){
        this.semester = semester;
    }

    get_lernfaecher(){
        return this.lernfaecher;
    }

    set_lernfaecher(lernfaecher){
        this.lernfaecher = lernfaecher;
    }

    get_selbsteinschaetzung(){
        return this.selbsteinschaetzung;
    }

    set_selbsteinschaetzung(selbsteinschaetzung){
        this.selbsteinschaetzung = selbsteinschaetzung;
    }


}