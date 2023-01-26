class Balaton:
    def __init__(self, település, fekvés, lakosság):
        self.település = település
        self.fekvés = fekvés
        self.lakosság= lakosság
    def fekv(self):
        if self.fekvés =='é':
            return 'északi parti'
        elif self.fekvés =='d':
            return 'déli parti' 
    def lakos(self):
        if self.lakosság >= 10000:
            return 'város'
        elif self.lakosság >= 5000:
            return 'nagyközség'
        else:
            return 'falu'
        
lista=[]
for _ in range(2):
    telepnev=input('Add meg egy település nevét! ')
    hely=input('Add meg a fekvése (északi vagy déli(é/d))! ')
    szam=int(input('Add meg a lakosság számát! '))
    lista2 = Balaton(telepnev,hely,szam)
    lista.append(lista2)
for listak in lista:
    print(listak.település,'egy',listak.fekv(),listak.lakos(),',', szam,'fővel.')