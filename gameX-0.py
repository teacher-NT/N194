from random import choice
import os
os.system("cls")

def bosh_doska_hosil_qil():
   return [
       '1','2','3','4','5','6','7','8','9'
   ]
    
def doskani_korsat(doska):
    start = 0
    end = 3
    print("-------------")
    for i in range(3):
        print("|"," | ".join(doska[start:end]), "|")
        print("-------------")
        start += 3
        end  += 3

def foydalanuvchi_tanlasin(doska):
    while True:
        foy = input("Sizni galiniz: ")
        if foy in doska:
            index = doska.index(foy)
            doska[index] = 'O'
            break
        else:
            print("Iltimos bo'sh katakni tanlang!")

def bosh_maydonlar(doska):
    free = []
    for i in doska:
        if i != 'O' and i != 'X':
            free.append(i)
    return free
        
def golib_bormi(doska, belgi):
    if doska[0] == belgi and doska[1]==belgi and doska[2]==belgi:
        return True
    elif doska[0] == belgi and doska[3] == belgi and doska[6] == belgi:
        return True 
    elif doska[0] == belgi and doska[4] == belgi and doska[8] == belgi:
        return True 
    elif doska[1] == belgi and doska[4] == belgi and doska[7] == belgi :
        return True
    elif doska[2] == belgi and doska[5] == belgi and doska[8] == belgi :
        return True
    elif doska[3] == belgi and doska[4] == belgi and doska[5] == belgi :
        return True
    elif doska[6] == belgi and doska[7] == belgi and doska[8] == belgi :
        return True
    elif doska[2] == belgi and doska[4] == belgi and doska[6] == belgi :
        return True
    else:
        return False

def kompyuter_tanlasin(doska):
    free = bosh_maydonlar((doska))
    if not free:
        return
    ch = choice(free)
    index = doska.index(ch)
    doska[index] = 'X'

doska = bosh_doska_hosil_qil()
while bosh_maydonlar(doska):
    doskani_korsat(doska)
    foydalanuvchi_tanlasin(doska)
    if golib_bormi(doska, 'O'):
        print("Siz g'olib bo'ldingiz!!!")
        break
    kompyuter_tanlasin(doska)
    if golib_bormi(doska, 'X'):
        doskani_korsat(doska)
        print("Kompyuter yutdi!!!")
        break
    os.system("cls")
else:
    print("G'olib aniqlanmadi...")




