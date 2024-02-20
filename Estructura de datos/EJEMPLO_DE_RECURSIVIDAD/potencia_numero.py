def potencia(base, exponente):
    # Caso base: cuando el exponente es 0, la potencia es 1.
    if exponente == 0:
        return 1
    # Caso recursivo: multiplicar la base por la potencia con exponente reducido.
    else:
        return base * potencia(base, exponente - 1)

# Ejemplo de uso
base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero no negativo): "))

if exponente < 0:
    print("El exponente debe ser un entero no negativo.")
else:
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es igual a: {resultado}")
