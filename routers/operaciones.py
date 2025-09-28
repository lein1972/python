def sumar(a, b):
    """Esta función suma dos números y devuelve el resultado."""

    return a + b + 10


# Definir los números pares
num1 = 100
num2 = 2

# Llamar a la función y mostrar el resultado
resultado = sumar(num1, num2)
print(f"La suma de {num1} y {num2} es {resultado}")

def restar(a, b):
    """
    Esta función toma dos números (a y b) y devuelve el resultado de a - b.
    """
    return a - b

# --- Ejemplo de uso ---

# Definir los números
numero1 = 10
numero2 = 4

# Llamar a la función
resultado = restar(numero1, numero2)

# Imprimir el resultado
print(f"La resta de {numero1} menos {numero2} es: {resultado}")

def multiplicar_numeros(a, b):
  """Esta función multiplica dos números y devuelve el resultado."""
  return a * b

# Ejemplo de uso
n1 = 6
n2 = 7
resultado_mult = multiplicar_numeros(n1, n2)
print(f"La multiplicación de {n1} por {n2} es: {resultado_mult}")
