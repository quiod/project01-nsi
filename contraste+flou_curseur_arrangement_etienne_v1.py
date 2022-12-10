from tkinter import *
from PIL import Image, ImageTk, ImageEnhance, ImageFilter
from tkinter.filedialog import askopenfilename
import PIL.ImageOps

###############################################FONCTIONS##################################################################
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

def negatif():
    global stacked
    stock = stacked
    L,H=stock.size
    for y in range(H):
        for x in range(L):
            r,v,b=stock.getpixel((x,y))
            stock.putpixel((x,y),(255-r,255-v,255-b))
    stock2 = ImageTk.PhotoImage(stock)
    label2 = Label(image=stock2)
    label2.image = stock2
    label2.place(x=580,y=0)
    stacked = stock

def noircir():
    global stacked
    stock = stacked
    L,H=stock.size
    for y in range(H):
        for x in range(L):
            r,v,b=stock.getpixel((x,y))
            l = int(r*0.299+v*0.587+b*0.114)
            stock.putpixel((x,y),(l,l,l))
    stock2 = ImageTk.PhotoImage(stock)
    label2 = Label(image=stock2)
    label2.image = stock2
    label2.place(x=580,y=0)
    stacked = stock

def contraste(x):
    global stacked
    stock = ImageEnhance.Color(stacked).enhance(int(x))
    stock2 = ImageTk.PhotoImage(stock)
    label2 = Label(image=stock2)
    label2.image = stock2
    label2.place(x=580,y=0)
    stacked = stock

def oulf():
    global stacked
    l=[]
    for x in range(10):
        l.append(stacked.filter(ImageFilter.BoxBlur(int(x))))
    return l

def flou(x):
    global stacked
    stock2=ImageTk.PhotoImage(oulf()[int(x)])
    label2 = Label(image=stock2)
    label2.image = stock2
    label2.place(x=580,y=0)
    stacked = stock

def telechargement():
    global stacked
    image.save('stacked.jpg')

###############################################PLACEMENT DES ELEMENTS#####################################################

#creation fenètre
root = Tk()
root.title("editeur photo")
root.geometry("1080x720")
root.config(background='grey')

#importation+mise en place première image
image = Image.open(askopenfilename())
resize_image = image.resize((500,int((500/image.size[0])*image.size[1]))) #reajustement de l'image par rapport au support
stacked=resize_image
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)

#image 2 initialisation
label2 = Label(image=img)

label1.place(x=0,y=0)
label2.place(x=580,y=0)

stacked = resize_image


###############################################BOUTON#####################################################################

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
curseur=Scale(root,width=10, orient='vertical', from_=1, to=10,
        resolution=1, tickinterval=3, length=75,command=contraste)
curseur.place(x=514,y=90)
b1 = Button(root,width=6,bg='#0961A4', text = "contraste")
b1.place(x=514,y=172)

#bouton du flou
curseur=Scale(root,width=10, orient='vertical', from_=1, to=10,
        resolution=1, tickinterval=3, length=75,command=flou)
curseur.place(x=514,y=202)
b2 = Button(root,width=6,bg='#0961A4', text = "flou")
b2.place(x=514,y=284)



root.mainloop()


#test sur les valeurs
'''r, g, b = stacked.split()
r = list(r.getdata())
g = list(g.getdata())
b = list(b.getdata())
t = [[]]
for i in range(len(r)):
    t.append([r[i],g[i],b[i]])
print(t)'''
