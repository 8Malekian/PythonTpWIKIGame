from bs4 import BeautifulSoup
from urllib.parse import unquote_plus
from tkinter import *

import urllib.request
import re
import sys




# objet des liens des pages
class Link():
    def __init__(self, nom, index, url):
        self.nom = nom
        self.index = index
        self.url = url

# extraction du de la page internet

def extractPage(url):
    print(url)
    with urllib.request.urlopen(url) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
    
    return soup
#validation du choix du joueur

def validationChoix(startList):
    choixJoueur=-1
    while True:
        try:
                choixJoueur=int(input("Votre choix :"))
        except ValueError:
                print("Entrer un nombre entre {} et  {} ".format(startList,startList+20))
                continue
        if (choixJoueur >= startList and choixJoueur <= startList+20)or choixJoueur==99 or choixJoueur==0:        
            finalchoice=choixJoueur
            return finalchoice     
        elif (choixJoueur==98) and (startList !=0):
            finalchoice=choixJoueur
            return finalchoice   
        else:
            print("Entrer un nombre entre {} et  {} ".format(startList,startList+20))
    

#extraction des liens à partir de la page au hazard

def extract():
    
    url = "https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard"

    soup = extractPage(url)
   
    for anchor in soup.find_all('link', {'rel': "canonical"}):
        url= unquote_plus(anchor.get("href").split("https://fr.wikipedia.org")[1],encoding='utf-8', errors='replace')
        #print(url)
    for anchor in soup.find('h1',class_="firstHeading"):
        anchorText=str(anchor.string)     
        #print(anchorText)
         

    return Link(anchorText,0,url)
            
            

     

#affichage des résultats

def affichage(list,cherche,tours):
    if len(list)<20:
      for i in range(len(list)):
          print(i," - ",list[i].nom)  
    else:
        if tours!=0:{
            print("00 - revenir au choix précédent")
        }
        for i in range(cherche,(cherche+21),1):
            if i<len(list):
                print(i," - ",list[i].nom)
        if cherche!=0:{print("98 - voir liens précédent")} 
        print("99 - Voir la suite")
        


# extraction du l'ensemble des liens d'un page sous forme d'un tableau d'objet link

def extractall(elem):
    sortie=[]
    i = 1
    #print("extract",elem)
    url = "https://fr.wikipedia.org{}".format(elem)
    soup = extractPage(url)

    for jumpLink in soup.find_all("div", {'class':["toc","navbox-container","homonymie","image","reference-cadre","noprint plainlinksneverexpand nowrap tnavbar","bandeau-cell","infobox_v3"]}):
            jumpLink.extract()    
    for jumpLink in soup.find_all("table", {'class':["infobox_v2","infobox_v3","infobox","wikitable"]}):
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
            url= unquote_plus(anchor.get("href"),encoding='utf-8', errors='replace')  
            i += 1
            #print(anchor.get("href"))
            #print(url)
            #print(str(anchor.getText()))

            sortie.append(Link(str(anchor.getText()),i,url))    
            #print(i)
    return sortie
def gagnant(choix,cible):
    return (choix==cible)
    



def Main():
    positionTour=0
    nbTour=0
    choixNonvalider=True
    proposition=[]
    defaite= True
    choixJoueur=0
    startList=0
    actuel=""
    depart= extract()
    precedent=depart
    actuel=depart
    cible= extract()
    
    while defaite:
        choixNonvalider= True
        
        proposition.append(extractall(actuel.url))
        while choixNonvalider:
            print("************************ WikiGame **** Tour : {}".format(nbTour+1))
                       
            print("Départ :{}".format(depart.nom))
        
            print("Cible :{}".format(cible.nom))
            if (positionTour==0):
                print("Actuellement :{}".format(depart.nom))
            else: 
                print("Actuellement :{}".format(actuel.nom))  
            affichage(proposition[positionTour],startList,nbTour)
            choixJoueur=validationChoix(startList)

            if choixJoueur==00 & positionTour!=0   :
                    del proposition[-1]
                    positionTour-=1
                    startList=0
                    actuel=precedent
                    print(actuel)
            elif choixJoueur==98:
                    startList-=20               
            elif choixJoueur==99: 
                    startList+=20
                    
            else:
                    if gagnant(actuel.url,cible.url):
                        defaite=False
                        break
                    if nbTour>1:
                        precedent=actuel
                    url=proposition[positionTour][choixJoueur]
                    #print(url.url)
                    #print(url.nom)
                    actuel=url
                    proposition.append(extractall(actuel.url))
                    positionTour+=1
                    nbTour+=1
                    choixNonvalider=False
    
    print("Bravos, vous avez gagnez en {} de tours".format (nbTour+1))
                    

    



def interface():
    root =Tk()
    positionTour=0
    nbTour=0
    listeDesPropositions = Listbox()
    choixNonvalider=True
    proposition=[]
    defaite= True
    choixJoueur=0
    startList=0

    actuel=""
    depart= extract()
    precedent=depart
    actuel=depart
    cible= extract()
    proposition.append(extractall(actuel.url))


    def up(depart,list):
        depart+=20
        affichageList(depart,list)
    def down(depart,list):
        if depart>0:
            depart-=20
            affichageList(depart,list)   
       
    def affichageList(depart,list):
        
        
        if len(list)<20:
            listeDesPropositions.delete(0,'end')
            for i in range(len(list)):
                listeDesPropositions.insert(i,(i, list[i].nom))
        else:
            listeDesPropositions.delete(0,'end')
            for i in range(depart,(depart+21),1):
                if i<len(list):
                    listeDesPropositions.insert(i,(i, list[i].nom)) 
                



    root.title('************************ WikiGame ********************')
        
    Label(root,
              text ="Départ :{}".format(depart.nom)).grid(row =2)
    Label(root,
              text ="Cible :{}".format(cible.nom)).grid(row =3)
    if (positionTour==0):
            Label(root,
              text ="Actuellement :{}".format(depart.nom)).grid(row =4)                
    else:
            Label(root,
              text ="Actuellement :{}".format(actuel.nom)).grid(row =4) 
    listeDesPropositions = Listbox(root, width=30, height=25)
    listeDesPropositions.grid(row=5, column=0, padx=15, pady=15,sticky = E)
    affichageList(startList,proposition[positionTour])
    """    
    Button(root, text ='suivant',
               command = up(startList,proposition[positionTour])).grid(row =5, sticky = W)
    Button(root, text ='précedent',
               command =down(startList,proposition[positionTour])).grid(row =5, sticky = W)
    
      """
    root.mainloop()

   


interface()     
    
#extract()   
#Main()   
