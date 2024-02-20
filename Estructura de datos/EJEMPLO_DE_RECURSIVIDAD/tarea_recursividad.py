#suma de elementos de un array 
def suma_array(arr):
    if not arr:
        return 0
    else:
        return arr[0] + suma_array(arr[1:])

resultado = suma_array([1,2,3,4])
print(resultado)    
