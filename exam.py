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


extract()
# extraction du l'ensemble des liens d'un page


def extractall():
    sortie=[]
    i = 0

    url = "https://fr.wikipedia.org/wiki/Python_(langage)"

    soup = extractPage(url)

    for jumpLink in soup.find_all("div", {'class':["toc","navbox-container","homonymie","image","reference-cadre"]}):
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
  
    
    for anchor in soup.find('div', class_="mw-parser-output").find_all('a'):
        i += 1
        print(anchor.getText())
        sortie.append(anchor.getText())    
    print(i)


extractall()

"""
def calculeTheBest(proposition1,proposition2):
         
    val1= extract(proposition1)
    val2= extract(proposition2)
    if val1<val2:
            print ("c'est {} qui gagne".format(proposition1), round ((val1/(val1+val2))*100, 2), "%")
    if val1>val2:
            print ("c'est {} qui gagne".format(proposition2), round ((val1/(val2+val1))*100, 2), "%") 


var1 =input("propo1")
var2 =input("propo2")
calculeTheBest(var1,var2) 
"""
