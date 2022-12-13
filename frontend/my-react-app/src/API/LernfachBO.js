import BusinessObject from './BusinessObject';

export default class LernfachBO extends BusinessObject{

	constructor(lernfachname){
        super();
        this.lernfachname = lernfachname;
    }

    getlernfachname(){
        return this.lernfachname;
    }

    setlernfachname(lernfachname){
        this.lernfachname = lernfachname;
    }

}