// src/sum.ts

/**
 * Función TypeScript profesional para sumar dos números.
 * @param a El primer número a sumar.
 * @param b El segundo número a sumar.
 * @returns El resultado de la suma.
 */
export function sum(a: number, b: number): number {
  return a + b;
}

// Ejemplo de uso
const result: number = sum(120, 45);
console.log(`El resultado de la suma (120 + 45) es: ${result}`);

/**
 * Función TypeScript profesional para restar dos números.
 * @param a El minuendo (el número al que se le resta).
 * @param b El sustraendo (el número que resta).
 * @returns El resultado de la resta.
 */
export function subtract(a: number, b: number): number {
  return a - b;
}