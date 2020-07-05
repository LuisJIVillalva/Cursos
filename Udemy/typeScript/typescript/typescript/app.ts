(()=>{
    const sumar = (a: number,b: number):number => a+b;

    const nombre = ():string=> 'Hola Fernando';
    
    const obtenerSalario = ():Promise<String> => {
        return new Promise( (resolve, reject)=>{
            resolve('Fernando');

        });
    }

    obtenerSalario().then(a => console.log(a.toUpperCase()))

})();