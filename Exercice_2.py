import PIL.Image 
from tkinter import filedialog
from tkinter import *
from tkinter.messagebox import showinfo
from random import randint

class Exo2:
    def __init__(self):
        self.__format = [ ( "Image" , ".bmp" ), ( "Image" , ".png" ), ( "Image" , ".jpg" ) ]
        self.__root = Tk()
        self.__root.title("1ARIT")
        self.__root.geometry("500x350")
        self.__root.configure()
        bg = PhotoImage(file = 'fond2.png')
        self.__label2 = Label(self.__root, image = bg)
        self.__label2.place(x=0,y=0)
        self.__label = Label(self.__root, text='Exercice 2',bg='#569862', fg='white', font=10)
        self.__button1 = Button(self.__root, text="Masquage d'une image", command = lambda:self.masquageComplet(),bg='#569862', fg='white', font=10)
        self.__button2 = Button(self.__root, text="Démasquage d'une image", command = lambda:self.demasquage(),bg='#569862', fg='white', font=10)
        self.__entry = Entry(self.__root, text='Donne moi une valeur de k', font=10)
        self.__button3 = Button(self.__root, text='Valide k',command=lambda:self.getK(),bg='#569862', fg='white', font=10)
        self.__k = 0
        self.__label.pack(padx=10, pady=10)
        self.__button1.pack(padx=10, pady=10)
        self.__button2.pack(padx=10, pady=10)
        self.__button3.pack(padx=10, pady=10)
        self.__entry.pack(padx=10, pady=10)
        self.__root.mainloop()
    
    ###Récupération de k###
    
    def getK(self):
        self.__k = self.__entry.get()
        
    ### Création d'une clé ###
        
    def keyCreate(self,width,height):
        crypted = PIL.Image.new('RGB',(width,height))
        for i in range(width):
            for j in range(height):
                r=randint(0,255)
                g=randint(0,255)
                b=randint(0,255)
                crypted.putpixel((i,j),(r,g,b))   
        crypted.save('image_exo2\key_exo2.bmp')  
        return crypted      

    ### Masquage d'une image ### 

    def masquage(self,image,key,k):
        width,height = image.size
        pixel = image.load()
        key = key.load()
        
        if k is not int:
            k = int(k,base=10)
        if k < 0:
            k = abs(k) 
            
        for i in range(width):
            for j in range(height):  
                
                r,g,b = pixel[i,j]
                r2,g2,b2 = key[i,j]
                
                r3 = r2 + (1/k*r)
                g3 = g2+ (1/k*g)
                b3 = b2 + (1/k*b)
                
                if r3 > 255:
                    r3 = 255
                if g3 > 255:
                    g3 = 255
                if b3 > 255:
                    b3 = 255
                    
                image.putpixel((i,j),(int(r3),int(g3),int(b3)))
        image.save('image_exo2\image_chiffrée_exo2.bmp')        
        image.show()

    ### Démasquage d'une image ### 
       
    def demasquage(self):
        giveImage = filedialog.askopenfilename(title = 'Sélectionnez une image' ,filetypes = self.__format)
        giveKey = filedialog.askopenfilename(title = 'Sélectionnez une clé' ,filetypes = self.__format)
        image = PIL.Image.open(giveImage)
        key = PIL.Image.open(giveKey)
        width,height = image.size
        pixel = image.load()
        key = key.load()
        
        k = self.__k
        if k is not int:
            k = int(k,base=10)
        if k < 0:
            k = abs(k) 
            
        for i in range(width):
            for j in range(height):
                
                r,g,b = pixel[i,j]
                r2,g2,b2 = key[i,j]
                
                r3 = k*(r-r2)
                g3 = k*(g-g2)
                b3 = k*(b-b2)
                
                image.putpixel((i,j),(r3,g3,b3))
        image.save('image_exo2\image_déchiffrée_exo2.bmp')        
        image.show()

    ###Déroulement d'un masquage###
    
    def masquageComplet(self):
        giveImage = filedialog.askopenfilename(title = 'Sélectionnez une image' ,filetypes = self.__format)
        image = PIL.Image.open(giveImage)
        k = self.__k
        key = self.keyCreate(image.size[0],image.size[1])
        self.masquage(image,key,k)

Exo2()
