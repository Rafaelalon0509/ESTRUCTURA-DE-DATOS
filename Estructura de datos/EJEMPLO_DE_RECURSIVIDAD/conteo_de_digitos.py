def contar_digitos(numero):
    # Caso base: cuando el número tiene un solo dígito.
    if numero < 10:
        return 1
    # Caso recursivo: contar un dígito y llamar recursivamente con el número reducido.
    else:
        return 1 + contar_digitos(numero // 10)

# Ejemplo de uso
numero = int(input("Ingrese un número entero: "))
resultado = contar_digitos(numero)
print(f"El número de dígitos en {numero} es: {resultado}")
