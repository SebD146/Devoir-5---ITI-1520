import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'numpy'])

# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip',
'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print(installed_packages)

import numpy as np

global messageGagnantX
global messageGagnantO
messageGagnantX = 'Le joueur X a gagné le match.'
messageGagnantO = 'Le joueur O a gagné le match.'

def effaceTableau (tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

    # a completer
   
   tab = np.array([['-','-','-'],['-','-','-'],['-','-','-']])

    # retourne rien

      
def verifieGagner(tab):  
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''
    if testLignes(tab) == messageGagnantX or testLignes(tab) == messageGagnantO:
       return True
    if testCols(tab) == messageGagnantX or testCols(tab) == messageGagnantO:
       return True
    if testDiags(tab) == messageGagnantX or testDiags(tab) == messageGagnantO:
       return True
   
    # a completer
   
    return False  # a changer

 
def testLignes(tab):
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer

   if tab[0,0] == 'X' and tab[0,1] == 'X' and tab[0,2] == 'X':
      return messageGagnantX
   elif tab[1,0] == 'X' and tab[1,1] == 'X' and tab[1,2] == 'X':
      return messageGagnantX
   elif tab[2,0] == 'X' and tab[2,1] == 'X' and tab[2,2] == 'X':
      return messageGagnantX
   elif tab[0,0] == 'O' and tab[0,1] == 'O' and tab[0,2] == 'O':
      return messageGagnantO
   elif tab[1,0] == 'O' and tab[1,1] == 'O' and tab[1,2] == 'O':
      return messageGagnantO
   elif tab[2,0] == 'O' and tab[2,1] == 'O' and tab[2,2] == 'O':
      return messageGagnantO

   return '-'


def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer

   if tab[0,0] == 'X' and tab[1,0] == 'X' and tab[2,0] == 'X':
      return messageGagnantX
   elif tab[0,1] == 'X' and tab[1,1] == 'X' and tab[2,1] == 'X':
      return messageGagnantX
   elif tab[0,2] == 'X' and tab[1,2] == 'X' and tab[2,2] == 'X':
      return messageGagnantX
   elif tab[0,0] == 'O' and tab[1,0] == 'O' and tab[2,0] == 'O':
      return messageGagnantO
   elif tab[0,1] == 'O' and tab[1,1] == 'O' and tab[2,1] == 'O':
      return messageGagnantO
   elif tab[0,2] == 'O' and tab[1,2] == 'O' and tab[2,2] == 'O':
      return messageGagnantO

   return '-'
   
def testDiags(tab):
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   
   if tab[0,0] == 'X' and tab[1,1] == 'X' and tab[2,2] == 'X':
      return messageGagnantX
   if tab[0,2] == 'X' and tab[1,1] == 'X' and tab[2,0] == 'X':
      return messageGagnantX
   if tab[0,0] == 'O' and tab[1,1] == 'O' and tab[2,2] == 'O':
      return messageGagnantO
   if tab[0,2] == 'O' and tab[1,1] == 'O' and tab[2,0] == 'O':
      return messageGagnantO

   return '-'   # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

  
  
def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
   # a completer
   count = 0
   for i in range(0,10):
      if i in cases_occupe:
         count += 1
      else: continue
   
   if count == 9:
      return True

   return False



def joue():
   tab = np.array([['-','-','-'],['-','-','-'],['-','-','-']])
   """
   INDEX GUIDE:
   [[(0,0), (0,1), (0,2)]
    [(1,0), (1,1), (1,2)]
    [(2,0), (2,1), (2,2)]]
   """
   global cases_occupe
   cases_occupe = []
   print(tab)
   while True:
      if verifieGagner(tab) == True:
         print('Match terminée.')
         if testCols(tab) == messageGagnantX or testDiags(tab) == messageGagnantX or testLignes(tab) == messageGagnantX:
            print(messageGagnantX)
         elif testCols(tab) == messageGagnantO or testDiags(tab) == messageGagnantO or testLignes(tab) == messageGagnantO:
            print(messageGagnantO)
         effaceTableau(tab)
         tab = np.array([['-','-','-'],['-','-','-'],['-','-','-']])
         cases_occupe = []
         continue

      if testMatchNul(tab) == True:
         print('Match terminée.')
         print('Le match est nul.')
         tab = np.array([['-','-','-'],['-','-','-'],['-','-','-']])
         cases_occupe = []
         continue

      while True:
         print('[1,2,3]', '\n'  '[4,5,6]', '\n' '[7,8,9]')
         case = int(input('Choisis le nombre de votre case (joueur X): '))

         if case in cases_occupe:
            print('Cette case est deja occupée.')
            continue

         else:
            if case == 1:
               tab[0,0] = 'X'
               cases_occupe.append(case)
            if case == 2:
               tab[0,1] = 'X'
               cases_occupe.append(case)
            if case == 3:
               tab[0,2] = 'X'
               cases_occupe.append(case)
            if case == 4:
               tab[1,0] = 'X'
               cases_occupe.append(case)
            if case == 5:
               tab[1,1] = 'X'
               cases_occupe.append(case)
            if case == 6:
               tab[1,2] = 'X'
               cases_occupe.append(case)
            if case == 7:
               tab[2,0] = 'X'
               cases_occupe.append(case)
            if case == 8:
               tab[2,1] = 'X'
               cases_occupe.append(case)
            if case == 9:
               tab[2,2] = 'X'
               cases_occupe.append(case)
         print(cases_occupe)
         print(tab)
         break

      if verifieGagner(tab) == True:
         print('Match terminée.')
         if testCols(tab) == messageGagnantX or testDiags(tab) == messageGagnantX or testLignes(tab) == messageGagnantX:
            print(messageGagnantX)
         elif testCols(tab) == messageGagnantO or testDiags(tab) == messageGagnantO or testLignes(tab) == messageGagnantO:
            print(messageGagnantO)
         effaceTableau(tab)
         tab = np.array([['-','-','-'],['-','-','-'],['-','-','-']])
         cases_occupe = []
         continue

      if testMatchNul(tab) == True:
         print('Match terminée.')
         print('Le match est nul.')
         tab = np.array([['-','-','-'],['-','-','-'],['-','-','-']])
         cases_occupe = []
         continue

      while True:
         print('[1,2,3]', '\n'  '[4,5,6]', '\n' '[7,8,9]')
         case = int(input('Choisis le nombre de votre case (joueur O): '))
         if case in cases_occupe:
            print('Cette case est deja occupée.')
            continue
         else:
            if case == 1:
               tab[0,0] = 'O'
               cases_occupe.append(case)
            if case == 2:
               tab[0,1] = 'O'
               cases_occupe.append(case)
            if case == 3:
               tab[0,2] = 'O'
               cases_occupe.append(case)
            if case == 4:
               tab[1,0] = 'O'
               cases_occupe.append(case)
            if case == 5:
               tab[1,1] = 'O'
               cases_occupe.append(case)
            if case == 6:
               tab[1,2] = 'O'
               cases_occupe.append(case)
            if case == 7:
               tab[2,0] = 'O'
               cases_occupe.append(case)
            if case == 8:
               tab[2,1] = 'O'
               cases_occupe.append(case)
            if case == 9:
               tab[2,2] = 'O'
               cases_occupe.append(case)
         print(cases_occupe)
         print(tab)
         break

joue()

