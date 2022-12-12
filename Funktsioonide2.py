from math import *
from random import *
#1
print("")
print("Puu läbimõõdu arvutamine")
C = float(input("mis on ümbermõõt: "))
d = C / pi 
print("Puu läbimõõt: ",round(d,2))
#2
print("")
print("pikk on ristkülikukujulise maatüki diagonaal")
N = float(input("Sisestage number N: "))
M = float(input("Sisestage number M:"))
d = sqrt(N**2+M**2)
print(" pikk on ristkülikukujulise maatüki diagonaal", round(d,2), "m")
#3
print("")
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print("Sinu kiirus oli " + str(kiirus) + " km/h")
#4
print("")
firstNum = int(input("First number: "))
secondNum = int(input("Second number: "))
thirdNum = int(input("Third number: "))
fourthNum = int(input("Fourth number: "))
fifthNum = int(input("Fifth number: "))
average = (firstNum+secondNum+thirdNum+fourthNum+fifthNum)/5
print(average)
#5
print("")
print('   @..@\n  (----)\n ( \__/ )\n^^ "" ^^')
#6
print("")
a = float(input("sisestage esimene pool: "))
b = float(input("sisestage teise pool: "))
c = float(input("sisestage kolmas pool: "))
print(a+b+c)
#7
print("")
friend = int(input("kui palju sõpru? "))
hind = float(input("kui palju on pizza? "))/friend
protsent = float(input("protsent? "))
allahindlust = hind*protsent/100
total = allahindlust+hind
print("total hind: ", round(total,2))
#random #6
print("")
a = randint(0,100)
b = randint(0,100)
c = randint(0,100)
print(f"a={a}\n,b={b}\n,c={c}")
#8
print("")
läbitudVahemaa = float(input("läbitud vahemaa: "))
täidetudKütuseKogus = float(input("täidetud kütuse kogus: "))
kütust = täidetudKütuseKogus/läbitudVahemaa*100
print(kütust,"km/l")
#9
print("")
killometr = float(input("teie kiirus km/h: "))
total = killometr*1000/60
print("keskmine kiirus:", round(total,2),"m/m")
#10
print("")
M = int(input("sisestage minutid: "))
H = M//60
M =M%60
print(f"{H}:{M}")