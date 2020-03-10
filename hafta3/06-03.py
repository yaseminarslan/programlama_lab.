#06.03.20

#TT YY space, TY YT event

from sympy import FiniteSet

t = FiniteSet(1,2,3)
s = FiniteSet(2,4,6)
if t == s:
    print("True")
else:
    print("False")
print(t.union(s))
print(t.intersect(s))
print(t**2) 

# space örneklem uzayını belirtir, event ise belirli bir olayı belirtir.

def probability(space, event):
    return len(event)/len(space)

#asal mi
def check_primes(number):
    if number != 1:
        for factor in range (2, number):
            if number%factor == 0:
                return False
    else:
        return False

    return True

# * icerideki degerleri tek tek alip virgulle birlestirip gonderen bir yapi
space = FiniteSet(*range(1,21))
# append fonksiyonu icin 35.satir zorunlu. baslangic degeri vermek icin /initialize
primes = []
for num in space:
#her bir deger icin primes olup olmadigina bakacak
    if check_primes(num):
        primes.append(num)
    event = FiniteSet(*primes)
    p = probability(space, event)
    print(p)


file1 = open("my_f.txt", "r")
file1.readlines()
content = file1.readlines()
print(content)

for line in content :
    for item in line:
        print(item)