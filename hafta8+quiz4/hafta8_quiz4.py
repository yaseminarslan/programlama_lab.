# min heap: parent node degeri, child node degerinden ya kucuk yada child node degerine esittir.
#parametre olarak bir dizi alir
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

# parametre olarak gonderilen dizideki tum elemanlar min_heapify fonksiyonuna gonderilir.
def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)

my_array_1  = [8,10,3,4,7,15,1,2,16]
print(build_min_heap(my_array_1))
print(my_array_1)

# heapsort, dizi siralamak icin kullanilir.
# gonderilen dizideki kok ile son elemanın yeri degisir. 
# son eleman yeni listeye eklenir. eski listeden silinir
# liste kucukten buyuge siralanir.
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


#parametre olarak gonderilen diziye, parametre olarak gonderilen degeri ekler
def insertItemToHeap(myheap_1, item):
    for i in range(len(myheap_1)):
        #gonderdigimiz elemanin listede olup olmadigini kontrol ediyor .
        if myheap_1[i] == item:
            print("listeye yeni eleman eklenemedi")
            # listede oldugu icin ekleme yapilmiyor.
            return myheap_1
    myheap_1.append(item)
    build_min_heap(myheap_1)
    return myheap_1

print(insertItemToHeap(my_array_1, 26))

# dizinin en kucuk elemanini siler ve siralanmis halini yazdirir.
def removeItemFrom(myheap_1):
    # dizi siralanir.
    array_2 = heapsort(myheap_1)
    print("dizi", array_2)
    array_2[0], array_2[-1] = array_2[-1], array_2[0]
    # en kucuk eleman siliniyor.
    array_2.pop() 
    build_min_heap(array_2)
    return array_2

print("ilk elemani silinmis dizi", removeItemFrom(my_array_1))
