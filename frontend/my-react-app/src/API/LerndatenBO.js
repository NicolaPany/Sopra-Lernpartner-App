import BusinessObject from './BusinessObject';

export default class LerndatenBO extends BusinessObject{

    constructor(tageszeit, tage, frequenz, lernort, lernart, gruppengroesse_min, gruppengroesse_max, vorkenntnisse, extrovertiertheit, profil_id)
        super();
        this.tageszeit = tageszeit
        this.tage = tage
        this.frequenz = frequenz
        this.lernort = lernort
        this.lernart = lernart
        this.gruppengroesse_min = gruppengroesse_min
        this.gruppengroesse_max = gruppengroesse_max
        this.vorkenntnisse = vorkenntnisse
        this.extrovertiertheit = extrovertiertheit
        this.profil_id = profil_id;
    }

    gettageszeit(){
        return this.tageszeit;
    }

    settageszeit(tageszeit){
        this.tageszeit = tageszeit;
    }

    gettage(){
        return this.tage;
    }

    settage(tage){
        this.tage = tages;
    }

    getfrequenz(){
        return this.frequenz;
    }

    setfrequenz(frequenz){
        this.frequenz = frequenz;
    }

    getlernort(){
        return this.lernort;
    }

    setlernort(lernort){
        this.lernort = lernort;
    }

    getlernart(){
        return this.lernart;
    }

    setlernart(lernart){
        this.lernart = lernart;
    }

    getgruppengroesse_min(){
        return this.gruppengroesse_min;
    }

    setgruppengroesse_min(gruppengroesse_min){
        this.gruppengroesse_min = gruppengroesse_min;
    }

    getgruppengroesse_max(){
        return this.gruppengroesse_max;
    }

    setgruppengroesse_max(gruppengroesse_max){
        this.gruppengroesse_max = gruppengroesse_max;
    }

    getvorkenntnisse(){
        return this.vorkenntnisse;
    }

    setvorkenntnisse(vorkenntnisse){
        this.vorkenntnisse = vorkenntnisse;
    }

    getextrovertiertheit(){
        return this.extrovertiertheit;
    }

    setextrovertiertheit(extrovertiertheit){
        this.extrovertiertheit = extrovertiertheit;
    }

    getprofil_id(){
        return this.profil_id;
    }

    setprofil_id(profil_id){
        this.profil_id = profil_id;
    }

