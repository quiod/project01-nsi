from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import PIL.ImageOps


def negatif():
    stock =PIL.ImageOps.invert(resize_image)
    stock2 = ImageTk.PhotoImage(stock)
    labelS = Label(image=stock2)
    labelS.image = stock2
    labelS.place(x=580,y=0)


#creation fenètre
root = Tk()
root.title("editeur photo")
root.geometry("1080x720")
root.config(background='grey')

#importation+mise en place première image
image = Image.open(askopenfilename())
resize_image = image.resize((500,int((500/image.size[0])*image.size[1]))) #reajustement de l'image par rapport au support
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img

#image 2 initialisation
label2 = Label(image=img)
label2.image = img

label1.place(x=0,y=0)
label2.place(x=580,y=0)


#fonction qui met la deuxieme image en negatif

#bouton du negatif
btn = Button(root, text ="Cliquez ici!", command = negatif)
btn.pack()


root.mainloop()