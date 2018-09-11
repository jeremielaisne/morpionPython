import tkinter
from tkinter import *
from morpion import Morpion
import sys

class TkAppM(Tk, Morpion):
    
    def __init__ (self):
        #appel Tkinter
        Tk.__init__(self)
        #appel classe de la fonction Morpion
        Morpion.__init__(self)
        self.title('TicTacToe')
        self.canv = Canvas(self, width=600, height=600, bg='#f5f5dc', bd=0)
        self.canv.pack()
        
        self.initializeGrid()
        self.initializeTk()
      

    def initializeTk(self):
        #creation de widget Tkinter Fils de Canvas
        lab01 = tkinter.Label(self, text='Morpion', bg='#f5f5dc', font=('serif',20,'bold'))
        self.canv.create_window(450,500, window=lab01)
        wid01 = tkinter.Button(self, text='Quit', command=self.quit)
        self.canv.create_window(570,570, window=wid01)
        wid02 = tkinter.Button(self, text='->')
        self.canv.create_window(530,570, window=wid02)
        wid03 = tkinter.Button(self, text='NewGame', command=self.newGame_M)
        self.canv.create_window(400,570, window=wid03)

        #decompte
        self.canv.create_text(120, 30, text=("Player 1 ",self.comptJ1), font='Bold 12', fill="blue")
        self.canv.create_text(380, 30, text=("Player 2 ",self.comptJ2), font='Bold 12', fill="red")
        self.canv.create_rectangle(50,510,220,540, fill="white")

        #le perdant de la precedente partie commence
        if self.boolM is 0:
            self.canv.create_text(140, 525, text="Player 1 start...", font='Arial 12', fill="blue")
        elif self.boolM is 1:
            self.canv.create_text(140, 525, text="Player 2 start...", font='Arial 12', fill="red")

        #action clic appel de fonction
        self.bind("<Button-1>", self.d_playM)

    def initializeGrid(self):
        for x in range (0,3):
            for y in range (0,3):
                self.canv.create_rectangle(200+x*100,100+y*100,300+x*100,200+y*100,width=4,fill='#ffff99')

    def display_crossM(self, x, y):
        #une croix est dessine
        self.canv.create_line(220+self.x*100,120+self.y*100,280+self.x*100,180+self.y*100, width=8 ,fill='red')
        self.canv.create_line(280+self.x*100,120+self.y*100,220+self.x*100,180+self.y*100, width=8 ,fill='red')

    def display_roundM(self, x, y):
        #un rond est dessine
        self.canv.create_oval(280+self.x*100,120+self.y*100,220+self.x*100,180+self.y*100, width=8 ,outline='blue')

    def d_playM(self, event):
        #reaction suite au clic delimite en pixel
        if event.y > 100 and event.y < 200:
            self.y = 0
        elif event.y > 200 and event.y < 300:
            self.y = 1
        elif event.y > 300 and event.y < 400:
            self.y = 2
            
        if event.x > 200 and event.x < 300:
            self.x = 0     
        elif event.x > 300 and event.x < 400:
            self.x = 1
        elif event.x > 400 and event.x < 500:
            self.x = 2
        self.console_M()
        
    def console_M(self):
        # indexNb apres calcul ligne et colonne situe l'emplacement sur la grille du clic
        self.indexNb = (self.x)+(self.y*3)
        # si l'emplacement est libre on joue et si l'indice est pair le perdant joue puis on avance indice de 1 (code repris de la classe morpion) 
        if self.grid[self.indexNb] == '-':
            if self.index2%2 == self.boolM:
                self.grid[self.indexNb] = 'O'
                self.tab[self.indexNb] = 1
                self.display_roundM(self.x, self.y)
            else:
                self.grid[self.indexNb] = 'X'
                self.tab[self.indexNb] = 2
                self.display_crossM(self.x, self.y)
            self.gridDisplay()
            self.index2 += 1
            self.canv.create_rectangle(50,510,220,540, fill="white")
        else:
            print ("case occupee")
            self.canv.create_text(160, 530, text="Case Occupee !!!!!!!", font='Bold 9', fill="black")
        #verification
        self.checkM()
        #si vainqueur apres coup precedent
        if self.winJ is 1:
            self.unbind("<Button-1>")
            self.canv.create_text(140, 525, text="Player 1 win!", font='Arial 12', fill="blue")
            self.boolM = 1
        elif self.winIA is 1:
            self.unbind("<Button-1>")
            self.canv.create_text(140, 525, text="Player 2 win!", font='Arial 12', fill="red")
            self.boolM = 0
        elif self.index2 is 9:
            self.unbind("<Button-1>")
            self.canv.create_text(140, 525, text="Pas de vainqueur", font='Arial 12', fill="black")

    def newGame_M(self):
        #nouvelle partie efface tout et recommence
        self.canv.delete("all")
        self.index2 = 0
        self.initGrid()
        self.initializeGrid()
        self.initializeTk()
        
        

            
#Main TkInter
if __name__ == "__main__":
    root1 = TkAppM()
    root1.geometry('600x600')
    root1.resizable(width=False, height=False)
    root1.mainloop()
