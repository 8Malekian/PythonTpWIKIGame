from bs4 import BeautifulSoup
import urllib.request
import re
import sys
# objet des liens des pages


class Link():
    def __init__(self, nom, index, url):
        self.nom = nom
        self.index = index
        self.url = url
# extraction du titre


def extractPage(url):
    with urllib.request.urlopen(url) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
    return soup


def extract():
    sortie = "0"
    url = "https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard"

    soup = extractPage(url)
    for anchor in soup.find_all('h1', {"class": "firstHeading"}):
            result = str(anchor.get_text()).strip().split(" ")[0]
            sortie = str(result.replace(",", ""))

        # print("le resultat est ")
        # print(str(sortie) )

    return sortie
def affichage(list,cherche):
    if len(list)<20:
      for i in range(len(list)):
          print(i," - ",list[i].nom)  
    else:
        for i in range(cherche,20,1):
            print(i," - ",list[i].nom) 
        


# extraction du l'ensemble des liens d'un page sous forme d'un tableau d'objet link
def extractall(elem):
    sortie=[]
    i = 0

    url = "https://fr.wikipedia.org/wiki/{}".format(elem)
    

    soup = extractPage(url)

    for jumpLink in soup.find_all("div", {'class':["toc","navbox-container","homonymie","image","reference-cadre","noprint plainlinksneverexpand nowrap tnavbar"]}):
            jumpLink.extract()    
    for jumpLink in soup.find_all("table", {'class':["infobox_v2","infobox_v3","infobox"]}):
            jumpLink.extract()   
    for jumpLink in soup.find_all("a", {'class':["mw-redirect","extiw","internal"]}):
            jumpLink.extract()   
    for jumpLink in soup.find_all("span", {'class':["mw-editsection","indicateur-langue"]}):
            jumpLink.extract()    
    for jumpLink in soup.find_all("ul", class_="bandeau-portail"):
            jumpLink.extract()       
    for jumpLink in soup.find_all("sup", class_="reference"):
            jumpLink.extract()  
            
    for anchor in soup.find('div', class_="mw-parser-output").find_all('a',attrs={'href': re.compile("/wiki/")}):
        anchorText=str(anchor.getText())
        if anchorText.strip()!="":
               
            i += 1
            # print(anchor.getText())

            sortie.append(Link(str(anchor.getText()),i,anchor.get("href")))    
            #print(i)
    return sortie
"""
extractall("python")

"""
def Main():
    nbTour=0
    proposition=[]
    startList=0
    actuel=""
    print("************************ WikiGame **** Tour : {}".format(nbTour+1))
    depart= extract()
    actuel=depart
    print("Départ :{}".format(depart))
    cible= extract()
    print("Cible :{}".format(cible))
    if (nbTour==0):
        print("Actuellement :{}".format(depart))
    else: 
        print("Actuellment :{}".format(actuel))
    
    proposition.append(extractall(actuel))
    affichage(proposition[0],startList)
Main()   
