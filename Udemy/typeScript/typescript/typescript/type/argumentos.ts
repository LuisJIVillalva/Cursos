(function () {
    function activar(quien   :string,//obligatorio                
                     momento?:string,//opcional
                     objeto  :string='Syndra'//por defecto
                    ) {
        
        if (!momento){
            console.log(`${quien} la rompe con ${objeto}`)
        }else{
            console.log(`${quien} ${momento} la rompe con ${objeto}`)
        }
    }

    activar("Cratospool","siempre","Jhin");
})();