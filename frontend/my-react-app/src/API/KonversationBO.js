import NamedBusinessObject from './NamedBusinessObject';

export default class KonversationBO extends NamedBusinessObject{

	constructor(koversation_id, anfragestatus){
		super();
		this.konversation_id = koversation_id
		this.anfragestatus = aanfragestatus

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

    setanfragestatus(aanfragestatus){
        this.anfragestatus = aanfragestatus;
    }

}