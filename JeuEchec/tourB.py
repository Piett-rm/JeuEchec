from piece import Piece

class TourB(Piece):
    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.afficher = "T"
        self.couleur = "blanc"

    def get_possible_stroke(self, tableau):
        possible_stroke = []
      
        for i in range(1,8): #coup vers le haut
            if self.coordonneY-i>=0:
                if tableau[self.coordonneY-i][self.coordonneX]==" ":#peut se placer tant qu'il y a du vide
                    possible_stroke.append((self.coordonneX,self.coordonneY-i))      

                else:
                    if tableau[self.coordonneY-i][self.coordonneX] in ["p", "r", "d", "f", "t", "c"]: #ne peut pas manger les  pièces ["p", "r", "d", "f", "t", "c"]
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

