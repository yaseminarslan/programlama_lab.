# min heap: parent node degeri, child node degerinden ya kucuk yada child node degerine esittir.
def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)

def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)

my_array_1  = [8,10,3,4,7,15,1,2,16]
print(build_min_heap(my_array_1))
print(my_array_1)

# heapsort, dizi sıralamak için kullanılır.
def heapsort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array

my_array_1  = [8, 10, 3, 4, 7, 15, 1, 2, 16]
my_array_2  = heapsort(my_array_1)
print(my_array_1,  my_array_2)


# diziye gonderilen degeri ekler.

def insertItemToHeap(myheap_1, item):
    for i in range(len(myheap_1)):
        if myheap_1[i] == item:
            print("listeye yeni eleman eklenemedi")
            return myheap_1
    myheap_1.append(item)
    build_min_heap(myheap_1)
    return myheap_1

print(insertItemToHeap(my_array_1, 26))

# dizinin en kucuk elemanini siler ve siralanmis halini yazdirir.
def removeItemFrom(myheap_1):
    array_2 = heapsort(myheap_1)
    print("dizi", array_2)
    array_2.pop(0)
    build_min_heap(array_2)
    return array_2

print("ilk elemani silinmiş dizi", removeItemFrom(my_array_1))

#En küçük elemanı siliniyor

# def removeitemFrom(my_heap):
#     array_2 = heapsort(my_heap)
#     array_2[0], array_2[-1] = array_2[-1], array_2[0]
#     array_2.pop()
#     build_min_heap(array_2)
#     return array_2