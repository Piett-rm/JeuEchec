from board import Board
if __name__ == "__main__":
    try:
        compteur=1
        ECHEC = False
        BoardavecPiece=Board()
        BoardavecPiece.affichertableau()

        while True :
            if compteur==1:
                print("!!!!!!!Joueur blanc a toi de jouer tu as les pions en Majuscules!!!!!!!")
                compteur=compteur+1
            else:
                print("!!!!!!!Joueur noir a toi de jouer tu as les pions en Minuscules!!!!!!!")
                compteur=1
            ECHEC = BoardavecPiece.demander_coup()
            if ECHEC:
                print("Fin de partie")
                break
            BoardavecPiece.piece_placer()
            BoardavecPiece.affichertableau()
    except Exception as exc:
        print("Mon Erreur: ", exc)