import os
os.getcwd()
'c:\\'

def get_words(my_file = u"C:\\Users\\COMU\\Documents\\data.txt"):
my_list = []
f= open(my_file, "r+")
contents = f.readlines()
for line in content:
    # sprint(line)
    # bosluga gore pars etme
    words = line.split(" ")
    for word in words:
        # print(word)
        my_list.append(word)
# print(contents)

f.close()
return my_list

len(my_list)

#histogram
def get_hist(my_list):
my_hist = {} 
for w in my_list:
    if w in my_hist.keys():
        my_hist[w] = my_hist[w] + 1
    else:
        my_hist[w] = 1
    return my_hist

def get_files(path_1):
    file_s = [file for file in my_list if os.path.isfile(item) ]
    return file_s

#cagirma
lst_1 = get_words()
get_hist(lst_1)

#sadece filelar gelecek
from os 
my_list = os.listdir()

for item in my_list:
    if os.path.isfile(item):
        print(item)
for item in my_list:
    if os.path.isdir(item):
        print(item)

#bulundugum yerdeki aktif klasorleri gosterir
dir_s = [dir for dir in my_list if os.path.isdir(item) ]
#bulundugu yerdeki aktif filelari gosterir
file_s = [file for file in my_list if os.path.isfile(item) ]

dir_s, file_s