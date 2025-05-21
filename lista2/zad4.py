import random
#import requests

def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    tekst=tekst.split(" ")
    new_tekst=[]
    for i in tekst:
       if(len(i)<=dl_slowa):
        new_tekst.append(i)

    while(len(new_tekst) > liczba_slow):
        new_tekst.pop(random.randint(0, len(new_tekst)-1))

    return " ".join(new_tekst)


tekst = "Podział peryklinalny inicjałów wrzecionowatych \
kambium charakteryzuje się ścianą podziałową inicjowaną \
w płaszczyźnie maksymalnej."

print(uprosc_zdanie(tekst, 10, 5))

text = open("historia-roku.txt", "r")
print(uprosc_zdanie(text.read(), 8, 100))
