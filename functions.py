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
def matrice_identite(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
def multiplier_matrices(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return C
def echanger_lignes(A, i, j):
    A[i], A[j] = A[j], A[i]