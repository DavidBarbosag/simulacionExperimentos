import Veccplx as vc
import math
import numpy as np


def boolto10(M):
    tamanofA = len(M)
    tamanocA = len(M[0])
    resultado = np.zeros((tamanofA, tamanocA))    
    
    for i in range(tamanofA):
        for j in range(tamanocA):
            if M[i][j] == True:
                resultado[i][j] = 1
            else:
                resultado[i][j] = 0

    return resultado

def resExp(M,v):
    tamanofA = len(M)
    tamanocA = len(M[0])
    tamanov = len([v])
    M10 = boolto10(M)
    resultado = np.zeros((0, tamanov))
    resultado = vc.multmat(M10,v)
    return resultado

A = np.array([
    [False, False, False, False, False, False],
    [False, False, False, False, False, False],
    [False, True, False, False, False, True],
    [False, False, False, True, False, False],
    [False, False, True, False, False, False],
    [True, False, False, False, True, False]
])

v = np.array([
    [6],
    [2],
    [1],
    [5],
    [3],
    [10]    
])
