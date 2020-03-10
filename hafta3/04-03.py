#04.03.20

def lookup (d, v):
    for k in d:
        if d[k] == v:
            return k


known = {0:0, 1:1}
def fibo_rec(n):
    if n < 2:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)
    if n in known:
        return known[n]
    else:
        result = fibo_rec(n-1) + fibo_rec(n-2)
        known[n] = result
        return result


list_1=[1,4,7,84,3,62,23]

my_d=dict()
my_d=(1:'bir', 2:2, '3' : 'three')
for key in my_d.keys():
    print(key,my_d[key])
    
    # 5 in my_d   false geldı. 5 yerine 1 yaz true geldi.
    if -10 not in my_d:
        my_d[-10]=50
    my_d
    
    
    def my_h(list_1):
        my_d={}
        for item in list_1:
            if item not in my_d:
                my_d[item]=item+1
                return my_d
            print(my_h([2,3,4,6,2,5,6,6,6,6,6,6,6,2]))
            
            
     def lookup(d,v):
         for key in d:
             if d[key]==v:
                 return key
             else:
                 return -1
             
                lookup(my_d,2)