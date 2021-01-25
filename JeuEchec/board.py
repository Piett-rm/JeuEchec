from pionB import PionB
from pionN import PionN
from tourB import TourB
from tourN import TourN
from cavalierB import CavalierB
from cavalierN import CavalierN
from fouB import FouB
from fouN import FouN
from dameB import DameB
from dameN import DameN
from roiB import RoiB
from roiN import RoiN


class Board:
    def __init__(self):
        self.tableau = []
        self.creertableau()
        self.dico_lettre = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7} 
        self.dico_chiffre = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7}
        self.PionBlanc1 = PionB(0, 6) #pion  blanc se place en  0,6
        self.PionBlanc2 = PionB(1, 6) #pion  blanc se place
        self.PionBlanc3 = PionB(2, 6) #pion  blanc se place
        self.PionBlanc4 = PionB(3, 6) #pion  blanc se place
        self.PionBlanc5 = PionB(4, 6) #pion  blanc se place
        self.PionBlanc6 = PionB(5, 6) #pion  blanc se place
        self.PionBlanc7 = PionB(6, 6) #pion  blanc se place
        self.PionBlanc8 = PionB(7, 6) #pion  blanc se place

        self.PionNoir1 = PionN(0, 1) #pion noir se place en 
        self.PionNoir2 = PionN(1, 1) #pion  noir se place
        self.PionNoir3 = PionN(2, 1) #pion  noir se place
        self.PionNoir4 = PionN(3, 1) #pion  noir se place
        self.PionNoir5 = PionN(4, 1) #pion  noir se place
        self.PionNoir6 = PionN(5, 1) #pion  noir se place
        self.PionNoir7 = PionN(6, 1) #pion  noir se place
        self.PionNoir8 = PionN(7, 1) #pion  noir se place

        self.TourBlanc1 = TourB(0, 7) #la tour blanche se place en 0, 7
        self.TourBlanc2 = TourB(7, 7) #la tour blanche

        self.TourNoir1 = TourN(0, 0) #la tour noir se place en 0, 0
        self.TourNoir2 = TourN(7, 0) #la tour noir se place

        self.CavalierBlanc1 = CavalierB(1, 7)#le cavalier blanc se place en 1,7
        self.CavalierBlanc2 = CavalierB(6, 7) #le cavalier blanc

        self.CavalierNoir1 = CavalierN(1, 0)  #le cavalier noir se place en 1,0
        self.CavalierNoir2 = CavalierN(6, 0)  #le cavalier noir se place en 

        self.FouBlanc1 = FouB(2, 7) #le fou blanc se place en 2,7
        self.FouBlanc2 = FouB(5, 7) #le fou blanc

        self.FouNoir1 = FouN(2, 0) #le fou noir se place en 2,0
        self.FouNoir2 = FouN(5, 0) #le fou noir

        self.RoiBlanc = RoiB(3, 7) #le roi blanc se place en 3,7
        self.RoiNoir = RoiN(3, 0)   #le roi noir se place 

        self.DameBlanc = DameB(4, 7) #la dame blanche se place en 4,7
        self.DameNoir = DameN(4, 0)  #la dame noir se place en 

        #le tableau regroupe toute les pièces dans la grille
        self.tablesdespieces = [self.PionBlanc1, self.PionBlanc2, self.PionBlanc3, self.PionBlanc4, self.PionBlanc5,
                                self.PionBlanc6, self.PionBlanc7, self.PionBlanc8, self.PionNoir1, self.PionNoir2,
                                self.PionNoir3, self.PionNoir4, self.PionNoir5, self.PionNoir6, self.PionNoir7,
                                self.PionNoir8, self.TourBlanc1, self.TourBlanc2, self.TourNoir1, self.TourNoir2,
                                self.CavalierBlanc1, self.CavalierBlanc2, self.CavalierNoir1, self.CavalierNoir2,
                                self.FouBlanc1, self.FouBlanc2, self.FouNoir1, self.FouNoir2, self.RoiBlanc,
                                self.RoiNoir, self.DameBlanc, self.DameNoir]
        
        self.piece_placer()

    def creertableau(self):#
        for i in range(8):
            self.tableau.append([" ", " ", " ", " ", " ", " ", " ", " "])

    def affichertableau(self): #permet l'affichage de l'échiquier
        nombre = 9

        colonne = " " + " A" + " B" + " C" + " D" + " E" + " F" + " G" + " H"
        print(colonne)
        for i in self.tableau:
            nombre = nombre - 1
            ligne = str(nombre) + " "
            for j in i:
                ligne = ligne + str(j) + " "
            print(ligne)



    def is_saisie_correct(self, entree):# vérifie que la saisie est vraie.

        if len(entree) > 2 or len(entree) == 1: #si l'entrée est supérieur a 2 ou égal a 1 alors c'est faux 
            return False
        cles_lettres = self.dico_lettre.keys()
        cles_chiffres = self.dico_chiffre.keys()
        if entree[0].upper() in cles_lettres and entree[1] in cles_chiffres: #si l'entrée [0] donc la piece est dans la clé de de dico_lettre et l'entrée[1] donc le nombre est dans le dico_chiffre
            return True #retourne Vrai
        else:
            return False #retourne Faux

    def piece_placer(self): #peremt de placer les pièces
        print("Nombre de pieces sur l'échiquier  : "+ str(len(self.tablesdespieces))) #calcul le nombre de piece
        for piece in self.tablesdespieces: #les pieces dans le tableau des pièces
            self.tableau[piece.coordonneY][piece.coordonneX] = piece.afficher   #affiche aux coordonnees son affichage

    def demander_coup(self):
        ECHEC = False #permet de faire la condition de victoire
        while True:
            print("Quelle pièce veux tu bouger ? ")
            coupbouger = input() #permet d'avoir la pièce qu on veut bouger
            if self.is_saisie_correct(coupbouger): #j'appelle la fonction is_saisie_correct(): 
                break  # sort de la boucle
            else:
                print("tu as mal noté ! Réessayer ")
        lettre = self.dico_lettre[coupbouger[0].upper()] #le upper permet que ça fonctionne meme si le joueur met une minuscule    
        chiffre = self.dico_chiffre[coupbouger[1]]
        Pion_Case = self.PionsurCase(lettre, chiffre)
        if Pion_Case != None: #si la case qu on n'a pas choisi est nul alors on continue
            for possible_stroke in Pion_Case.get_possible_stroke(self.tableau): #verifie les coups possible
                print(f"Voici les coups possibles {possible_stroke}")

            while True:
                print("ou veux tu te déplacer? ") 
                coupdeplacement = input()
                if self.is_saisie_correct(coupdeplacement):
                    break  # sort de la boucle
                else:
                    print("tu as mal noté ! Réessayer ")


            lettre_deplacement = self.dico_lettre[coupdeplacement[0].upper()]
            chiffre_deplacement = self.dico_chiffre[coupdeplacement[1]]
            if  ((lettre_deplacement, chiffre_deplacement) in Pion_Case.get_possible_stroke(self.tableau)):#si c'est possible alors 
                print("coup possible")
                # Suppression de la pièce de la liste des pièces
                for Piece in self.tablesdespieces:                
                    if  (lettre_deplacement, chiffre_deplacement) == (Piece.coordonneX, Piece.coordonneY):
                        if Piece.afficher.upper() == "R":
                            print("Echec et Mat!!!!!!!!!")
                            ECHEC = True
                            break
                        self.tablesdespieces.remove(Piece)
                        print("pièce prise !")
                        break

                # Repositionnement de la pièce sur sa nouvelle case
                Pion_Case.coordonneX = lettre_deplacement
                Pion_Case.coordonneY = chiffre_deplacement
                print("le coup est possible")
                self.tableau[chiffre][lettre] = " "
        print(" pas de piece a cet endroit")
        return ECHEC


    def PionsurCase(self, x, y):#permet de retourner les coordonnées de la pièce
        for piece in self.tablesdespieces:
            if piece.coordonneX == x and piece.coordonneY == y:
                return piece
