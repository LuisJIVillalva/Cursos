(function () {
    let miFuncion = function( a: String){
        return a.toUpperCase();
    }

    const miFuncionF = (a: String)=> a.toUpperCase();
    
    const sumarN = function (a:number, b:number) {
        return a +b;
    }

    const sumarNF = (a:number, b:number)=> a+b;

    const hulk = {
        nombre: 'Hulk',
        smash(){

            setTimeout(()=>{
                console.log(`${this.nombre} smash!!!`)
                
            }, 1000);
        }
    }

    hulk.smash();
    console.log(miFuncion('Normal'))
    console.log(miFuncionF('Normal'))
    console.log(sumarN(1,2))
    console.log(sumarNF(1,2))
})();