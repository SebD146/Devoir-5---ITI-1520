# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','D','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]
     for i in p:
         if p.index(i)%2==0:
             donneur.append(i)
         elif p.index(i)%2==1:
             autre.append(i)


     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI

     
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    resultat=[]
    ordre = "A23456789DJQK"
    l.sort(key=lambda c:ordre.index(c[0]))
    liste = []
    liste2 = []

    # cree deux listes: un pour les numeros de cartes (liste), un pour les suits (liste2)
    for i in range(len(l)):
        string1 = l[i]
        string2 = string1[0]
        string3 = string1[1]
        liste.append(string2)
        liste2.append(string3)

    liste3 = []
    liste4 = []

    # elimine les paires de liste et met le reste dans un liste (liste4)
    # met les suits correspondents aux nombres dans liste4 dans un liste (liste3)
    for i in range(len(liste)):
        n = liste[i]
        n2 = liste2[i]
        count = liste.count(n)
        if n in liste4:
            continue
        else:
            if count % 2 == 1:
                liste4.append(n)
                liste3.append(n2)

    # combinent le nombre des cartes avec leur suit correspondent et les mettent dans resultat
    for i in range(len(liste4)):
        n3 = liste4[i]
        n4 = liste3[i]
        n5 = n3 + n4
        resultat.append(n5)     

    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
     
    

    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''
    print(p)

    

    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI

    

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     while True:
         global x
         x = int(input("Votre choix: "))
         if x <= n and x >= 1:
             x = x - 1
             return x
         else:
             print("S.V.P entrez une position valide.")
             continue
             
     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI

def joue():
     '''()->None
     Cette fonction joue le jeu'''

     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)
     print("Votre main est maintenant:")
     affiche_cartes(humain)
     print("\n")
     while True:
         if len(donneur) != 0 and len(humain) != 0:
             attend_le_joueur()
             print("A ton tour...")
             print("J'ai", len(donneur), "cartes dans ma main. Choisis-en une")
             cartesDonneur = len(donneur)
             entrez_position_valide(cartesDonneur)
             print("Vous avez choisis la carte ", x+1, ". C'est donc la carte: ", donneur[x], ". Je l'ajoute a votre main.", sep="")
             humain.append(donneur[x])
             donneur.pop(x)
             humain=elimine_paires(humain)
             print("Votre main est maintenant:")
             random.shuffle(humain)
             affiche_cartes(humain)
             print("\n")
         elif len(donneur) == 0 or len(humain) == 0:
             if len(humain)==0:
                 print("Felicitations! Vous avez gagner le jeux.")
                 break
             elif len(donneur)==0:
                 print("J'ai gagner le jeux. Meilleur chance la prochaine fois.")
                 break

         if len(donneur) != 0 and len(humain) != 0:
             attend_le_joueur()
             print("A mon tour...")
             choixRobot = random.randint(0, len(humain)-1)
             print("Je choisis la carte ", humain[choixRobot], ". Je l'ajoute a ma main.", sep="")
             donneur.append(humain[choixRobot])
             humain.pop(choixRobot)
             donneur=elimine_paires(donneur)
             print("Votre main est maintenant:")
             random.shuffle(donneur)
             affiche_cartes(humain)
             print("\n")
         elif len(donneur) == 0 or len(humain) == 0:
             if len(humain)==0:
                 print("Felicitations! Vous avez gagner le jeux.")
                 break
             elif len(donneur)==0:
                 print("J'ai gagner le jeux. Meilleur chance la prochaine fois.")
                 break

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
    

	 
# programme principale
joue()
