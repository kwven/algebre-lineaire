from functions import *

def verifier_conditions_lu(A):
    n = len(A)
    for k in range(n-1):
        if abs(det([[A[i][j] for j in range(k+1)] for i in range(k+1)])) < 1e-10:
            return False
    return True


def lu_decomposition(A):
    if not verifier_conditions_lu(A):
        return "erore"

    n = len(A)
    L = matrice_identite(n)
    U = [[0.0] * n for _ in range(n)]

    for j in range(n):
        for i in range(j+1):
            somme = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - somme

        for i in range(j+1, n):
            somme = sum(L[i][k] * U[k][j] for k in range(j))
            if abs(U[j][j]) < 1e-10:
                raise ValueError("Division par zéro")
            L[i][j] = (A[i][j] - somme) / U[j][j]

    return L, U

def resoudre_lu(L, U, b):
    n = len(L)
    y = [0] * n
    x = [0] * n

    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    for i in range(n-1, -1, -1):
        if abs(U[i][i]) < 1e-10:
            raise ValueError("Système singulier")
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]

    return x