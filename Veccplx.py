import numpy as np
import math
import cmath


def sumavec(v, w):
    tamano = len(v)
    suma = np.zeros(tamano, dtype=np.complex_)
    k = 0
    while k < tamano:
        suma[k] = v[k] + w[k]
        k = k + 1
    return suma


def invvec(v):
    tamano = len(v)
    resultado = np.zeros(tamano, dtype=np.complex_)
    k = 0
    while k < tamano:
        resultado[k] = v[k] * -1
        k = k + 1
    return resultado


def multescvec(v, c):
    tamano = len(v)
    resultado = np.zeros(tamano, dtype=np.complex_)
    k = 0
    while k < tamano:
        resultado[k] = v[k] * c
        k = k + 1
    return resultado


def sumamtx(A, B):
    tamanofA = len(A)
    tamanocA = len(A[0])
    tamanofB = len(B)
    tamanocB = len(B[0])
    if tamanofA != tamanocB and tamanocA != tamanofB:
        raise Exception('Incompatible types')
    else:
        suma = np.zeros((tamanofA, tamanocA), dtype=np.complex_)
        for j in range(tamanofA):
            for k in range(tamanocA):
                suma[j][k] = A[j][k] + B[j][k]
    return suma


def invmtx(A):
    tamanofA = len(A)
    tamanocA = len(A[0])
    resultado = np.zeros((tamanofA, tamanocA), dtype=np.complex_)
    for j in range(tamanofA):
        for k in range(tamanocA):
            resultado[j][k] = A[j][k] * -1

    return resultado


def multescmtx(A, c):
    tamanofA = len(A)
    tamanocA = len(A[0])
    resultado = np.zeros((tamanofA, tamanocA), dtype=np.complex_)
    for j in range(tamanofA):
        for k in range(tamanocA):
            resultado[j][k] = A[j][k] * c
    return resultado


def trans(A):
    tamanofA = len(A)
    tamanocA = len(A[0])
    resultado = np.zeros((tamanofA, tamanocA), dtype=np.complex_)
    for j in range(tamanofA):
        for k in range(tamanocA):
            resultado[j][k] = A[k][j]
    return resultado


def conj(A):
    tamanofA = len(A)
    tamanocA = len(A[0])
    resultado = np.zeros((tamanofA, tamanocA), dtype=np.complex_)
    for j in range(tamanofA):
        for k in range(tamanocA):
            resultado[j][k] = np.conjugate((A[j][k]))
    return resultado


def adj(A):
    tamanofA = len(A)
    tamanocA = len(A[0])
    resultado = np.zeros((tamanocA, tamanofA), dtype=np.complex_)
    for j in range(tamanocA):
        for k in range(tamanofA):
            resultado[j][k] = np.conjugate((A[k][j]))
    return resultado


def multmat(A, B):
    tamanofA = len(A)
    tamanocA = len(A[0])
    tamanofB = len(B)
    tamanocB = len(B[0])

    if tamanocA != tamanofB:
        raise Exception('Incompatible types')
    else:
        mult = np.zeros((tamanofA, tamanocB), dtype=np.complex_)
        for j in range(tamanofA):
            for k in range(tamanocB):
                for l in range(tamanofB):
                    mult[j][k] += A[j][l] * B[l][k]
    return mult


def accvec(A, x):
    tamanofA = len(A)
    tamanocA = len(A[0])
    tamanov = len(x[0])
    tamanovf = len(x)
    resultado = np.zeros((tamanofA, tamanov), dtype=np.complex_)
    for j in range(tamanofA):
        for k in range(tamanov):
            for l in range(tamanovf):
                resultado[j][k] += A[j][l] * x[l][k]
    return resultado

def prodint(A,B):
    tamanofA = len(A)
    tamanocA = len(A[0])
    tamanofB = len(B)
    tamanocB = len(B[0])
    m1 = np.zeros((tamanofA, tamanocB), dtype=np.complex_)
    j = 0
    resultado = np.complex_()
    if tamanocA == 1:
        m1 = multmat(adj(A),B)
        tamanom1f = len(m1)

        for j in range(tamanom1f):
            resultado = resultado + m1[j][j]
    else:

        m1 = multmat(adj(A),B)
        tamanom1f = len(m1)

        for j in range(tamanom1f):
            resultado = resultado + m1[j][j]


    return resultado





def norma(A):
    resultado = np.complex_()
    resultado = cmath.sqrt(prodint(A,A))
    return resultado


def dist(A,B):
    resultado = np.complex_()
    resultado = cmath.sqrt(prodint(A-B, A-B))
    return resultado

def hermi(A):


    return (A == adj(A))


def unit(A):
    tamanofA = len(A)
    tamanocA = len(A[0])

    m = np.zeros((tamanofA, tamanocA), dtype=np.complex_)
    m = A*adj(A)
    n = np.identity(tamanocA)

    if np.array_equal(m,n):
        resultado = True
    else:
        resultado = False


    return resultado

def prodtens(A,B):
    tamanofA = len(A)
    tamanocA = len(A[0])
    tamanofB = len(B)
    tamanocB = len(B[0])
    nfilas = tamanofA * tamanofB
    ncolumnas = tamanocA * tamanocB
    resultado = np.zeros((nfilas, ncolumnas), dtype=np.complex_)
    for j in range(nfilas):
        for k in range(ncolumnas):
            resultado[j][k] = A[j // tamanofB, k // tamanocB] * B[j % tamanofB, k % tamanocB]
    return resultado


#print(adj(x))
# if __name__ == '__main__':
#   print_hi('Pychars')