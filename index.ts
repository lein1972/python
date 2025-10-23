// index.ts

// Importamos la función 'add' desde el módulo que acabamos de crear.
import { add } from './src/calculator';

const num1: number = 25;
const num2: number = 17;

console.log(`\n--- Test de Funcionalidad ---\n`);
console.log(`La suma de ${num1} y ${num2} es: ${add(num1, num2)}`);
console.log(`\n-----------------------------\n`);