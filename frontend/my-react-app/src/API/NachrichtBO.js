import BusinessObject from './BusinessObject';

export default class NachrichtBO extends BusinessObject{

	constructor(nachricht_id, nachricht_text, person_id, konversation_id){
        super();
        this.nachricht_id = nachricht_id;
        this.nachricht_text = nachricht_text;
        this.person_id = person_id;
        this.konversation_id = konversation_id;
    }

    getnachricht_id(){
        return this.nachricht_id;
    }

    setnachricht_id(nachricht_id){
        this.nachricht_id = nachricht_id;
    }

    getnachricht_text(){
        return this.nachricht_text;
    }

    setnachricht_text(nachricht_text){
        this.nachricht_text = nachricht_text;
    }

    getperson_id(){
        return this.person_id;
    }

    setperson_id(person_id){
        this.person_id = person_id;
    }

    getkonversation_id(){
        return this.konversation_id;
    }

    setkonversation_id(konversation_id){
        this.konversation_id = konversation_id;
    }

}