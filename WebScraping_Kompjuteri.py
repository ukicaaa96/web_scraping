#Analiziramo sajt i trazimo potrebne informacije

# class adPrice - cena
# class adName - image

import bs4
import requests

cena = []
cenaFinal =[]

naziv=[]
nazivFinal=[]
url = "https://www.kupujemprodajem.com/Kompjuteri-Desktop/Polovni-kompjuteri/10-98-1-grupa.htm"
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text , "lxml")

################################################################################
for i in soup.select(".adPrice"):#Uzimamo svaki podatak iz klase adPrice - to je cena predemta
    cene = i.text
    cena.append(str(cene))#smestamo u listu koju cemo kasnije filtrirati
for j in cena:# filtriranje - uzimamo samo brojeve i valutu bez ostalih stvari (/''{:#^ i nepotrebnih slova)
    cenaFinal.append(''.join(c for c in j if c in '0123456789,€dinKontakt '))#praznom stringu dodajemo odgovarajuce karaktere

################################################################################

for i in soup.select(".adName"): #Uzimamo svaki podatak iz klase adName - to je ime predmeta
    nazivi = i.text
    naziv.append(str(nazivi))#smestamo u listu koju cemo kasnije filtrirati
for j in naziv:# filtriranje - uzimamo samo slova bez ostalih stvari (/''{:$#^....)
    nazivFinal.append(''.join(c for c in j if c in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890 ')) #praznom stringu dodajemo odgovarajuce karaktere

################################################################################
if (len(cenaFinal) == len(nazivFinal)):
    for g in range (len(nazivFinal)): #ispis naziva i cene zajedno
        print(nazivFinal[g] + " : " + cenaFinal[g])

else:
    print("broj predmeta i broj cena nije isti...")
