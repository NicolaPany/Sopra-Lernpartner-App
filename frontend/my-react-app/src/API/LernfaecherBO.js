import BusinessObject from './BusinessObject';

export default class LernfaecherBO extends BusinessObject{

	constructor(lernfach_id, lernfachname){
        super();
        this.lernfach_id = lernfach_id;
        this.lernfachname = lernfachname;
    }

    getlernfach_id(){
        return this.lernfach_id;
    }

    setlernfach_id(lernfach_id){
        this.lernfach_id = lernfach_id;
    }

    getlernfachname(){
        return this.lernfachname;
    }

    setlernfachname(lernfachname){
        this.lernfachname = lernfachname;
    }

}