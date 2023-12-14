def cofactor_matrix(matrix):
    cofactors = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            minor = [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]
            sign = (-1) ** (i+j)
            cofactor = sign * determinant(minor)
            row.append(cofactor)
        cofactors.append(row)
    return cofactors

def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        sign = (-1) ** c
        submatrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += sign * matrix[0][c] * determinant(submatrix)
        print(c)
    return det

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Determinan matriks adalah nol, matriks tidak memiliki invers.")
    
    cofactors = cofactor_matrix(matrix)
    adjoint = transpose(cofactors)
    
    inverse = [[adjoint[i][j] / det for j in range(len(adjoint[0]))] for i in range(len(adjoint))]
    
    return inverse

# Contoh matriks 3x3
matrix_3x3 = [
    [1,2,3],
    [2,5,3],
    [1,0,8]
]

# Menghitung matriks invers
inverse_matrix_3x3 = inverse_matrix(matrix_3x3)

# Menampilkan hasil
print("Matriks Awal:")
for row in matrix_3x3:
    print(row)

print("\nMatriks Invers:")
for row in inverse_matrix_3x3:
    print(row)
    

