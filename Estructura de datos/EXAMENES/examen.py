def funcionMisteriosa(n):
    #el caso base es hacer que la funcion sume en secuencia los numeros y el resultado sume al siguiente 
    #es decir 1+2 = 3 y a este sumarle el numero 3  y asi sucesivamente  
    if n <=0:

        return 0
    return n + funcionMisteriosa (n-1)

print(funcionMisteriosa(5))
#aqui mostrara como resultado el numero 15 ya que 1+2= 3 +3 = 6 +4= 10 +5=15