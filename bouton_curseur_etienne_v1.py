from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import PIL.ImageOps


###############################################FONCTIONS##################################################################


def negatif():
    global stacked
    stock = PIL.ImageOps.invert(stacked)
    stock2 = ImageTk.PhotoImage(stock)
    label2 = Label(image=stock2)
    label2.image = stock2
    label2.place(x=580,y=0)
    stacked=stock

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


###############################################BUTTON#####################################################


#bouton du negatif
btnNegatif = Button(root, text ="negatif", command = negatif)
btnNegatif.pack(side=TOP)
#bouton du noircissement
btnNoircir=Button(root,text="Noircir",command = noircir)
btnNoircir.pack(side=TOP)
#bouton du interchangement
btninter=Button(root,text="inter",command = interchangement)
btninter.pack(side=TOP)
curseur=Scale(root,width=10, orient='vertical', from_=0, to=100,
        resolution=5, tickinterval=25, length=100,command=)
curseur.pack(side=TOP)

root.mainloop()