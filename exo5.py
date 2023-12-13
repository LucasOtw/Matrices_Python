import numpy as np 

matrice = np.array([[-2,5,-1],[1, -1,2],[3,0,4]])
matrice2 = np.array([[4],[12],[20]])

determinant = np.linalg.det(matrice)

print("Matrice")
print(matrice)
print("Determinant de la matrice", determinant)

matrice_inverse = np.linalg.inv(matrice)

print("La matrice inverse:\n",matrice_inverse)

resultat = np.dot(matrice_inverse, matrice2)

print("Le resultat de la multiplication est :\n", resultat)
