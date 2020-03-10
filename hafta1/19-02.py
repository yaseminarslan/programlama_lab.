#19.02.20
#bir sayının istenen bir kuvvetini veren fonksiyon

def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)
print (power(4, 3))

#recursive vesiyonu
def power1(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        if b % 2 == 0:
            return power1(a*a, b//2)
        else:
            return power1(a*a, b//2) * a
        #return a * power1(a, b-1)
print (power1(5, 3))

#verilen bir listedeki ardisik sayilarin en buyuk toplamini bulan fonksiyon
liste_1=[4,-3,5,-2,-1,2,6,-2]
max = 0
for i in range(8):
    for j in range(i, 8):
        t=0
        for k in range(i, j):
            t = t + liste_1[k]
    if max < t:
        max = t
        #i_a max toplamin baslangic indeksi
        #i_b max toplamin bitis indeksi
        i_a, i_b = i,j
print(max, i_a, i_b)