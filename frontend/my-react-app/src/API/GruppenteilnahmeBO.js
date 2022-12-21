import BusinessObject from './BusinessObject';

export default class GruppenteilnahmeBO extends BusinessObject{

	constructor(gruppenteilnahme_id, status, profil_id, lerngruppe_id){
        super();
        this.gruppenteilnahme_id = gruppenteilnahme_id;
        this.status = status;
        this.profil_id = profil_id;
        this.lerngruppe_id = lerngruppe_id;
    }

    getgruppenteilnahme_id(){
        return this.gruppenteilnahme_id;
    }

    setgruppenteilnahme_id(gruppenteilnahme_id){
        this.gruppenteilnahme_id = gruppenteilnahme_id;
    }

    getstatus(){
        return this.status;
    }

    setstatus(status){
        this.status = status;
    }

    getprofil_id(){
        return this.profil_id;
    }

    setprofil_id(profil_id){
        this.profil_id = profil_id;
    }

    getlerngruppe_id(){
        return this.lerngruppe_id;
    }

    setlerngruppe_id(lerngruppe_id){
        this.lerngruppe_id = lerngruppe_id;
    }

}