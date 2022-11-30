# Q1 John


# Q2 Seb

listeQ2 = [-2, 3, 0, 9, 6, -4, -1, 2]

def prodListePos_rec(liste, longueur):
    """
    (list)--->int
    Fonction recursive qui prend comme parametre une liste et le longueur de 
    la liste et retourne le produit des elements positifs dans la liste (>0).
    """

    if longueur <= 1:
        if longueur == 1:
            print(liste[0]) # REMOVE IN FINAL CODE
            return liste[0]
        elif longueur <= 1:
            print(1)
            return 1

    e1 = liste[longueur-1]

    e2 = liste[longueur-2]

    if e1 > 0 and e2 > 0:
        liste.append(e1*e2)
        liste.remove(e1)
        liste.remove(e2)
        return prodListePos_rec(liste, len(liste))
    else:
        if e1 <= 0:
            liste.remove(e1)
            return prodListePos_rec(liste, len(liste))
        elif e2 <= 0:
            liste.remove(e2)
            return prodListePos_rec(liste, len(liste))


#prodListePos_rec(listeQ2, len(listeQ2))
prodListePos_rec([1,-2,5,0,6,-5], len([1,-2,5,0,6,-5]))
prodListePos_rec([],len([]))