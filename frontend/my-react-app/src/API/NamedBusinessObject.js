import BusinessObject from "./BusinessObject";

export default class NamedBusinessObject extends BusinessObject{

    constructor(name){
        super();
        this.name = name;
    }

    getname(){
        return this.name;
    }

    setname(name){
        this.name = name;
    }
}