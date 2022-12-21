import BusinessObject from './BusinessObject';

export default class ChatteilnahmeBO extends BusinessObject{

	constructor(chatteilnahme_id, profil_id, konversation_id){
        super();
        this.chatteilnahme_id = chatteilnahme_id;
        this.profil_id = profil_id;
        this.konversation_id = konversation_id;
    }

    get_chatteilnahme_id(){
        return this.chatteilnahme_id;
    }

    set_chatteilnahme_id(chatteilnahme_id){
        this.chatteilnahme_id = chatteilnahme_id;
    }

    get_profil_id(){
        return this.profil_id;
    }

    set_profil_id(profil_id){
        this.profil_id = profil_id;
    }

    get_konversation_id(){
        return this.konversation_id;
    }

    set_konversation_id(konversation_id){
        this.konversation_id = konversation_id;
    }

}