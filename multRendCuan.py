import Veccplx as vc
import math
import numpy as np



def resExp(M,nR,nT):
    tamanofM = len(M)
    tamanocM = len(M[0]) 
    mproren  = np.zeros((nR+nT+1, nR+nT+1))
    mop = np.zeros((nR+nT+1, nR+nT+1))
    mop = vc.multmat(M,M)
    for i in range(tamanofM):
        for j in range(tamanocM):
            mproren[i][j] = mop[i][j] * np.conjugate(mop[i][j])
    return mproren
