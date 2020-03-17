#Kupujem prodajem - Polovni racunari

# class adPrice - cena
# class adName - ime
# class locationSec - mesto
import bs4
import requests

karakteri = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMčČćĆšŠđĐžŽ- . ,0123456789,€dinKontakt Kupujem Pozvati Novo"

class Predmet:
    def __init__(self, imeKlase, karakteriZaFilter,brojStrana):
        self.imeKlase = imeKlase
        self.karakteriZaFilter = karakteriZaFilter
        self.brojStrana = brojStrana
     

    def Lista(self):#vraca listu (ime,cena,lokacija....)
        lista = []
        listaFinal =[]
        for i in range(1,3):
            url = "https://www.kupujemprodajem.com/Kompjuteri-Desktop/Polovni-kompjuteri/10-98-" + str(i)+"-grupa.htm"
            res = requests.get(url)
            soup = bs4.BeautifulSoup(res.text , "lxml")
            for i in soup.select("."+self.imeKlase):
                podatak = i.text
                lista.append(str(podatak))
            for j in lista:
                if(j != "Mesto/Grad"):
                    listaFinal.append(''.join(c for c in j if c in self.karakteriZaFilter))
        return listaFinal

def FilterCena(cenaLista):#bes decimalnih vrednosti samo cena i valuta
    cenaFilter=[]
    for i in cenaLista:
        string = ""
        prekidac = True
        for j in i:
            if (j != "," and prekidac == True):
                string += j
            elif(j == ","):
                prekidac = False
                
        if("€" in i):
            string += "€"
            
        cenaFilter.append(string)
    return cenaFilter

def FilterCenaINT(cenaLista):#pretvaramo cene u int
    ceneINT = []
    for i in cenaLista:
        a = ''.join(c for c in i if c in "1234567890")
        ceneINT.append(int(a))
    print(ceneINT)
    
        

brojStrana = 4# koliko strana zelimo da program preuzme

p1 = Predmet("adName" , karakteri, brojStrana)
p2 = Predmet("adPrice" , karakteri, brojStrana)
p3 = Predmet("locationSec" , karakteri, brojStrana)

ime = p1.Lista()
cena = p2.Lista()
mesto = p3.Lista()


#recnik sa nazivom,cenom i lokacijom
racunari = {}

for i in range(1,len(p1.Lista())):
    racunari.update({i:ime[i] + " | " + cena[i]+ " | " + mesto[i]})

for i in racunari:
    print(racunari[i])





