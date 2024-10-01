"""
Diky, pekne. Ukol mate splneny. Doplnil jsem par poznamek.
Zaroven bych se vyhybal specialnim znakum jako rovnitko v nazvu souboru. Omezil bych se pouze na podtrzitka, pripadne pomlcky. 
"""
import numpy as np

"""
Pokud pracujete s nejakym promennym rozmerem, je obecne dobre ho ukladat do samostatne promenne, aby jej  bylo pak mozne snadno zmanit v celem programu.
Napr.
n = 10 ci dim = 10
"""
matrix= np.zeros((10, 10))

upper_diagonal =2
lower_diagonal=-1

np.fill_diagonal(matrix,2) #<-- nevyuzita promenna upper_diagonal (ktera by mela byt spise main_diagonal)
np.fill_diagonal(matrix[1:,0:-1],lower_diagonal)
np.fill_diagonal(matrix[0:,1:],-1) #<-- nezavedena/nevyuzita promenna upper diagonal
"""
Prikladam jeste alternativni zpusob. np.fill_diagonal je nicmene take dobra moznost.
Existuje vsak prikaz np.diag( diag_vect, offset ), kde offset nastavuje posun od hlavni diagonaly.
Ekvivateltni reseni by mohlo tedy napriklad byt

matrixDifferentApproach = np.diag( 2  * np.ones( 10 ) ) + np.diag( ( -1 ) * np.ones( 10 -1 ), -1 ) + np.diag( ( -1 ) * np.ones( 10 - 1), + 1 )
print(matrixDifferentApproach)

vizte dokumentaci
https://numpy.org/doc/stable/reference/generated/numpy.diag.html
https://numpy.org/doc/2.0/reference/generated/numpy.fill_diagonal.html
"""

det = np.linalg.det(matrix)
vlastni_cisla, vlastni_vektory = np.linalg.eig(matrix)
hodnost = np.linalg.matrix_rank(matrix)

#help (np.linalg.eig);
#help (np.linalg.matrix_rank);

"""
.reshape zde neni nutne, nicmene je dobre, ze hledite na dimenze
Zaroven si povsimnete rozdilu mezi

print(np.arange(1, 11).shape)
print(np.arange(1, 11).reshape(10, 1).shape)
"""
vektor_b = np.arange(1, 11).reshape(10, 1) 
x = np.linalg.solve(matrix,vektor_b)

"""
Do print funkce lze nacpat spoustu veci. Velmi elegantni je pouzit formatovany string

print( f'10x10 Matice\n {matrix}' )
Vypisujete-li desetinne cislo, lze timto zpusobem snadno ovlivnit pocet cifer, ktery se vypise
print( f'Determinant: {np.linalg.det(matrix)/6:.2f}' )
vs
print( f'Determinant: {np.linalg.det(matrix)/6}' )
"""
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
