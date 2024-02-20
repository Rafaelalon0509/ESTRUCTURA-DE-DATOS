def revertir_cadena(cadena):
    # Caso base: cuando la cadena es vacía.
    if not cadena:
        return cadena
    # Caso recursivo: invertir la cadena excluyendo el último carácter.
    else:
        return cadena[-1] + revertir_cadena(cadena[:-1])

# Ejemplo de uso
entrada = input("Ingrese una cadena: ")
resultado = revertir_cadena(entrada)
print(f"La cadena invertida es: {resultado}")