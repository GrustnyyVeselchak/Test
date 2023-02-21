def perebor_sort(array):
    n = len(array)
    for i in range(0, n-1):
        k = i
        for j in range (i + 1, n):
            if array[j] < array [k]:
                k = j
                array[i],array[k] = array[k],array[i]#
    return array
    
array = [15,30,4]
b = perebor_sort(array)
print(b)