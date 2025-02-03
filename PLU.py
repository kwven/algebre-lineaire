from functions import *
from LU import resoudre_lu

def plu_decomposition(A):
    n = len(A)
    P = matrice_identite(n)
    L = matrice_identite(n)
    U = [[A[i][j] for j in range(n)] for i in range(n)]

    for k in range(n-1):
        index_pivot = trouver_pivot_max(U, k, n)
        if index_pivot != k:
            echanger_lignes(U, k, index_pivot)
            echanger_lignes(P, k, index_pivot)
            if k > 0:
                for j in range(k):
                    L[k][j], L[index_pivot][j] = L[index_pivot][j], L[k][j]

        for i in range(k+1, n):
            if abs(U[k][k]) < 1e-10:
                raise ValueError("Pivot nul")
            factor = U[i][k] / U[k][k]
            L[i][k] = factor
            for j in range(k, n):
                U[i][j] -= factor * U[k][j]

    return P, L, U

def resoudre_plu(P, L, U, b):
    n = len(P)
    Pb = [sum(P[i][j] * b[j] for j in range(n)) for i in range(n)]
    return resoudre_lu(L, U, Pb)