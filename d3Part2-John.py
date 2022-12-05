# Jeu de cartes appelé "Pouilleux" 



# L'ordinateur est le donneur des cartes.



# Une carte est une chaine de 2 caractères. 

# Le premier caractère représente une valeur et le deuxième une couleur.

# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.

# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.

# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.

# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.



# Auteur : John Okito Olongo

# Date : 28 octobre 2022



import random

import copy



#-------------------------------------------- mes focntions -----------------------------------------------#

def nettoyerTab(tableau, formes):

    '''

    (list, list) -> list

    la fonctione prend deux list en paramètres. La première contient des nombres et des espaces

    la deuxème contient uniquement des couleurs. Elle crée une nouvelle liste en associant les numéros

    aux images correspondantes et retourne ce tableau. 

    '''

    nouveau = [] # tableau sans les espaces

    for i in range(len(tableau)):

        if(tableau[i] != " "): # on ne prend pas les cases vides

            nouveau.append(tableau[i]+formes[i]) 

    return nouveau





def separer(jeu, image):

    '''

    (list, bool) -> list

    La fonction prend une liste jeu qui contient des numéros et des images. Elle les sépare

    pour retourner un tableau contenant que des images ou des nombres. Selon le boolean en paramètres

    True = image et False = nombres

    '''

    

    numeros = copy.deepcopy(jeu) # stockage des numéros. D'abord copier le tableau en entrée de maière profonde

    couleurs = [] # stockages des formes

    

    for i in range(len(numeros)):

        couleurs.append(numeros[i][-1]) # ne garder que le dernier caractère

        numeros[i] = numeros[i][:-1] # garder tout sauf le dernier caractère

    if(image):

        return couleurs

    else:

        return numeros



def nombresMultiples(numeros):

    '''

    (list) -> list

    La fonction prend un tableau qui contient des nombres. Elle efface les numeros qui sont en pairs

    Elle retourne un tableau des espaces à l'index des numéros pairs effacés

    '''

    position = [] # la position des nombres

    compteur = [] # le nombre de fois que ces nombres apparaissent dans la liste

    intermediaire = []

    

    for i in range(len(numeros)):

        if(numeros.count(numeros[i]) > 1): #l e caractère est retrouvé à plusieurs endroit

            position.append(i)

            compteur.append(numeros.count(numeros[i]))



    for i in range(len(position)):

        if(compteur[i] % 2 != 0): #la carte se trouve plus de 2 fois dans la main. 

            if numeros[position[i]] not in intermediaire:

                intermediaire.append(numeros[position[i]])

            else:

                numeros[position[i]] = " " # supprimer la carte en laissant vide

        else:

            numeros[position[i]] = " " # supprimer la carte en laissant vide

    

    return numeros

#--------------------------------------------------------------------------------------------------------#



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

    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

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





     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS

     # AJOUTEZ VOTRE CODE ICI

     tour = False # false = autre, true = donneur

     for i in range(len(p)):

        if(tour):

             donneur.append(p[i]) # distribuer la carte actuelle

             tour = False # changer de personne à qui distribuer la prochaine carte

        else:

            autre.append(p[i])

            tour = True



     

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





    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS

    # AJOUTEZ VOTRE CODE ICI



    substitution = []

    couleur = [] #copier les couleurs





    substitution = separer(l, False) #séparer les nombres

    couleur = separer(l, True) #séparer les couleurs

    substitution = nombresMultiples(substitution) #nettoye

    resultat = nettoyerTab(substitution, couleur) #le tableau 

     

    



    random.shuffle(resultat)

    return resultat





def affiche_cartes(p):

    '''

    (list)-None

    Affiche les éléments de la liste p séparées par d'espaces

    '''



    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS

    # AJOUTEZ VOTRE CODE ICI

    for i in range(len(p)): #parcourir la longueur de toutes les cartes

        print(p[i], end = " ") #afficher les cartes avec un espace à la fin



    print("\n") #un sauf à la ligne pour le rendu visuel

    



def entrez_position_valide(n):

     '''

     (int)->int

     Retourne un entier du clavier, de 1 à n (1 et n inclus).

     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]

     

     Précondition: n>=1

     '''



     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS

     # AJOUTEZ VOTRE CODE ICI

     juste = False

     choix = 0

     while(juste != True):

         print("SVP entrez un entier de 1 à " + str(n) + ": ", end ='')

         choix = int(input())

         if(choix >= 1 and choix <= n):

             juste = True         

     return choix

     



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



     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS

     # AJOUTEZ VOTRE CODE ICI



     tour = True # True pour humain, False pour robot.

     jouer = True # à False, la partie s'arrête

     while(jouer):

         if(tour): # le tour de l'humain

             print("Votre tour.")

             print("Votre main est:")

             affiche_cartes(humain)

             print("J'ai", len(donneur), "cartes si 1 est ma première carte et", len(donneur), "la position de ma dernière carte, laquelle de mes cartes voulez-vous?")

             choisir = entrez_position_valide(len(donneur))

             if(choisir != 1):

                 print("Vous avez demandé ma", str(choisir) + "ème carte.")

             else:

                 print("Vous avez demandé ma", str(choisir) + "ère carte.")

             print("La voilà. C'est un ", donneur[choisir-1])

             print("Avec ", donneur[choisir-1], "ajouté, votre main est:")

             humain.append(donneur[choisir-1])

             del donneur[choisir-1] #retirer la carte chez le robot

             affiche_cartes(humain)

             print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")

             humain=elimine_paires(humain)

             affiche_cartes(humain)

             attend_le_joueur()

             tour = False # on change de joueur

         else: # le tour du robot

             print("Mon tour")

             prendre = random.randint(1,len(humain)) #tirer un nombre au hasard entre 1 et le nombre de cartes de l'humain

             if(prendre != 1):

                 print("J'ai pris votre ", str(prendre) + "ème carte.")

             else:

                 print("J'ai pris votre", str(prendre) + "ère carte.")

             donneur.append(humain[prendre-1]) #prendre la carte et l'ajouter au donneur

             del humain[prendre-1]

             donneur = elimine_paires(donneur)

             tour = True

         if(len(humain) == 0 and len(donneur) == 1) : #vérifier si c'est la fin du jeu

             attend_le_joueur()

             print("J'ai terminé toutes les cartes. \nFélicitations! Vous humain, vous avez gagné.")

             jouer = False #fin du jeu

         elif(len(donneur) == 0 and len(humain) == 1): 

             print("J'ai terminé toutes les cartes. \nVous avez perdu! Moi, Robot, j'ai gagné.")

             jouer = False #fin du jeu

             

    

# programme principale

joue()