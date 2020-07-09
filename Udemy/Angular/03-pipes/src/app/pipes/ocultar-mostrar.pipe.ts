import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'ocultarMostrar'
})
export class OcultarMostrarPipe implements PipeTransform {

  transform(value: string, mostrar: boolean): string {
    if (mostrar){
      return value;
    }else{
      return '*'.repeat(value.length);
    }
  }

}
