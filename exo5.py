import numpy as np 

matrice = np.array([[1,2,3],[4, 5,6],[7,8,9]])
matrice2 = np.array([[10],[31],[52]])

determinant = np.linalg.det(matrice)

print("Matrice")
print(matrice)
print("Determinant de la matrice", determinant)

matrice_inverse = np.linalg.inv(matrice)

print("La matrice inverse:\n",matrice_inverse)

resultat = np.dot(matrice_inverse, matrice2)

print("Le resultat de la multiplication est :\n", resultat)
