import NamedBusinessObject from './NamedBusinessObject';


export default class LerngruppeBO extends NamedBusinessObject{

	constructor(lerngruppe_id, gruppenname, teilnehmer){
        super();
        this.lerngruppe_id = lerngruppe_id
        this.gruppenname = gruppenname
        this.teilnehmer = teilnehmer;
    }


    getlerngruppe_id(){
        return this.lerngruppe_id;
    }

    setlerngruppe_id(lerngruppe_id){
        this.lerngruppe_id = lerngruppe_id;
    }

    getgruppenname(){
        return this.gruppenname;
    }

    setgruppenname(gruppenname){
        this.gruppenname = gruppenname;
    }

    getteilnehmer(){
        return this.teilnehmer;
    }

    setteilnehmer(teilnehmer){
        this.teilnehmer = teilnehmer;
    }

}