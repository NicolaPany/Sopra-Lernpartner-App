import ChatteilnahmeBO from './ChatteilnahmeBO';
import GruppenteilnahmeBO from './GruppenteilnahmeBO';
import KonversationBO from './KonversationBO';
import LerndatenBO from './LerndatenBO';
import LernfaecherBO from './LernfaecherBO';
import LerngruppeBO from './LerngruppeBO';
import MatchBO from './MatchBO';
import NachrichtBO from './NachrichtBO';
import PersonBO from './PersonBO';
import Profil_LernfaecherBO from './Profil_LernfaecherBO';
import ProfilBO from './ProfilBO';

export default class AppAPI {

            static #api = null;

            #AppServerBaseURL = '/lernapp'

            static getAPI() {
              if (this.#api == null) {
                this.#api = new AppAPI();
              }
            return this.#api;
            }

            #fetchAdvanced = (url, init) => fetch(url, init, {credential: 'include'})
              .then(res => {
                 if (!res.ok) {
                   throw Error(`${res.status} ${res.statusText}`);
                 }
                 return res.json();
              }
            )



            //Person related
            #getPersonURL = () => `${this.AppServerBaseURL}/personen`;
            #addPersonURL = () => `${this.#AppServerBaseURL}/personen`;
            #getPersonURL = (id) => `${this.#AppServerBaseURL}/personen/${id}`;
            #deletePersonURL = (id) => `${this.#AppServerBaseURL}/personen/${id}`;

            //Profil related
            #getProfilURL = () => `${this.#AppServerBaseURL}/profil`;
            #addProfilURL = () => `${this.#AppServerBaseURL}/profil`;
            #getProfilURL = (id) => `${this.#AppServerBaseURL}/profil-by-id/${id}`;
            #deleteProfilURL = (id) => `${this.#AppServerBaseURL}/profil/${id}`;

            //Gruppen related
            #getLerngruppenURL = () => `${this.#AppServerBaseURL}/lerngruppen`;

            //Lerndaten related
            #getLerndatenURL = (id) => `${this.#AppServerBaseURL}/lerndaten/${id}`;
            #addLerndatenURL = () => `${this.#AppServerBaseURL}/lerndaten`;
            #deleteLerndatenURL = (id) => `${this.#AppServerBaseURL}/lerndaten/${id}`;

            //Konversation related
            #getKonversationURL = () => `${this.#AppServerBaseURL}/konversation`;
            #addKonversationURL = () => `${this.#AppServerBaseURL}/konversation`;
            #getKonversationURL = (id) => `${this.#AppServerBaseURL}/konversation/${id}`;
            #deleteKonversationURL = (id) => `${this.#AppServerBaseURL}/konversation/${id}`;




"""Person"""
            getPerson() {
              return this.#fetchAdvanced(this.#getPersonURL()).then((responseJSON) => {
                let personenBOs = PersonBO.fromJSON(responseJSON);
                return new Promise(function (resolve) {
                  resolve(personenBOs);
                })
              })
            }

            addPerson(personBO) {
              return this.#fetchAdvanced(this.#addPersonURL(), {
                method: 'POST',
                headers: {
                  'Accept': 'application/json, text/plain',
                  'Content-type': 'application/json',
                },
                body: JSON.stringify(personBO)
              }).then((responseJSON) => {
                let responsePersonBO = PersonBO.fromJSON(responseJSON)[0];
                return new Promise(function (resolve) {
                   resolve(responsePersonBO);
                })
              })
            }


            getPerson(personID) {
              return this.#fetchAdvanced(this.#getPersonURL(personID)).then((responseJSON) => {
                let personBO = PersonBO.fromJSON(responseJSON);
                console.info(personBO);
                return new Promise(function (resolve) {
                  resolve(personBO);
                })
              })
            }


            deletePerson(personID) {
              return this.#fetchAdvanced(this.#deletePersonURL(personID), {
               method: 'DELETE'
              }).then((responseJSON) => {
                let responsePersonBO = PersonBO.fromJSON(responseJSON)[0];
                return new Promise(function (resolve) {
                  resolve(responsePersonBO);
                })
              })
            }

"""Profil"""

            getProfil() {
              return this.#fetchAdvanced(this.#getProfilURL()).then((responseJSON) => {
                let profilBOs = ProfilBO.fromJSON(responseJSON);
                return new Promise(function (resolve) {
                    resolve(profilBO);
                })
              })
            }

            addProfil(profilBO) {
            console.log(profilBO)
               return this.#fetchAdvanced(this.#addProfilURL(), {
                 method: 'POST',
                 headers: {
                  'Accept': 'application/json, text/plain',
                  'Content-type': 'application/json',
                  },
                   body: JSON.stringify(profilBO)
                 }).then((responseJSON) => {
                   let responseProfilBO = ProfilBO.fromJSON(responseJSON);
                   return new Promise(function (resolve) {
                     resolve(responseProfilBO);
                   })
               })
            }

            getProfil(profilID) {
              return this.#fetchAdvanced(this.#getProfilURL(profilID)).then((responseJSON) => {
                let profilBO = ProfilBO.fromJSON(responseJSON);
                console.info(profilBO)
                return new Promise(function (resolve) {
                  resolve(profilBO);
                })
              })
            }

            deleteProfil(profilID) {
              return this.#fetchAdvanced(this.#deleteProfilURL(profilID), {
                method: 'DELETE'
              }).then((responseJSON) => {
                let responseProfilBO = ProfilBO.fromJSON(responseJSON)[0];
                return new Promise(function (resolve) {
                  resolve(responseProfilBO);
                })
              })
            }



"""Gruppen"""

            getLerngruppe() {
              return this.#fetchAdvanced(this.#getLerngruppeURL()).then((responseJSON) => {
                let lerngruppeBO = LerngruppeBO.fromJSON(responseJSON);
                return new Promise(function (resolve) {
                  resolve(LerngruppeBO);
                })
              })
            }


"""Lerndaten"""

            getLerndaten(lerndatenID) {
              return this.#fetchAdvanced(this.#getLerndatenURL(lerndatenID)).then((responseJSON) => {
                let lerndatenBO = LerndatenBO.fromJSON(responseJSON);
                console.info(lerndatenBO);
                return new Promise(function (resolve) {
                  resolve(lerndatenBO);
                })
              })
            }

"""Konversation"""

           getKonversation() {
             return this.#fetchAdvanced(this.#getKonversationURL()).then((responseJSON) => {
                let konversationBO = KonversationBO.fromJSON(responseJSON);
                return new Promise(function (resolve) {
                  resolve(konversationBO);
               })
             })
           }

           addKonversation(konversationBO) {
             return this.#fetchAdvanced(this.#addKonversationURL(), {
               method: 'POST',
               headers: {
               'Accept': 'application/json, text/plain',
               'Content-type': 'application/json',
              },
              body: JSON.stringify(konversationBO)
             }).then((responseJSON) => {
               let responseKonversationBO = KonversationBO.fromJSON(responseJSON);
               console.log(responseKonversationBO);
               return new Promise(function (resolve) {
                resolve(responseKonversationBO);
               })
             })
           }

          getKonversation(id){
            return this.#fetchAdvanced(this.#getKonversationURL(id)).then((responseJSON) => {
              let konversationBO = KonversationBO.fromJSON(responseJSON);
              return new Promise(function (resolve){
                resolve(konversationBO)
              })
            })
          }

          deleteKonversation(id) {
            return this.#fetchAdvanced(this.#deleteKonversationURL(id), {
              method: 'DELETE'
            }).then((responseJSON) => {
            let responseKonversationBO = KonversationBO.fromJSON(responseJSON)[0];
                return new Promise(function (resolve) {
                  resolve(responseKonversationBO);
                })
            })
          }





