# MY IMPORTS
import numpy as np
import random as rd

# MY FUNCTIONS
def conflits(T):
    """
    Attend en parametre un tableau des emplacements des 8 REINES
    dans la matrice
    :param T:
    :return: S
    """
    S = 0
    n = len(T)
    for i in range(n):
        m = 0
        for j in range(n):
            if T[i] == T[j] or abs(i - j) == abs(T[i] - T[j]):
                m +=1
        S += m -1
        print(f" {i} : {m-1}")
    return S


def regeneration_s(T,l,c):
    """
    fonction permettant d'effectuer un decalage de 'l' ligne et 'c' colonne
    :param T: liste des positions des 8 reines
    :param n: la taille de la matrice
    :param l: le nombre de decalage en ligne
    :param c: le nombre de decalage en collone
    :return: new_T
    """
    n = len(T)
    new_T = [0 for i in range(n)]

    for i in range(n):
        li = (i + l)%(n - 1) if (i + l) > (n-1) else i + l
        co = (T[i] + c)%(n - 1) if (T[i] + c) > (n-1) else T[i] + c

        new_T[li] = co

    return new_T


def _initialize(n):

     return [ rd.randint(0,n-1) for i in range(n) ]



def _show_queens_in_echec(matrice,T):
    for i in range(len(T)):
        matrice[i, T[i]] = 1
    return matrice


if __name__ == '__main__':
    n = 8
    s = 0
    tables_values = []
    echequier = np.zeros((n,n)) # creation d'une matrice nxn remplie de zeros
    is_ok = False

    # initialisation
    #T = [7, 0, 1, 3, 1, 5, 2, 4]
    T = _initialize(n)
    print(T)
    s = conflits(T)
    tables_values.append(s)

    while is_ok == False:
        T1 = regeneration_s(T,1,2)
        print(T1)
        s1 = conflits(T1)
        if s1 > tables_values[-1] :
            is_ok = True
        else:
            T = T1
            tables_values.append(s1)


    print(T)
    print(tables_values)
    print(_show_queens_in_echec(echequier,T))