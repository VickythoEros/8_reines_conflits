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
    for i in T:
        m = 0
        for j in T:
            if i[0] == j[0] or i[1] == j[1] or abs(i[0] - j[0]) == abs(i[1] - j[1]):
                m +=1
        S += m -1
        #print(f" {i} : {m-1}")
    return S


def regeneration_s(T,n,l,c):
    """
    fonction permettant d'effectuer un decalage de 'l' ligne et 'c' colonne
    :param T: liste des positions des 8 reines
    :param n: la taille de la matrice
    :param l: le nombre de decalage en ligne
    :param c: le nombre de decalage en collone
    :return: new_T
    """
    new_T = []
    for i in T:
        li = (i[0] + l)%(n - 1) if (i[0] + l) > (n-1) else i[0] + l
        co = (i[1] + c)%(n - 1) if (i[1] + c) > (n-1) else i[1] + c
        new_T.append([li,co])
    return new_T


def _initialize(n):
     return [ [rd.randint(0,n-1),rd.randint(0,n-1)] for i in range(n) ]



def _show_queens_in_echec(matrice,T):
    for i in T:
        matrice[i[0], i[1]] = 1
    return matrice


if __name__ == '__main__':
    n = 8
    s = 0
    tables_values = []
    echequier = np.zeros((n,n)) # creation d'une matrice nxn remplie de zeros
    is_ok = False

    T = _initialize(n)
    #T = [[1, 1], [4, 0], [6, 6], [0, 1], [2, 3], [1, 0], [5, 6], [4, 6]]
    s = conflits(T)
    tables_values.append(s)

    while is_ok == False:
        T1 = regeneration_s(T,n,1,2)
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