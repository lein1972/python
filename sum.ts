// sum.ts (Modificando la función existente 'sum')

/**
 * Función TypeScript profesional para sumar TRES números.
 * Se modificó para simular un futuro conflicto.
 * * @param a El primer número.
 * @param b El segundo número.
 * @param c El tercer número.
 * @returns El resultado de la suma de a, b y c.
 */
export function sum(a: number, b: number, c: number): number {
  return a + b + c; // CAMBIO CLAVE: se añade 'c'
}


/**
 * Función TypeScript profesional para restar dos números.
 * (Se mantiene la función 'subtract' sin cambios).
 * ...
 */
export function subtract(a: number, b: number): number {
  return a - b;
}


// Ejemplo de uso (actualizado)
const resultSum: number = sum(100, 50, 20); // Ahora se necesitan tres argumentos
console.log(`El resultado de la nueva suma (100 + 50 + 20) es: ${resultSum}`);

const resultSub: number = subtract(120, 45);
console.log(`El resultado de la resta (120 - 45) es: ${resultSub}`);





