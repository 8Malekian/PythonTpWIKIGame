from bs4 import BeautifulSoup
import urllib.request
import re
import sys


def extract(val):
    #val = input("donner moi les noms de la recherche")

    sortie="0"
    with urllib.request.urlopen('https://www.ecosia.org/search?q={}'.format(val)) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        for anchor in soup.find_all('span',{"class": "result-count"}):
            result=str(anchor.get_text()).strip().split(" ")[0]
            sortie=int(result.replace(",",""))
    return sortie
        #print("le resultat est ")
        #print(str(sortie) ) 

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