from bs4 import BeautifulSoup
import urllib.request
import re
import sys

def extract():
    

    sortie="0"
    with urllib.request.urlopen("https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard") as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        for anchor in soup.find_all('h1',{"class": "firstHeading"}):
            result=str(anchor.get_text()).strip().split(" ")[0]
            sortie=str(result.replace(",",""))
    
        print("le resultat est ")
        print(str(sortie) ) 
    return sortie
extract()

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