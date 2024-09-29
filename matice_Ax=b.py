import numpy as np

matrix= np.zeros((10, 10))

upper_diagonal =2
lower_diagonal=-1

np.fill_diagonal(matrix,2)
np.fill_diagonal(matrix[1:,0:-1],lower_diagonal)
np.fill_diagonal(matrix[0:,1:],-1)

det = np.linalg.det(matrix)
vlastni_cisla, vlastni_vektory = np.linalg.eig(matrix)
hodnost = np.linalg.matrix_rank(matrix)

#help (np.linalg.eig);
#help (np.linalg.matrix_rank);

vektor_b = np.arange(1, 11).reshape(10, 1)
x = np.linalg.solve(matrix,vektor_b)

print("matice A:")
print(matrix)
print("Determinant matice je:", det)
print("Vlastní čísla matice jsou:", vlastni_cisla)
print("Vlastní vektory matice jsou:\n", vlastni_vektory)
print("Hodnost matice je:", hodnost)
print("\nVektor b:")
print(vektor_b)
print("\nŘešení soustavy x:")
print(x)
