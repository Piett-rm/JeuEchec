from piece import Piece

class FouN(Piece):
    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.afficher = "f"

    def get_possible_stroke(self,tableau):
        possible_stroke = []
        for i in range(1,8):
            if self.coordonneY-i>=0 and self.coordonneX+i<8:#pour en haut a droite 
                if tableau[self.coordonneY-i][self.coordonneX+i]==" ":#peut se placer tant qu'il y a du vide
                    possible_stroke.append((self.coordonneX + i, self.coordonneY - i))
                else:
                    if tableau[self.coordonneY-i][self.coordonneX+i]in ["P", "R", "D", "F", "T", "C"]:  #ne peut pas manger les pièces ["P", "R", "D", "F", "T", "C"]
                        possible_stroke.append((self.coordonneX + i, self.coordonneY - i))
                    break
    
        for i in range(1,8):
            if self.coordonneY+i<8 and self.coordonneX+i<8:#pour en bas a gauche
                if tableau[self.coordonneY+i][self.coordonneX+i]==" ":
                    possible_stroke.append((self.coordonneX + i, self.coordonneY + i))
                else:
                    if tableau[self.coordonneY+i][self.coordonneX+i]in ["P", "R", "D", "F", "T", "C"]:
                        possible_stroke.append((self.coordonneX + i, self.coordonneY + i))
                    break
        
        for i in range(1,8):
            if self.coordonneY+i<8 and self.coordonneX-i>=0:#pour en bas a droite 
                if tableau[self.coordonneY+i][self.coordonneX-i]==" ":
                    possible_stroke.append((self.coordonneX-i, self.coordonneY + i))
                else:
                    if tableau[self.coordonneY+i][self.coordonneX-i]in ["P", "R", "D", "F", "T", "C"]:
                        possible_stroke.append((self.coordonneX-i, self.coordonneY + i))
                    break

        for i in range(1,8):
            if self.coordonneY-i>=0 and self.coordonneX-i>=0:#pour en haut a gauche 
                if tableau[self.coordonneY-i][self.coordonneX-i]==" ":
                    possible_stroke.append((self.coordonneX-i, self.coordonneY-i))
                else:
                    if tableau[self.coordonneY-i][self.coordonneX-i]in ["P", "R", "D", "F", "T", "C"]:
                        possible_stroke.append((self.coordonneX-i, self.coordonneY +i))
                    break

        return possible_stroke
