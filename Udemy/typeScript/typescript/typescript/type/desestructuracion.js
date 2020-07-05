"use strict";
(function () {
    var avenger = {
        nombre: 'Steve',
        clave: 'Capitán América',
        poder: 'Droga'
    };
    var extraer = function (_a) {
        var nombre = _a.nombre, clave = _a.clave;
        console.log(nombre + " " + clave);
    };
    extraer(avenger);
    var avengers = ['thor', 'Ironman', 'Spiderman'];
    var extraerA = function (_a) {
        var loki = _a[0], hombre = _a[1], arana = _a[2];
        console.log(loki);
        console.log(hombre);
        console.log(arana);
    };
    extraerA(avengers);
})();
