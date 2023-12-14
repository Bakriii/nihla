import numpy as aljabar

b = aljabar.array([[1,2,3,9],
                   [2,5,3,8],
                   [1,0,8,5],
                   [1,0,8,5]])

inv = aljabar.linalg.inv(b)

print("matriks awal")
print(b)

print("\nmatriks invers:")
print(inv)