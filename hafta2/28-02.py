#28.02.20

# Bir diziyi ikiye bolduk.
# Unsorted'i sıraladiktan sonra en buyuk terim sorted'a aktarıldi.

#Insertion Short 


def insertionShort(arr) :
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0) and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
print(insertionShort(arr=[5,6,2,9,1,7,3]))
        
# Shell Short
def ShellSort(array=[4, 3, 2, 1]):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j = j - gap
            array[j] = temp
        # aralık değerlerini yariya indirdi.
        gap //= 2
    return array