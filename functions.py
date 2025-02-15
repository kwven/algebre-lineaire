#

#
def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    det = 0
    for j in range(n):
        sous_matrice = [[A[i][k] for k in range(n) if k != j] for i in range(1, n)]
        det += A[0][j] * ((-1) ** j) * det(sous_matrice)
    return det

#
def matrice_identite(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

#
def multiplier_matrices(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return C

#
def echanger_lignes(A, i, j):
    A[i], A[j] = A[j], A[i]

def trouver_pivot_max(A, k, n):
    pivot_max = abs(A[k][k])
    index_max = k
    for i in range(k+1, n):
        if abs(A[i][k]) > pivot_max:
            pivot_max = abs(A[i][k])
            index_max = i
    return index_max

#
def valeur_abs(a):
    if a<0:
        return -1*a
    else:
        return a
    
#
def est_diagonale_dominant(A):
    n=len(A)
    for i in range(n):
        k=0
        for j in range(n):
            if i!=j:
                k+=valeur_abs(A[i][j])
        if valeur_abs(A[i][i])<k:
            return False
    return True

#
def copier(A):
    return A

#

def symetrique(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                return False
    return True

#
def norme(A):
    a=0
    for i in A:
        a+=i[0]**2
    return a**(1/2)
