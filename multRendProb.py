import Veccplx as vc
import math
import numpy as np



def resExp(M,X,nR,nT):
    tamanofM = len(M)
    tamanocM = len(M[0])
    tamanocX = len(X[0])   
    numren = nR  
    probrend = 1/nR
    mproren = np.zeros((nR+nT+1, nR+nT+1))
    mop = np.zeros((nR+nT+1, nR+nT+1))
    resultado = resultado = np.zeros((nR+nT+1, nR+nT+1))

    for i in range(nR):
        mproren[i+1][0] = probrend

    mop = mproren + M
    resultado = vc.multmat(vc.multmat(mop,mop),X)
    return resultado
