import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'capitalizado'
})
export class CapitalizadoPipe implements PipeTransform {

  transform(value: string, ...args: unknown[]): string {
    value = value.toLocaleLowerCase();
    let nombres = value.split(' ');
    nombres = nombres.map(nombre => nombre[0].toLocaleUpperCase() + nombre.substr(1));
    return nombres.join(' ');
  }

}
