class Piece:
    def __init__(self,coordX,coordY):
        self.nom= "pièce"
        self.afficher ="affichage"
        self.coordonneX=coordX
        self.coordonneY=coordY

    def get_affichage(self):
        return self.afficher