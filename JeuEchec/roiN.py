from piece import Piece

class RoiN(Piece):
    def __init__(self,coordX,coordY):
        super().__init__(coordX,coordY)
        self.afficher="r"

    def get_possible_stroke(self,tableau):
        possible_stroke = []

        if self.coordonneY-1>=0:
            if tableau[self.coordonneY-1][self.coordonneX]==" ":
                possible_stroke.append((self.coordonneX,self.coordonneY-1))
            else:
                if tableau[self.coordonneY-1][self.coordonneX] in ["P", "R", "D", "F", "T", "C"]: #ne peut pas manger les pices ["P", "R", "D", "F", "T", "C"]
                    possible_stroke.append((self.coordonneX,self.coordonneY-1))

        if self.coordonneY+1<8:
            if tableau[self.coordonneY+1][self.coordonneX]==" ":
                possible_stroke.append((self.coordonneX,self.coordonneY+1))
            else:
                if tableau[self.coordonneY+1][self.coordonneX] in ["P", "R", "D", "F", "T", "C"]:
                    possible_stroke.append((self.coordonneX,self.coordonneY+1))
        
        if self.coordonneX+1<8:
            if tableau[self.coordonneY][self.coordonneX+1]==" ":
                possible_stroke.append((self.coordonneX+1,self.coordonneY))
            else:
                if tableau[self.coordonneY][self.coordonneX+1] in ["P", "R", "D", "F", "T", "C"]:
                    possible_stroke.append((self.coordonneX+1,self.coordonneY))

        if self.coordonneX-1>=0:
            if tableau[self.coordonneY][self.coordonneX-1]==" ":
                possible_stroke.append((self.coordonneX-1,self.coordonneY))
            else:
                if tableau[self.coordonneY][self.coordonneX-1] in ["P", "R", "D", "F", "T", "C"]:
                    possible_stroke.append((self.coordonneX-1,self.coordonneY))

        if self.coordonneX-1>=0 and self.coordonneY - 1>=0 :
            if tableau[self.coordonneY-1][self.coordonneX-1]==" ":
                possible_stroke.append((self.coordonneX-1,self.coordonneY-1))
            else:
                if tableau[self.coordonneY-1][self.coordonneX-1] in ["P", "R", "D", "F", "T", "C"]:
                    possible_stroke.append((self.coordonneX-1,self.coordonneY-1))

        if self.coordonneX-1>=0 and self.coordonneY + 1<8 :
            if tableau[self.coordonneY+1][self.coordonneX-1]==" ":
                possible_stroke.append((self.coordonneX-1,self.coordonneY+1))
            else:
                if tableau[self.coordonneY+1][self.coordonneX-1] in ["P", "R", "D", "F", "T", "C"]:
                    possible_stroke.append((self.coordonneX-1,self.coordonneY+1))
        
        if self.coordonneX+1<8 and self.coordonneY + 1<8 :
            if tableau[self.coordonneY+1][self.coordonneX+1]==" ":
                possible_stroke.append((self.coordonneX+1,self.coordonneY+1))
            else:
                if tableau[self.coordonneY+1][self.coordonneX+1] in ["P", "R", "D", "F", "T", "C"]:
                    possible_stroke.append((self.coordonneX+1,self.coordonneY+1))

        if self.coordonneX+1<8 and self.coordonneY - 1>=0 :
            if tableau[self.coordonneY-1][self.coordonneX+1]==" ":
                possible_stroke.append((self.coordonneX+1,self.coordonneY-1))
            else:
                if tableau[self.coordonneY-1][self.coordonneX+1] in ["P", "R", "D", "F", "T", "C"]:
                    possible_stroke.append((self.coordonneX+1,self.coordonneY-1))

        return possible_stroke