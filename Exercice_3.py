import PIL.Image 
from numpy import asarray
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from random import randint

from numpy import asarray

class Exo3:
    def __init__(self):
        self.__format = [ ( "Image" , ".bmp" ), ( "Image" , ".png" ), ( "Image" , ".jpg" ) ]
        self.__root = Tk()
        self.__root.title("1ARIT")
        self.__root.geometry("500x350")
        self.__root.configure()
        bg = PhotoImage(file = 'fond2.png')
        self.__label2 = Label(self.__root, image = bg)
        self.__label2.place(x=0,y=0)
        self.__label = Label(self.__root, text='Exercice 3',bg='#569862', fg='white', font=10)
        self.__button1 = Button(self.__root, text="Masquage d'une image", command = lambda:self.masquageText(self.__text),bg='#569862', fg='white', font=10)
        self.__button2 = Button(self.__root, text="Démasquage d'une image", command = lambda:self.demasquageText(),bg='#569862', fg='white', font=10)
        self.__entry = Entry(self.__root, text='Donne moi un texte à masquer', font=10)
        self.__button3 = Button(self.__root, text='Valide ton texte',command=lambda:self.getText(),bg='#569862', fg='white', font=10)
        self.__text = ""
        self.__label.pack(padx=10, pady=10)
        self.__button1.pack(padx=10, pady=10)
        self.__button2.pack(padx=10, pady=10)
        self.__button3.pack(padx=10, pady=10)
        self.__entry.pack(padx=10, pady=10)
        self.__root.mainloop()
        
    ###popup pour afficher le texte caché###
    
    def open_popup(self,texte):
        top= Toplevel(self.__root)
        top.geometry("1920x250")
        top.title("Texte Caché")
        Label(top, text= texte).place(x=0,y=0)  
        
    ###Récupération du texte###
    
    def getText(self):
        self.__text = self.__entry.get()
    
    ###Masquage de texte###
      
    def masquageText(self,text):
        giveImage = filedialog.askopenfilename(title = 'Sélectionnez une image' ,filetypes = self.__format)
        image = PIL.Image.open(giveImage)
        data = asarray(image)
        
        #convertit le message en octet
        messageFinal = ""
        for lettre in text:
            posAscii = ord(lettre)
            binaire = bin(posAscii)[2:]
            while len(binaire) < 8:
                binaire = "0" + binaire
            messageFinal += binaire
            
        #inscrire sur 2 octets
        longueur = len(messageFinal)
        binaire = bin(longueur)[2:]
        while len(binaire) < 16:
            binaire = "0" + binaire
        messageResultat = binaire + messageFinal
        
        #modifier les pixels rgb avec le binaire du texte
        tour = 0
        i = 0
        for ligne in data:
            j = 0
            for colonne in ligne:
                rgb = 0
                for couleur in colonne: 
                    pix = data[i][j][rgb]
                    if pix == 255:
                        pix = 254
                    pixBinaire = bin(pix)[2:]
                    listePixBinaire = list(pixBinaire)
                    del listePixBinaire [-1]
                    listePixBinaire.append(messageResultat[tour])
                    newPix = int("".join(listePixBinaire),2)
                    data[i][j][rgb] = newPix
                    tour += 1
                    rgb += 1
                    if tour >= len(messageResultat):
                        break
                j += 1
                if tour >= len(messageResultat):
                        break
            i += 1
            if tour >= len(messageResultat):
                        break
        imageFin = PIL.Image.fromarray(data)
        imageFin.save('image_exo3/texte_caché.png')
    
    def demasquageText(self):
        giveImage = filedialog.askopenfilename(title = 'Sélectionnez une image' ,filetypes = self.__format)
        image = PIL.Image.open(giveImage)
        data = asarray(image).copy()
        
        #récupérer le binaire du texte dans les pixels rgb
        tour = 0
        taille = ""
        message = ""
        newTaille = 1267
        x = 0
        for ligne in data:
            y = 0
            for colonne in ligne:
                rgb = 0
                for couleur in colonne:
                    pix = data[x][y][rgb]
                    pixBinaire = bin(pix)[2:]
                    lastPix = pixBinaire[-1]
                    if tour < 16:
                        taille += lastPix
                    if tour == 16:
                        newTaille = int(taille,2)
                    if tour - 16 < newTaille:
                        message += lastPix
                    if tour-16 >= newTaille:
                        break
                    tour += 1
                    rgb += 1
                if tour-16 >= newTaille-1:
                        break
                y += 1
            if tour-16 >= newTaille-1:
                        break
            x += 1 
            
        #remettre le message sous forme ascii
        messageOctet = []
        for i in range(len(message)//8):
            messageOctet.append(message[i*8:(i+1)*8]) 
        result = ""
        retour = 0
        for oct in messageOctet:
            index = int(oct,2)
            lettreAscii = chr(index)
            result += lettreAscii
            if retour >= 175:
                result += "\n"
                retour = 0
            retour += 1
        result = str(result)[2:]
        self.open_popup(result)
        
        
Exo3()

        