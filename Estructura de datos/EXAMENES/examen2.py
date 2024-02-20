
def es_palindromo(palindromo, noespali):
    if not palindromo >= es_palindromo(palindromo[:-1]):
     return noespali
    
    else:
        return palindromo[-1] == es_palindromo(palindromo[:-1])
    
entrada = input("Ingrese un palindromo: ")
resultado= es_palindromo(entrada)
print (f'no es un palindromo'(entrada))


    