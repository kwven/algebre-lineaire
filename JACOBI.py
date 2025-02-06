from functions import *

def decomposition_jacobi(A, b, M):
    if est_diagonale_dominant(A)==False:
        return "erore"
    n = len(A)
    x = [0] * n
    for p in range(M):
        x_nouveau = copier(x)
        for i in range(n):
            somme =0
            for j in range(n):
                if j!=i:
                    somme+=A[i][j] * x[j]
            x_nouveau[i] = (b[i] - somme) / A[i][i]
        x = x_nouveau
    return x

#just enter your matix here and print this function