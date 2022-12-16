#Importation des bibliothèques utiles au projet

from tkinter import *
from PIL import Image, ImageTk, ImageEnhance, ImageFilter, ImageDraw
from tkinter.filedialog import askopenfilename, askdirectory, asksaveasfile
import PIL.ImageOps
import os

###############################################FONCTIONS##################################################################
#Fonctions actionnées lors d'un clic sur le bouton correspondant: 
#L'image finale est sauvegardée après chaque changement dans la variable globale stacked.
#L'image modifiée est placée dans label2.

def interchangement():
    global stacked
    img = ImageTk.PhotoImage(stacked)
    label1 = Label(image=img)
    label2 = Label(image=img)
    label1.place(x=0,y=0)
    label2.place(x=580,y=0)
    label2 = Label(image=img)
    label2.image = img
    label2.place(x=580,y=0)
    boutonflou()
    boutoncontraste()

def negatif():
    global stacked
    global l
    global l1
    stock = stacked
    L,H=stock.size
    for y in range(H):
        for x in range(L):
            r,v,b=stock.getpixel((x,y))
            stock.putpixel((x,y),(255-r,255-v,255-b)) #formule pour rendre negatif les couleurs RGB
    stock2 = ImageTk.PhotoImage(stock) #creer une image adapter a TKinter venant de PIL
    label2 = Label(image=stock2) #creer le label TK pour cette image
    label2.image = stock2 #la stocker pour simplifier
    label2.place(x=580,y=0) #la placer 
    l=oulf() #mettre a jour la list des images flou car il y a eu changement
    stacked = stock #mettre a jour stack
    boutonflou() #reinitialiser le curseur pour le remettre a 0
    l1=rcontraste() #mettre a jour la list des images contraste car il y a eu changement
    boutoncontraste() #reinitialiser le curseur pour le remettre a 0
    #etc, meme legende pour tout les fonction

def noircir():
    global stacked
    global l
    global l1
    stock = stacked
    L,H=stock.size
    for y in range(H):
        for x in range(L):
            r,v,b=stock.getpixel((x,y))
            l = int(r*0.299+v*0.587+b*0.114) #formule pour rendre les couleurs en noir et blanc
            stock.putpixel((x,y),(l,l,l))
    stock2 = ImageTk.PhotoImage(stock)
    label2 = Label(image=stock2)
    label2.image = stock2
    label2.place(x=580,y=0)
    l=oulf()
    stacked = stock
    boutonflou()
    l1=rcontraste()
    boutoncontraste()

def contraste(x):
    global stacked
    global l
    global l1
    stock = l1[int(x)-1] #appelle de la list creer par rcontraste() avec x définie par le curseur
    stock2 = ImageTk.PhotoImage(stock)
    label2 = Label(image=stock2)
    label2.image = stock2
    label2.place(x=580,y=0)
    stacked = l1[int(x)-1]
    l=oulf()
    boutonflou()

def rcontraste():
    global stacked
    l1=[]
    for x in range(2,13):
        l1.append(ImageEnhance.Contrast(stacked).enhance(int(x)/2)) #creation de la liste du contraste avec different niveau pour que le bouton curseur aille chercher dedans
    return l1

def oulf():
    global stacked
    l=[]
    l.append(stacked)
    for x in range(10):
        l.append(stacked.filter(ImageFilter.BoxBlur(int(x))))  #creation de la liste du flou avec different niveau pour que le bouton curseur aille chercher dedans
    return l

def flou(x):
    global stacked
    global l
    global l1
    stock=l[int(x)-1] #appelle de la list creer par oulf() avec x définie par le curseur
    stock2=ImageTk.PhotoImage(stock)
    label2 = Label(image=stock2)
    label2.image = stock2
    label2.place(x=580,y=0)
    stacked = stock
    l1=rcontraste()
    boutoncontraste()

def telechargement():
    global stacked
    fichier = asksaveasfile(title="Enregistrer l'image sous", filetypes=[("Fichier JPG",".jpg")], defaultextension=".jpg")
    stacked.save(fichier)

def flouinfo():
    global labelF
    labelF = Label(root, text="flou sert a melanger les pixel voisin pour les rendre méconnaissable", font=('Helvetica 10'))
    labelF.place(x=565,y=310)
    b1 = Button(root,width=6,bg='RED', text = "X",command=flouinfodelete)
    b1.place(x=960,y=310)

def flouinfodelete():
    global labelF
    labelF.destroy()
    img = ImageTk.PhotoImage(stacked)
    label2 = Label(image=img)
    label2.place(x=580,y=0)
    label2 = Label(image=img)
    label2.image = img
    label2.place(x=580,y=0)

def contrastinfo():
    global labelC
    a=time.time()
    b=0
    labelC = Label(root, text="contrast sert a changer la différence de luminosité entre les parties claires et sombres d'une image.", font=('Helvetica 8'))
    labelC.place(x=565,y=198)
    b1 = Button(root,width=6,bg='RED', text = "X",font=('Helvetica 8'),command=contrastinfodelete)
    b1.place(x=1045,y=198)

def contrastinfodelete():
    global labelC
    labelC.destroy() 
    img = ImageTk.PhotoImage(stacked)
    label2 = Label(image=img)
    label2.place(x=580,y=0)
    label2 = Label(image=img)
    label2.image = img
    label2.place(x=580,y=0)

def boutonflou():
    curseur=Scale(root,width=10, orient='vertical', from_=1, to=10,
            resolution=1, tickinterval=3, length=75,command=flou)
    curseur.place(x=514,y=202)
    b2 = Button(root,width=6,bg='#0961A4', text = "flou",command=flouinfo)
    b2.place(x=514,y=284)

def flip():
    global stacked
    global l
    global l1
    stock = stacked
    reverse = PIL.ImageOps.flip(stock)
    stock2 = ImageTk.PhotoImage(reverse)
    Label2 = Label(image=stock2)
    Label2.Image = stock2
    Label2.place(x=580,y=0)
    stacked = reverse
    boutonflou()
    l=oulf()
    l1=rcontraste()
    boutoncontraste()

def boutoncontraste():
    curseur=Scale(root,width=10, orient='vertical', from_=1, to=10,
            resolution=1, tickinterval=3, length=75,command=contraste)
    curseur.place(x=514,y=90)
    b1 = Button(root,width=6,bg='#0961A4', text = "contraste",command=contrastinfo)
    b1.place(x=514,y=172)
    
def mirror():
    global stacked
    global l
    global l1
    stock = stacked
    reverse = PIL.ImageOps.mirror(stock)
    stock2 = ImageTk.PhotoImage(reverse)
    Label2 = Label(image=stock2)
    Label2.Image = stock2
    Label2.place(x=580,y=0)
    stacked = reverse
    boutonflou()
    l=oulf()
    l1=rcontraste()
    boutoncontraste()
    
    
###############################################PLACEMENT DES ELEMENTS#####################################################


#creation fenètre
root = Tk()
root.title("Couetoushop")
root.geometry("1080x720")
root.config(background='grey')

#importation de l'image à modifier
image = Image.open(askopenfilename(title="Ouvrir l'image à modifier"))

#conversion si png
if image.format=='PNG':
    image = image.convert("RGB")

#création du label contenant l'image de gauche, sur laquelle appliquer les modifications
resize_image = image.resize((500,int((500/image.size[0])*image.size[1]))) #reajustement de l'image par rapport au support
stacked=resize_image
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)

#création du label contenant l'image modifiée
label2 = Label(image=img)

#placement de ces labels dans la fenêtre
label1.place(x=0,y=0)
label2.place(x=580,y=0)

#définition de la variable qui sera sauvegardée après toutes les modifications
stacked = resize_image #creation de la variable stacked qui contient constament l'image actuellement utilisé

l=oulf()
l1=rcontraste()


###############################################BOUTON#####################################################################
#cr&ation des boutons permettant les modifications

#bouton de remplacement
btnChangement = Button(root, text ="<--", command = interchangement)
btnChangement.place(x=514,y=0)

#bouton de enregistrer image
btnimage = Button(root, text ="telecharger", command = telechargement)
btnimage.pack(side=BOTTOM)

#bouton du negatif
btnNegatif = Button(root, text ="negatif", command = negatif)
btnNegatif.place(x=514,y=30)

#bouton du noircissement
btnNoircir=Button(root,text="Noircir",command = noircir)
btnNoircir.place(x=514,y=60)

#bouton du contraste
boutoncontraste()

#bouton du flou
boutonflou()

#bouton flip
btnflip = Button(root, width=6, text ="flip", command = flip)
btnflip.place(x=514,y=314)

#bouton mirroir
btnmir = Button(root, width=6, text ="mirroir", command = mirror)
btnmir.place(x=514,y=344)


root.mainloop()