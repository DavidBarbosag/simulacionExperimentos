import unittest
import canicasBool as cb
import math
import numpy as np
import multRendProb as mr
import multRendCuan as mc
import __main__
import matplotlib
import matplotlib.pyplot as plt
import Veccplx as vc

prueba = 0


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
res = np.array([
    [ 0.+0.j],
    [ 0.+0.j],
    [12.+0.j],
    [ 5.+0.j],
    [ 1.+0.j],
    [ 9.+0.j]
])

# Matriz de probabilidad de los objetivos
M = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1/3, 0, 1, 0, 0, 0, 0],
    [0, 1/3, 0, 0, 1, 0, 0, 0],
    [0, 1/3, 1/3, 0, 0, 1, 0, 0],
    [0, 0, 1/3, 0, 0, 0, 1, 0],
    [0, 0, 1/3, 0, 0, 0, 0, 1]
])
# Matriz de estados
X = np.array([
    [1],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0]
])
# Numero de objetivos
nO = 5
# Numero de rendijas
nR = 2

resRenProb = np.array([
    [0.+0.j],
    [0.+0.j],
    [0.+0.j],
    [1/6+0.j],
    [1/6+0.j],
    [1/3+0.j],
    [1/6+0.j],
    [1/6+0.j]
])

# Matriz probabilidades experimento cuantico
N = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1/(2)**0.5, 0, 0, 0, 0, 0, 0, 0],
    [1/(2)**0.5, 0, 0, 0, 0, 0, 0, 0],
    [0, (-1+1j)/(6)**0.5, 0, 1, 0, 0, 0, 0],
    [0, (-1-1j)/(6)**0.5, 0, 0, 1, 0, 0, 0],
    [0, (1-1j)/(6)**0.5, (-1+1j)/(6)**0.5, 0, 0, 1, 0, 0],
    [0, 0, (-1-1j)/(6)**0.5, 0, 0, 0, 1, 0],
    [0, 0, (1-1j)/(6)**0.5, 0, 0, 0, 0, 1]
])
# REsultado deseado experimento cuantico
resRenCuan = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1/6, 1/3, 0, 1, 0, 0, 0, 0],
    [1/6, 1/3, 0, 0, 1, 0, 0, 0],
    [0, 1/3, 1/3, 0, 0, 1, 0, 0],
    [1/6, 0, 1/3, 0, 0, 0, 1, 0],
    [1/6, 0, 1/3, 0, 0, 0, 0, 1]
])
# Numero de objetivos
nOc = 5
# Numero de rendijas
nRc = 2

# Pruebas
# Prueba canicas booleanas
if np.array_equal(res,cb.resExp(A,v)):
    resultado = True
    prueba = prueba + 1
else:
    resultado = False
# Prueba experimento multiples rendijas probabilistico 
if np.array_equal(resRenProb,mr.resExp(M,X,nR,nO)):
    prueba = prueba + 1
else:
    prueba = prueba
# Prueba experimento multiples rendijas cuantico 
# Hay un problema con los decimales debido a esto la prueba sale negativa
if np.array_equal(resRenCuan,mc.resExp(N, nRc, nOc)):
    prueba = prueba + 1
else:
    prueba = prueba

ejex = [0, 0, 0, 1/6, 1/6, 1/3, 1/6, 1/6]
ejey = ['1', '2', '3', '4', '5', '6', '7', '8']

fig, ax = plt.subplots()
ax.set_ylabel('Probabilidad')
ax.set_xlabel('Posicion')
plt.bar(ejey, ejex)
plt.savefig('grafica.png')
plt.show()

if __name__ == "__main__":
    print("Numero de pruebas aprobadas",prueba)
