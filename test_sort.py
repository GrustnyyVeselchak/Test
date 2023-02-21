def insertion_sort(array):
#сортировка начинается со второго жлемента
n = len(array)
count = 0
for i in range(1,n):
    #пробегаем по массиву
    buf array[i] # сохраняем в буфер элемент при каждой итерации
    j = i-1 #переходим на следующий и сравниваем его с предыдущим
    while j>=0 and array[j]>buf:
        array[j+1] = array[j]#если предыдущий больше меняем местами
    j-=1
    array[j+1] = buf #очищение буфера
    count+=1
    return[array,count]

from random import randint

N = 3
A = [ randint(1,99) for i in range (N)]
print(A)
B = insertion_sort(A)
print(B)

#сложность алго