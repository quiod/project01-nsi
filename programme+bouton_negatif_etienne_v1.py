from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import PIL.ImageOps


def interchangement():
    stock=10
    setimg(stock)
    

#fonction qui met la deuxieme image en negatif
def negatif():
    stock =PIL.ImageOps.invert(resize_image)
    stock2 = ImageTk.PhotoImage(stock)
    labelS = Label(image=stock2)
    labelS.image = stock2
    labelS.place(x=580,y=0)


def setimg(image):
    #importation+mise en place première image
     #reajustement de l'image par rapport au support
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(image=img)
    label1.image = img
    
    #image 2 initialisation
    label2 = Label(image=img)
    label2.image = img
    
    label1.place(x=0,y=0)
    label2.place(x=580,y=0)


#creation fenètre
root = Tk()
root.title("editeur photo")
root.geometry("1080x720")
root.config(background='grey')

image=Image.open(askopenfilename())
rezise_image=resize_image = image.resize((500,int((500/image.size[0])*image.size[1])))
setimg(resize_image)


#bouton du negatif
btn = Button(root, text ="Cliquez ici!", command = negatif)
btn.pack(side=TOP)

btn1 = Button(root, text ="Cliquez ici!", command = interchangement)
btn1.pack(side=BOTTOM)

root.mainloop()
