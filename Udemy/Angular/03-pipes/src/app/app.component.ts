import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
      nombre: string = 'Cratospool';
      nombre2: string = 'CraTosPool lUis JuAn';
          PI: number = Math.PI;
  porcentaje: number = 0.23658;
     arreglo: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
     salario: number = 12354
       fecha: Date = new Date(2020, 0);
     activar: boolean = true;

     valorPromesa = new Promise<string>((resolve) => {
      setTimeout(() => {
          resolve('llego la data');
      }, 4500);

     });

     idioma = 'en';
     videourl: string ='https://www.youtube.com/embed/HZcyanmm4gc';

     heroe = {
       nombre: 'Logan',
       clave: 'Wolverine',
       edad: 500,
       direccion: {
         calle: 'Primera',
         casa: 20
        }
      };

      cambiarIdioma(idioma: string): void{
        this.idioma = idioma;
      }
    }
