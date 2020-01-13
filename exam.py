# Python 3
# Extraction des liens d'une page web
from bs4 import BeautifulSoup
import urllib.request
import sys

param1 = str(sys.argv[1]).replace(' ', '+')
param2 = str(sys.argv[2]).replace(' ', '+')


def nbResultat(recherche):
    with urllib.request.urlopen('http://www.ecosia.org/search?q='+recherche) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        for anchor in soup.find_all('span', class_="result-count"):
            text = str(anchor.getText().strip())
            if text.find("results") != -1:
                r = text.split(' ')[0]
                return r


def calculEtAffiche(param1, param2):
    nbParam1 = int(nbResultat(param1).replace(',', ''))
    nbParam2 = int(nbResultat(param2).replace(',', ''))
    if(nbParam1 > nbParam2):
        print(param1, 'gagne avec', round(
            (nbParam1/(nbParam1+nbParam2))*100, 2), '%')
    else:
        print(param2, 'gagne avec', round(
            (nbParam2/(nbParam2+nbParam1))*100, 2), '%')


calculEtAffiche(param1, param2)
