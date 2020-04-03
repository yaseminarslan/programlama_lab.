#01.04.20

# video1****


#generate list with n items

import random
random.random()
s=random.randint(1,100)
print(s)


def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range (n):
        numbers.append(random.randint(min_,max_))
    return numbers
print(get_n_random_numbers())
print(get_n_random_numbers(12,-100,50))

my_list=get_n_random_numbers(15,-4,4)

#histogram with two methods

print(sorted(my_list))

def my_frequency_with_dict(list):
    frequency_dict={} #dict()={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict
print(my_frequency_with_dict(my_list))


# ayni islev farkli format

def my_frequency_with_list_of_tuples(list_1):
    frequency_list=[]
    for i in range (len(list_1)):
        s=False
        for j in range (len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])
    return frequency_list


my_list=[2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4,4]
result_1=my_frequency_with_dict(my_list)
result_2=my_frequency_with_list_of_tuples(my_list)
print(result_1,result_2)

# video2****

# mode of a list with histogram

my_list_1=get_n_random_numbers(5,-2,2)
my_hist_d=my_frequency_with_dict(my_list_1)
my_hist_l=my_frequency_with_list_of_tuples(my_list_1)
print(my_hist_d,my_hist_l)


# to get mode, we have to search all keys on hist_dict
frequency_max=-1 
#mode dongude, karsilastirilacak hafiza amacli deger.
mode=-1
for key in my_hist_d.keys():
    #print(key,my_hist_d[key])
    if my_hist_d[key]>frequency_max:
        frequency_max=my_hist_d[key]
        mode=key
print(my_hist_d)        
print(frequency_max,mode)


# to get mode, we have to search all keys on hist_dict
def my_mode_with_dict(my_hist_d):
    frequency_max=-1 
#mode dongude, karsilastirilacak hafiza amacli deger.
    mode=-1
    for key in my_hist_d.keys():
        #print(key,my_hist_d[key])
        if my_hist_d[key]>frequency_max:
            frequency_max=my_hist_d[key]
            mode=key        
    return mode,frequency_max
print(my_mode_with_dict(my_hist_d))

my_list_100=get_n_random_numbers(100,-40,40)
my_hist_1=my_frequency_with_dict(my_list_100)
print(my_mode_with_dict(my_hist_1))
print(sorted(my_list_100))



# mode of a list with histogram(a list of tuples)

my_list_1=get_n_random_numbers(10)
my_hist_list=my_frequency_with_list_of_tuples(my_list_1)
print(my_hist_list)

# to get mode, we have to search all keys on hist_dict
frequency_max=-1 
#mode degeri dongude karsilastirilacak hafiza amacli deger.
mode=-1
for item,frequency in my_hist_list:
    print(item,frequency)
    if frequency>frequency_max:
        frequency_max=frequency
        mode=item
print(my_hist_list)        
print(mode,frequency_max)

# to get mode, we have to search all keys on hist_dict
def my_mode_with_list(my_hist_list):
    frequency_max=-1 
#mode degeri dongude karsilastirilacak hafiza amacli deger.
    mode=-1
    for item,frequency in my_hist_list:
        print(item,frequency)
        if frequency>frequency_max:
            frequency_max=frequency
            mode=item        
    return mode,frequency_max
print (my_mode_with_list(my_hist_list))

my_list_100=get_n_random_numbers(20,-4,4)
my_hist_1=my_frequency_with_list_of_tuples(my_list_100)
my_mode_with_list(my_hist_1)

#linear search on list

def my_linear_search(my_list,item_search):
    found=(-1,-1) # default eğer listede yoksa
    for indis in range (n):
        if my_list[indis]==item_search:
            found=(my_list[indis],indis)# Listede Bulundu, return bulunan sayı , indisi tuple olarak return edilir.
            #break, uncomment for last found
    return found
my_list=get_n_random_numbers(10,-5,5)
print(my_linear_search(my_list,3))



#mean of list

my_list=get_n_random_numbers(10,-50,50)
print(my_list)
s,t=0,0
for item in my_list:
    s=s+1
    t=t+item
mean=t/s
print(mean)


# video3****


#sort the list
n=len(my_list)
#print(my_list)
for i in range(n-1,-1,-1):
    for j in range (0,i):
        if not(my_list[j]<my_list[j+1]):
            #print("swap islemi")
            temp=my_list[j]
            my_list[j]=my_list[j+1]
            my_list[j+1]=temp
print(my_list)

def bubble_sort(my_list):
    n=len(my_list)
    print(my_list)
    for i in range(n-1,-1,-1):
        for j in range (0,i):
            if not(my_list[j]<my_list[j+1]):
                #print("swap islemi")
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp    

    return my_list
print(bubble_sort(my_list))



#binary search on a sorted list
def my_binary_search(my_list,item_search):
    found=(-1,-1)
    low = 0
    high = len(my_list)-1
    
    while low <=high:
        mid=(low+high)//2
        if my_list[mid]==item_search:
            return my_list[mid],mid
        elif my_list[mid]>item_search:
            high = mid -1
        else:
            low = mid+1
    return found #none
my_list_1=get_n_random_numbers(10)
print("liste",my_list_1)
my_list_2=bubble_sort(my_list_1)
print("Sirali liste",my_list_2)
print(my_binary_search(my_list_2,3))


#median of a list

size=input("Dizi Boyutunu Giriniz : ")
size=int(size) #convert str to int 
my_list_1=get_n_random_numbers(size)
print("liste ",my_list_1)

my_list_2=bubble_sort(my_list_1)

print(my_list_2)
n=len(my_list_2)
if n%2==1:
    middle=int(n/2)+1
    median=my_list_2[middle]
    print(median)
else:
    middle_1=my_list_2[int(n/2)-1]
    middle_2=my_list_2[int(n/2)]
    median=(middle_1+middle_2)/2
    print(median)
    
    def my_median(my_list):
    my_list_2=bubble_sort(my_list_1)
    
    #print(my_list_2)
    n=len(my_list_2)
    if n%2==1:
        middle=int(n/2)
        median=my_list_2[middle]
    else:
        middle_1=my_list_2[int(n/2)-1]
        middle_2=my_list_2[int(n/2)]
        median=(middle_1+middle_2)/2
    return median

print (my_median(my_list_1))
