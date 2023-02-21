from random import randint

N = 10 #размер массива

A = [ randint(1,99) for i in range (N)]
print(A)

def selection_sort(N):
    for i in range(N):
        k = i # Начальное значение индекса минимального элемента
        for j in range(i+1, n):
            if array[j] < array[k]:
            k = j
            array[i], array[k] = array[k], array[i] # Минимальный элемент меняем с i-м элементом