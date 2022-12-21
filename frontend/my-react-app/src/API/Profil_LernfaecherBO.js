import BusinessObject from './BusinessObject';

export default class Profil_LernfaecherBO extends BusinessObject{

	constructor(lerngruppe_id, profil_id){
        super();
        this.lerngruppe_id = lerngruppe_id;
        this.profil_id = profil_id;
    }

    get_lerngruppe_id(){
        return this.lerngruppe_id;
    }

    set_lerngruppe_id(lerngruppe_id){
        this.lerngruppe_id = lerngruppe_id;
    }

    get_profil_id(){
        return this.profil_id;
    }

    set_profil_id(profil_id){
        this.profil_id = profil_id;
    }

}