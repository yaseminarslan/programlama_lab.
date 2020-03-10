#21.02.20

# Selection sort
def Selection(list1=[7, 6, 8, 9, 3, 2, 10, 5, 1]):
    n = len(list1)
    swaps, comparison = 0, 0
    for key in range(n-1):
        for i in range(key+1,n):
            comparison += 1
            if list1[i] < list1[key]:
                swaps += 1
                list1[i], list1[key] = list1[key], list1[i]

# Bubble sort 
def Bubble(list1=[7, 6, 8, 9, 3, 2, 10, 5, 1]):
    n = len(list1)
    swaps, comparison = 0, 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparison += 1
            if list1[j] > list1[j+1]:
                swaps += 1
                list1[j], list1[j+1] = list1[j+1], list1[j]