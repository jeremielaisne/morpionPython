class Morpion():
    
    def __init__(self):
        self.index = 0
        self.indexNb = 0
        self.index2 = 0
        self.boolM = 0

        self.comptJ1 = 0
        self.comptJ2 = 0
        self.grid = []
        self.tab = []
        for i in range (0 ,3):
            print ('\n')
            for j in range (0 ,3):
                self.grid.append('-')
                self.tab.append(0)
                print (self.grid[j]),
        print ('\n')


    def initGrid(self):
        for i in range (0, 9):
            self.grid[i] = '-'
            self.tab[i] = 0
        self.winJ = 0
        self.winIA = 0
        
    def gridDisplay(self):
        print ('\n')
        for self.index in range (0 ,9):
            if self.index !=0 and self.index%3 == 0:
                print ('\n')
            print (self.grid[self.index]),

    def tourM(self, index):
        self.indexNb  = input('Choisir un emplacement ! : ')
        if self.grid[self.indexNb] == '-':
            if self.index%2 == 0:
                self.grid[self.indexNb] = 'O'
                self.tab[self.indexNb] = 1 
            else:
                self.grid[self.indexNb] = 'X'
                self.tab[self.indexNb] = 2 
        else:
            print ('place occupee !')
            self.tourM(self.index)
        self.gridDisplay()

    def checkM(self):
        for i in range (0, 9):
            self.winJ = 0
            self.winIA = 0
            #lignes
            if i<7:
                if self.tab[i] == self.tab[i+1] == self.tab[i+2] == 1 and i%3 == 0:
                    self.winJ = 1
                    break
                elif self.tab[i] == self.tab[i+1] == self.tab[i+2] == 2 and i%3 == 0:
                    self.winIA = 1
                    break
            #colonnes
            if i<3:
                if self.tab[i] == self.tab[i+3] == self.tab[i+6] == 1:
                    self.winJ = 1
                    break
                elif self.tab[i] == self.tab[i+3] == self.tab[i+6] == 2:
                    self.winIA = 1
                    break
            #diagonales
            if self.tab[0] == self.tab[4] == self.tab[8] == 1 or self.tab[2] == self.tab[4] == self.tab[6] == 1:
                self.winJ = 1
                break
            elif self.tab[0] == self.tab[4] == self.tab[8] == 2 or self.tab[2] == self.tab[4] == self.tab[6] == 2:
                self.winIA = 1
                break
        #verif
        if self.winJ is 1:
            print ('\n joueur 1 a gagne ! \n')
            self.comptJ1 += 1
        elif self.winIA  is 1:
            print ('\n joueur 2 a gagne ! \n')
            self.comptJ2 += 1
            
    def playM(self):
        for self.index in range (1 ,9):
            self.tourM(self.index)
            self.checkM()
            if self.winJ is 1 or self.winIA  is 1:
                break
        self.gridDisplay()
        print ('\n fin du jeu !')
        


if __name__ == "__main__":
    morpion01 = Morpion()
    morpion01.playM()
