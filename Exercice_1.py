import PIL.Image 
from tkinter import filedialog
from tkinter import *
from tkinter.messagebox import showinfo
from random import randint

class Exo1:
    def __init__(self):
        self.__format = [ ( "Image" , ".bmp" ), ( "Image" , ".png" ), ( "Image" , ".jpg" ) ]
        self.__root = Tk()
        self.__root.title("1ARIT")
        self.__root.geometry("500x250")
        self.__root.configure()
        bg = PhotoImage(file = 'fond1.png')
        self.__label2 = Label(self.__root, image = bg)
        self.__label2.place(x=0,y=0)
        self.__label = Label(self.__root, text='Exercice 1',bg='#569862', fg='white', font=10)
        self.__button1 = Button(self.__root, text="Chiffrage d'une image", command = lambda:self.chiffrement(),bg='#569862', fg='white', font=10)
        self.__button2 = Button(self.__root, text="Déchiffrage d'une image", command = lambda:self.dechiffrement(),bg='#569862', fg='white', font=10)
        self.__label.pack(padx=10, pady=10)
        self.__button1.pack(padx=10, pady=10)
        self.__button2.pack(padx=10, pady=10)
        self.__root.mainloop()
        
    ### Création d'une clé ###
        
    def keyCreate(self,width,height):
        crypted = PIL.Image.new('RGB',(width,height))
        for i in range(width):
            for j in range(height):
                r=randint(0,255)
                g=randint(0,255)
                b=randint(0,255)
                crypted.putpixel((i,j),(r,g,b))   
        crypted.save('image_exo1\key_exo1.bmp')  
        return crypted    

    ### Chiffrage d'une image ### 
    
    def chiffrement(self):
        giveImage = filedialog.askopenfilename(title = 'Sélectionnez une image à chiffrer' ,filetypes = self.__format)
        image = PIL.Image.open(giveImage)
        key = self.keyCreate(image.size[0], image.size[1])
        self.dechiffrement()

    ### Déchiffrage d'une image ### 
                            
    def dechiffrement(self):
        giveImage = filedialog.askopenfilename(title = 'Sélectionnez une image à chiffrer ou déchiffrer' ,filetypes = self.__format)
        giveKey = filedialog.askopenfilename(title = 'Sélectionnez une clé' ,filetypes = self.__format)
        image = PIL.Image.open(giveImage)
        key = PIL.Image.open(giveKey)        
        pixel = image.load()
        key = key.load()
        width,height = image.size
        for i in range(width):
            for j in range(height):
                
                r,g,b = pixel[i,j]
                bin(r)
                bin(g)
                bin(b)
                
                r2,g2,b2 = key[i,j]
                bin(r2)
                bin(g2)
                bin(b2)
                
                r3 = r^r2
                g3 = g^g2
                b3 = b^b2
                
                image.putpixel((i,j),(r3,g3,b3))
        image.save('image_exo1\image_chiffrée_ou_déchiffrée_exo1.bmp')        
        image.show()

Exo1()                  
           
            
            
      

                        
                    
                    
                    
           
            
            