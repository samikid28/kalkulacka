def scitaj(cislo1, cislo2):
    
    return cislo1+cislo2

def odcitaj(cislo1, cislo2):
  return cislo1-cislo2

def vynasob(cislo1, cislo2):
  return cislo1*cislo2

def vydel(cislo1, cislo2):
    if cislo2==0:
        print("Nedá sa deliť nulou")
    else: 
        return cislo1/cislo2
print("Ak chces scitat napis 1")
print("Ak chces odcitat napis 2")
print("Ak chces vynasobit napis 3")
print("Ak chces vydelit napis 4")
      

value = int(input(" Ktoru operaciu chceš vykonať1/2/3/4: "))
cislo1=int(input("Zadaj 1. cislo:"))
cislo2=int(input("Zadaj 2. cislo:"))

if value==1:
  print("Scitanie cisel", scitaj(cislo1, cislo2))
 
if value ==2:
    print("Odcitanie cislel", odcitaj(cislo1, cislo2))

if value==3:
    print("Vynasobenie cisel", vynasob(cislo1, cislo2))

if value ==4:
    print("Vydelenie cisel", vydel(cislo1, cislo2))
