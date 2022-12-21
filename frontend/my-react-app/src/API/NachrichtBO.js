import BusinessObject from './BusinessObject';

export default class NachrichtBO extends BusinessObject{

	constructor(nachricht_id, nachricht_text, person_id, konversation_id){
        super();
        this.nachricht_id = nachricht_id;
        this.nachricht_text = nachricht_text;
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

}