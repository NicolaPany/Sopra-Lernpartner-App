import NamedBusinessObject from './NamedBusinessObject';

export default class KonversationBO extends NamedBusinessObject{

	constructor(koversation_id, anfragestatus, nachricht_id){
		super();
		this.konversation_id = koversation_id;
		this.anfragestatus = aanfragestatus;
		this.nachricht_id = nachricht_id;
    }

    getkonversation_id(){
        return this.konversation_id;
    }

    setkonversation_id(konversation_id){
        this.konversation_id = konversation_id;
    }

    getanfragestatus(){
        return this.anfragestatus;
    }

    setanfragestatus(anfragestatus){
        this.anfragestatus = anfragestatus;
    }

    getnachricht_id(){
        return this.nachricht_id;
    }

    setnachricht_id(nachricht_id){
        this.nachricht_id = nachricht_id;
    }

}