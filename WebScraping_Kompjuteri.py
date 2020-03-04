#Analiziramo sajt i trazimo potrebne informacije

# class adPrice - cena
# class adName - ime
# class locationSc - mesto
import bs4
import requests

cena = []
cenaFinal =[]

naziv=[]
nazivFinal=[]

mesto =[]
mestoFinal = []

racunari = {}

url = "https://www.kupujemprodajem.com/Kompjuteri-Desktop/Polovni-kompjuteri/10-98-1-grupa.htm"
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text , "lxml")

################################################################################
for i in soup.select(".adPrice"):#Uzimamo svaki podatak iz klase adPrice - to je cena predemta
    cene = i.text
    cena.append(str(cene))#smestamo u listu koju cemo kasnije filtrirati
for j in cena:# filtriranje - uzimamo samo brojeve i valutu bez ostalih stvari (/''{:#^ i nepotrebnih slova)
    cenaFinal.append(''.join(c for c in j if c in '0123456789,€dinKontakt Kupujem Pozvati '))#praznom stringu dodajemo odgovarajuce karaktere

################################################################################

for i in soup.select(".adName"): #Uzimamo svaki podatak iz klase adName - to je ime predmeta
    nazivi = i.text
    naziv.append(str(nazivi))#smestamo u listu koju cemo kasnije filtrirati
for j in naziv:# filtriranje - uzimamo samo slova bez ostalih stvari (/''{:$#^....)
    nazivFinal.append(''.join(c for c in j if c in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890 ')) #praznom stringu dodajemo odgovarajuce karaktere

################################################################################

for i in soup.select(".locationSec"): #Uzimamo svaki podatak iz klase locationSoc - to je lokacija oglasa
    lokacije = i.text
    mesto.append(str(lokacije))#smestamo u listu koju cemo kasnije filtrirati
for j in mesto:# filtriranje - uzimamo samo slova bez ostalih stvari (/''{:$#^....)
    if(j != "Mesto/Grad"):#Na sajtu je i naslov kolone gde se nalaze cene u istoj klasi kao cene tako da to ne zelimo da sacuvamo(preskacemo)
        mestoFinal.append(''.join(c for c in j if c in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890šŠđĐčČćĆŽž ')) #praznom stringu dodajemo odgovarajuce karaktere
################################################################
    

for g in range (1,len(nazivFinal)): # formiramo recnik sa rednim brojevima
    racunari.update({g:nazivFinal[g]+" : " + cenaFinal[g] + " : " + mestoFinal[g]})

###############################################################################################
while(True):
    print("1.Ispisi svaki oglas kompjutera")
    print("2.Ispisi samo oglase iz Beograda")
    izbor = int(input(">"))

    if(izbor == 1):#svi racunari sa prve stranice oglasa na KP 
        for r in racunari:
            print(racunari[r])    

        
    elif(izbor == 2):#samo racunari iz Beograda
        for r in racunari:
            if("Beograd" in racunari[r]):
                print(racunari[r])

    print("-------------------------------------------")
