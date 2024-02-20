#medir tiemo de ejecucion de algoritmos python 

import time 

#algoritmo 1 - bubble sort
start_time = time.time()
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            print(arr[i],arr[j])
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
#Ejemplo de uso: (lista desordenada 1)
lista_desorndenada1 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lista_desorndenada1)
print("Lista ordenada usando Bubble Sort: ", lista_desorndenada1)

tiempo_ejecucion_final = time.time() - start_time
print(f"tiempo de ejecucion de algoritmo 1: {tiempo_ejecucion_final} segundos")

#algoritmo 2 - quicksort
start_time2 = time.time()
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    privot = arr[len(arr)// 2]
    left = [x for x in arr if x < privot]
    middle = [x for x in arr if x == privot]
    right = [x for x in arr if x > privot]
    return quicksort(left) + middle + quicksort(right)
#Ejemplo de uso: (lista desordenada 2)
lista_desorndenada2 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lista_desorndenada2)
print("Lista ordenada usando QuickSort: ", lista_desorndenada2)

tiempo_ejecucion_final2 = float(time.time() - start_time2)
print(f"tiempo de ejecicion del algoritmo 2: {tiempo_ejecucion_final2} segundos")