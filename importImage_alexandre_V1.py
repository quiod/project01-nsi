#Import de l'image sur l'application. Cette image est choisie par l'utilisateur parmi les fichiers de son ordinateur.

###############################################################################

#Import des mmodules utiles : Image sert à manipuler les images, askopenfilename à intéragir avec l'utillisateur et ImageTk sert de passerelle entre Image et tkinter.
from tkinter import * 
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


#Création et configuration de la fenêtre
window = Tk()
window.title("Couetoushop")
window.geometry("1080x720")
window.minsize(1080,720)
window.config(background='#588D48')


#Import de l'image
img = Image.open(askopenfilename()) #la variable img devient l'image choisie par l'utillisateur
image = img.resize((500,int((500/img.size[0])*img.size[1]))) #l'image est redimensionnée pour faire 540 pixels de large, soit la moitié de la taille de la fenêtre afin de mettre les deux images côte à côte.
img = ImageTk.PhotoImage(image) #img devient un objet tkinter 
modif = ImageTk.PhotoImage(image) #on duplique l'image de base dans la variable modif pour pouvoir ensuite la modifier.
labelImage = Label(window,image=img,bd=20,relief=RIDGE)
labelModif = Label(window,image=modif,bd=20,relief=RIDGE)

#placement des labels côte à côte,car ils mesurent tous deux 500 pixels de large, et deux bordures de 20 pixels de large chacunes, ce qui fait en tout 540 pixels de large par label.
labelImage.place(x=0,y=0)
labelModif.place(x=540,y=0)
window.mainloop()