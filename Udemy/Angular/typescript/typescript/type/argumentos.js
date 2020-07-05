"use strict";
(function () {
    function activar(quien, //obligatorio                
    momento, //opcional
    objeto //por defecto
    ) {
        if (objeto === void 0) { objeto = 'Syndra'; }
        if (!momento) {
            console.log(quien + " la rompe con " + objeto);
        }
        else {
            console.log(quien + " " + momento + " la rompe con " + objeto);
        }
    }
    activar("Cratospool", "siempre", "Jhin");
})();
