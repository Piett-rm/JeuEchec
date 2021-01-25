from piece import Piece

class DameB(Piece):
    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.afficher = "D"

    def get_possible_stroke(self,tableau):

        possible_stroke = []

        #deplacement roi mais pour dame
        if self.coordonneY-1>=0:
            if tableau[self.coordonneY-1][self.coordonneX]==" ": #peut se déplacer s'il y a du vide
                possible_stroke.append((self.coordonneX,self.coordonneY-1))
            else:
                if tableau[self.coordonneY-1][self.coordonneX] in ["p", "r", "d", "f", "t", "c"]:
                    possible_stroke.append((self.coordonneX,self.coordonneY-1))

        if self.coordonneY+1<8:
            if tableau[self.coordonneY+1][self.coordonneX]==" ":
                possible_stroke.append((self.coordonneX,self.coordonneY+1))
            else:
                if tableau[self.coordonneY+1][self.coordonneX] in ["p", "r", "d", "f", "t", "c"]:
                    possible_stroke.append((self.coordonneX,self.coordonneY+1))
        
        if self.coordonneX+1<8:
            if tableau[self.coordonneY][self.coordonneX+1]==" ":
                possible_stroke.append((self.coordonneX+1,self.coordonneY))
            else:
                if tableau[self.coordonneY][self.coordonneX+1] in ["p", "r", "d", "f", "t", "c"]:
                    possible_stroke.append((self.coordonneX+1,self.coordonneY))

        if self.coordonneX-1>=0:
            if tableau[self.coordonneY][self.coordonneX-1]==" ":
                possible_stroke.append((self.coordonneX-1,self.coordonneY))
            else:
                if tableau[self.coordonneY][self.coordonneX-1] in ["p", "r", "d", "f", "t", "c"]:
                    possible_stroke.append((self.coordonneX-1,self.coordonneY))

        if self.coordonneX-1>=0 and self.coordonneY - 1>=0 :
            if tableau[self.coordonneY-1][self.coordonneX-1]==" ":
                possible_stroke.append((self.coordonneX-1,self.coordonneY-1))
            else:
                if tableau[self.coordonneY-1][self.coordonneX-1] in ["p", "r", "d", "f", "t", "c"]:
                    possible_stroke.append((self.coordonneX-1,self.coordonneY-1))

        if self.coordonneX-1>=0 and self.coordonneY + 1<8 :
            if tableau[self.coordonneY+1][self.coordonneX-1]==" ":
                possible_stroke.append((self.coordonneX-1,self.coordonneY+1))
            else:
                if tableau[self.coordonneY+1][self.coordonneX-1] in ["p", "r", "d", "f", "t", "c"]:
                    possible_stroke.append((self.coordonneX-1,self.coordonneY+1))
        
        if self.coordonneX+1<8 and self.coordonneY + 1<8 :
            if tableau[self.coordonneY+1][self.coordonneX+1]==" ":
                possible_stroke.append((self.coordonneX+1,self.coordonneY+1))
            else:
                if tableau[self.coordonneY+1][self.coordonneX+1] in ["p", "r", "d", "f", "t", "c"]:
                    possible_stroke.append((self.coordonneX+1,self.coordonneY+1))

        if self.coordonneX+1<8 and self.coordonneY - 1>=0 :
            if tableau[self.coordonneY-1][self.coordonneX+1]==" ":
                possible_stroke.append((self.coordonneX+1,self.coordonneY-1))
            else:
                if tableau[self.coordonneY-1][self.coordonneX+1] in ["p", "r", "d", "f", "t", "c"]:
                    possible_stroke.append((self.coordonneX+1,self.coordonneY-1))



        #deplaceement  fou mais pour dame
        for i in range(1,8):
            for i in range(1,8):
                if self.coordonneY-i>=0 and self.coordonneX+i<8:#pour en haut a droite 
                    if tableau[self.coordonneY-i][self.coordonneX+i]==" ": #peut se placer tant qu'il y a du vide
                        possible_stroke.append((self.coordonneX + i, self.coordonneY - i))
                    else:
                        if tableau[self.coordonneY-i][self.coordonneX+i]in ["p", "t", "c", "f", "r", "d"]:
                            possible_stroke.append((self.coordonneX + i, self.coordonneY - i))
                        break
    
        for i in range(1,8):
            for i  in range(1,8):
                if self.coordonneY+i<8 and self.coordonneX+i<8:#pour en bas a gauche
                    if tableau[self.coordonneY+i][self.coordonneX+i]==" ":
                        possible_stroke.append((self.coordonneX + i, self.coordonneY + i))
                    else:
                        if tableau[self.coordonneY+i][self.coordonneX+i]in ["p", "t", "c", "f", "r", "d"]:
                            possible_stroke.append((self.coordonneX + i, self.coordonneY + i))
                        break
        
        for i in range(1,8):
            for i  in range(1,8):
                if self.coordonneY+i<8 and self.coordonneX-i>=0:#pour en bas a droite 
                    if tableau[self.coordonneY+i][self.coordonneX-i]==" ":
                        possible_stroke.append((self.coordonneX-i, self.coordonneY + i))
                    else:
                        if tableau[self.coordonneY+i][self.coordonneX-i]in ["p", "t", "c", "f", "r", "d"]:
                            possible_stroke.append((self.coordonneX-i, self.coordonneY + i))
                        break

        for i in range(1,8):
            for i  in range(1,8):
                if self.coordonneY-i>=0 and self.coordonneX-i>=0:#pour en haut a gauche 
                    if tableau[self.coordonneY-i][self.coordonneX-i]==" ":
                        possible_stroke.append((self.coordonneX-i, self.coordonneY-i))
                    else:
                        if tableau[self.coordonneY-i][self.coordonneX-i]in ["p", "t", "c", "f", "r", "d"]:
                            possible_stroke.append((self.coordonneX-i, self.coordonneY +i))
                        break





        #deplaceement tour mais pour dame
        for i in range(1,8): #coup vers le haut
            if self.coordonneY-i>=0:
                if tableau[self.coordonneY-i][self.coordonneX]==" ":
                    possible_stroke.append((self.coordonneX,self.coordonneY-i))      

                else:
                    if tableau[self.coordonneY-i][self.coordonneX] in ["p", "r", "d", "f", "t", "c"]:
                        possible_stroke.append((self.coordonneX,self.coordonneY-i))               
                    break
        

        #coup de la tour en bas
        for i in range(1, 8):
            if self.coordonneY+i <8:
                if tableau[self.coordonneY+i][self.coordonneX] == " ":
                    possible_stroke.append((self.coordonneX, self.coordonneY+i))
                else:
                    if tableau[self.coordonneY+i][self.coordonneX] in ["p", "t", "c", "f", "r", "d"]:
                        possible_stroke.append((self.coordonneX, self.coordonneY+i))
                    break
            

        #coup de la tour a gauche
        for i in range(1, 8):  
            if self.coordonneX-i >=0:
                if tableau[self.coordonneY][self.coordonneX-i] == " ":
                    possible_stroke.append((self.coordonneX-i, self.coordonneY))
                else:
                    if tableau[self.coordonneY][self.coordonneX-i] in ["p", "t", "c", "f", "r", "d"]:
                        possible_stroke.append((self.coordonneX-i, self.coordonneY))
                    break
    
        #coup de la tour a droite
        for i in range(1, 8):
            if self.coordonneX+i <8:
                if tableau[self.coordonneY][self.coordonneX+i] == " ":
                    possible_stroke.append((self.coordonneX+i, self.coordonneY))
                else:
                    if tableau[self.coordonneY][self.coordonneX+i] in ["p", "t", "c", "f", "r", "d"]:
                        possible_stroke.append((self.coordonneX+i, self.coordonneY))
                    break

        return possible_stroke
