from bs4 import BeautifulSoup
from urllib.parse import unquote_plus
from tkinter import *
from urllib import parse
import urllib.request
import urllib

import re
import sys

startList=0
positionTour=0
nbTour=0
choixNonvalider=True
proposition=[]
defaite= True
choixJoueur=0
startList=0
actuel=""
cible=""
root =Tk()


# objet des liens des pages
class Link():
    def __init__(self, nom, index, url):
        self.nom = nom
        self.index = index
        self.url = url

# extraction du de la page internet

def extractPage(url):
    
    print('ici',url)
    try:
        with urllib.request.urlopen(url) as response:
            webpage = response.read()
            soup = BeautifulSoup(webpage, 'html.parser')
        return soup
    except:
        url = urllib.parse.urlsplit(url)
        url = list(url)
        url[2] = urllib.parse.quote(url[2])
        url = urllib.parse.urlunsplit(url)
        print('exe',url)
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
    global depart
    global precedent
    global cible
    global actuel
    global proposition
    global positionTour
    
    positionTour=0    
    choixJoueur=0
    startList=0
    listeDesPropositions = Listbox()
    depart= extract()
    precedent=depart
    actuel=depart
    cible= extract()    
    proposition.append(extractall(actuel.url))
    

    def up(list):
        print("up")
        global startList 
        startList += 20
        affichageList(startList,list)
        print(startList)
    def down(list):
        print("down")
        global startList 
        if startList>0:
            startList -= 20
            affichageList(startList,list)
           
    def back():
        global positionTour
        if nbTour!=0:
            positionTour-=1
            global startList 
            startList = 0
            global proposition
            del proposition[-1]
            global actuel
            actuel=precedent
            print(actuel)
            affichageList(startList,proposition[positionTour]) 

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
    
    def validationChoixFrame():
        choixJoueur=propoEntry.get()
        global startList
       
        try:
                choixJoueur=int(choixJoueur)
                
                if (choixJoueur >= startList and choixJoueur <= startList+20):        
                    finalchoice=choixJoueur
                    return finalchoice     
                else:
                    labelError.config(text="Entrer un nombre entre {} et  {} ".format(startList,startList+20))
                    return-1
            
        except ValueError:
                    labelError.config(text="Entrer un nombre entre {} et  {} ".format(startList,startList+20))
                    return -1
    
    def validation():
        global actuel
        global proposition
        global nbTour
        global positionTour
        global cible
        global startList
      
        
        if gagnant(actuel.url,cible.url):
            print("fff")          
            
        if positionTour>1:
            PageactuelLabel.config(text="Actuellement :{}".format(actuel.nom))
        
        choix = validationChoixFrame()
        
        url=proposition[positionTour][choix]
        #print(url.url)
        #print(url.nom)
        
        actuel=url
        proposition.append(extractall(actuel.url))
        positionTour+=1
        nbTour+=1
        startList=0 
        print(proposition[positionTour][1].nom)
        affichageList(startList,proposition[positionTour])             
                  
#frame d'affichage

    
    root.title('******************** WikiGame ********************')
    root.geometry("400x550")
    topFrame=Frame(root, width =400, height =50).grid(row=0,columnspan=2)
    Label(topFrame,
              text ="Départ :{}".format(depart.nom)).grid(row =0)
    Label(topFrame,
              text ="Cible :{}".format(cible.nom)).grid(row =1)
    PageactuelLabel=Label(topFrame,
            text ="Actuellement :{}".format(depart.nom)).grid(row =2)                
    
    listFrame=Frame(root).grid(row=4)

    listeDesPropositions = Listbox(listFrame,width=40, height= 22)
    listeDesPropositions.grid(row=4, column=0,ipady=5)
    
    affichageList(startList,proposition[positionTour])
    frameNavigBouton=Frame(listFrame)
    frameNavigBouton.grid(row=4,column=1)   
    Button(frameNavigBouton, text ='suivant',
               command = lambda: up(proposition[positionTour]),height="2",width="8").grid(row =4,column=1, sticky = W)
    Button(frameNavigBouton, text ='précedent',
               command = lambda: down(proposition[positionTour]),height="2",width="8").grid(row =5,column=1, sticky = W)
    Button(frameNavigBouton, text ='retour',
               command = lambda: back(),height="2",width="8").grid(row =6,column=1, sticky = W)
    propositionFrame=Frame(root).grid(row=7)
    propoEntry= Entry(propositionFrame)
    propoEntry.grid(row=7,column=0)
    validationButom=Button(propositionFrame,text ='validation', command = validation)
    validationButom.grid(row=7, column=1, sticky =W)
    LabelMessage=Label(root, text="Vous étes au tour: {}".format(nbTour+1))
    LabelMessage.grid(row=8)
    labelError=Label(root, text="",fg="red")
    labelError.grid(row=9)
    root.mainloop()

   


interface()     
    
#extract()   
#Main()   
