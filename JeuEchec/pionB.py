from piece import Piece

class PionB(Piece):
    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.afficher = "P"


    def get_possible_stroke(self, tableau):
        possible_stroke = []

        if self.coordonneY-1>=0 and  tableau[self.coordonneY-1][self.coordonneX] not in ["P", "R", "D", "F", "T", "C"]: #ne peut pas manger les pièces ["P", "R", "D", "F", "T", "C"]
            deplacement_possible = (self.coordonneX, self.coordonneY - 1)
            if self.coordonneY-1>=0 and tableau[self.coordonneY-1][self.coordonneX]==" ":
                possible_stroke.append(deplacement_possible)
            if self.afficher== tableau[self.coordonneY][6]:
                if self.coordonneY-1>=0 and tableau[self.coordonneY-2][self.coordonneX]==" ":
                    possible_stroke.append((self.coordonneX,self.coordonneY-2))
            if  self. coordonneY-1>=0 and self.coordonneX-1>=0 and tableau[self.coordonneY-1][self.coordonneX-1]!=" ":
                possible_stroke.append((self.coordonneX-1,self.coordonneY-1))
            if  self. coordonneY-1>=0 and self.coordonneX+1<8 and tableau[self.coordonneY-1][self.coordonneX+1]!=" ":
                possible_stroke.append((self.coordonneX+1,self.coordonneY-1))
        
        return possible_stroke

