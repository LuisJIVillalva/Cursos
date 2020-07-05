"use strict";
(() => {
    const avenger = {
        nombre: 'Steve',
        clave: 'Capitán América',
        poder: 'Droga'
    }

    const extraer = ({ nombre, clave }:any) => {
        console.log(`${nombre} ${clave}`)
    }

    extraer(avenger);


    const avengers: string[] = ['thor', 'Ironman', 'Spiderman'];

    const extraerA = ([loki, hombre, arana]:String[]) =>{
    console.log(loki)
    console.log(hombre)
    console.log(arana)
    }
    extraerA(avengers)
})();