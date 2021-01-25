from piece import Piece

class CavalierB(Piece):
    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.afficher = "C"

    def get_possible_stroke(self, tableau):
        possible_stroke = []
        #vérifie que dans les coordonnées le cavalier peut se déplacer
        if self.coordonneX+1<8 and self.coordonneY-2>=0 and tableau[self.coordonneY-2][self.coordonneX+1] not in ["P", "R", "D", "F", "T", "C"]: #ne peut pas manger les pieces ["P", "R", "D", "F", "T", "C"]
            possible_stroke.append((self.coordonneX + 1, self.coordonneY - 2)) #il ajoute dans le cou possible
        if self.coordonneX-1>=0 and self.coordonneY-2>=0 and tableau[self.coordonneY-2][self.coordonneX-1] not in ["P", "R", "D", "F", "T", "C"]:
            possible_stroke.append((self.coordonneX - 1, self.coordonneY - 2))
        if self.coordonneX-1>=0 and self.coordonneY+2<8 and  tableau[self.coordonneY+2][self.coordonneX-1] not in ["P", "R", "D", "F", "T", "C"]:
            possible_stroke.append((self.coordonneX - 1, self.coordonneY + 2))
        if self.coordonneX+1<8 and self.coordonneY+2<8 and tableau[self.coordonneY+2][self.coordonneX+1] not in ["P", "R", "D", "F", "T", "C"]:
            possible_stroke.append((self.coordonneX + 1, self.coordonneY + 2))
        if  self.coordonneX+2<8 and self.coordonneY-1>=0 and tableau[self.coordonneY-1][self.coordonneX+2] not in ["P", "R", "D", "F", "T", "C"]:
            possible_stroke.append((self.coordonneX + 2, self.coordonneY - 1))
        if  self.coordonneX-2>=0 and self.coordonneY-1>=0  and tableau[self.coordonneY- 1][self.coordonneX-2] not in ["P", "R", "D", "F", "T", "C"]:
            possible_stroke.append((self.coordonneX  -2, self.coordonneY - 1))
        if  self.coordonneX+1<8 and self.coordonneY+1<8 and tableau[self.coordonneY+1][self.coordonneX + 2] not in ["P", "R", "D", "F", "T", "C"]:
            possible_stroke.append((self.coordonneX + 2, self.coordonneY + 1))
        if self.coordonneX-2>=0 and self.coordonneY+1<8 and tableau[self.coordonneY+1][self.coordonneX-2] not in ["P", "R", "D", "F", "T", "C"]:
            possible_stroke.append((self.coordonneX - 2, self.coordonneY + 1))

        return possible_stroke
