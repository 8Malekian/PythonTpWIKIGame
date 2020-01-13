from bs4 import BeautifulSoup
import urllib.request
import re
import sys
# extraction du titre d'une page aléatoire


def extract():
    sortie = "0"
    with urllib.request.urlopen("https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard") as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        for anchor in soup.find_all('h1', {"class": "firstHeading"}):
            result = str(anchor.get_text()).strip().split(" ")[0]
            sortie = str(result.replace(",", ""))

        #print("le resultat est ")
        #print(str(sortie) )
    return sortie


extract()
# extraction du l'ensemble des liens d'un page


def extractall():
    # sortie=[]
    i = 0
    with urllib.request.urlopen("https://fr.wikipedia.org/wiki/Python_(langage)") as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')

        for jumpLink in soup.find_all("div", class_="toc"):
            jumpLink.extract()
        for jumpLink in soup.find_all("div", class_="navbox-container"):
            jumpLink.extract()
        for jumpLink in soup.find_all("table", class_="infobox_v2"):
            jumpLink.extract()
        for jumpLink in soup.find_all("table", class_="infobox_v3"):
            jumpLink.extract()
        for jumpLink in soup.find_all("table", class_="infobox"):
            jumpLink.extract()
        for jumpLink in soup.find_all("a", class_="mw-redirect"):
            jumpLink.extract()
        for jumpLink in soup.find_all("div", class_="homonymie"):
            jumpLink.extract()
        for jumpLink in soup.find_all("div", class_="image"):
            jumpLink.extract()
        for jumpLink in soup.find_all("span", class_="mw-editsection"):
            jumpLink.extract()
        for jumpLink in soup.find_all("ul", class_="bandeau-portail"):
            jumpLink.extract()
        for jumpLink in soup.find_all("div", class_="navbox-container"):
            jumpLink.extract()
        for jumpLink in soup.find_all("div", class_="reference-cadre"):
            jumpLink.extract()
        for jumpLink in soup.find_all("a", class_="extiw"):
            jumpLink.extract()
        for jumpLink in soup.find_all("sup", class_="reference"):
            jumpLink.extract()
        for jumpLink in soup.find_all("span", class_="indicateur-langue"):
            jumpLink.extract()
        for jumpLink in soup.find_all("a", class_="internal"):
            jumpLink.extract()

        for anchor in soup.find('div', class_="mw-parser-output").find_all('a'):
            i += 1
            print(anchor.getText())
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
