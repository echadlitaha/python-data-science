import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else :
        matrix = np.array(list).reshape(3, 3)

    moyenne_colonnes = np.mean(matrix, axis=0)
    moyenne_c = moyenne_colonnes.tolist()

    moyenne_lignes = np.mean(matrix, axis=1 )
    moyenne_l = moyenne_lignes.tolist()

    moyenne_globale = np.mean(matrix)
    moyenne_g = moyenne_globale.tolist()


    variance_colonnes = np.var(matrix, axis=0,ddof = 0)
    variance_c = variance_colonnes.tolist()

    variance_lignes = np.var(matrix, axis=1, ddof = 0 )
    variance_l = variance_lignes.tolist()

    variance_globale = np.var(matrix, ddof = 0)
    variance_g = variance_globale.tolist()


    ecart_type_colonnes = np.std(matrix, axis=0,ddof = 0)
    ecart_type_c = ecart_type_colonnes.tolist()

    ecart_type_lignes = np.std(matrix, axis=1,ddof = 0)
    ecart_type_l = ecart_type_lignes.tolist()

    ecart_type_globale = np.std(matrix,ddof = 0)
    ecart_type_g = ecart_type_globale.tolist()


    maximum_colonnes = np.max(matrix,axis = 0)
    maximum_c = maximum_colonnes.tolist()

    maximum_lignes = np.max(matrix,axis = 1)
    maximum_l = maximum_lignes.tolist()

    maximum_globale = np.max(matrix)
    maximum_g = maximum_globale.tolist()


    minimum_colonnes = np.min(matrix,axis = 0)
    minimum_c = minimum_colonnes.tolist()
    
    minimum_lignes = np.min(matrix,axis = 1)
    minimum_l = minimum_lignes.tolist()
    
    minimum_globale = np.min(matrix)
    minimum_g = minimum_globale.tolist()


    sommes_colonnes = np.sum(matrix,axis = 0)
    sommes_c = sommes_colonnes.tolist()
        
    sommes_lignes = np.sum(matrix,axis = 1)
    sommes_l = sommes_lignes.tolist()
        
    sommes_globale = np.sum(matrix)
    sommes_g = sommes_globale.tolist()

    result = {"mean": [
        moyenne_c,
        moyenne_l,
        moyenne_g
    ],"variance": [
    variance_c,
    variance_l,
    variance_g
],"standard deviation": [
    ecart_type_c,
    ecart_type_l,
    ecart_type_g
],"max": [
    maximum_c,
    maximum_l,
    maximum_g
],"min": [
    minimum_c,
    minimum_l,
    minimum_g
],"sum": [
    sommes_c,
    sommes_l,
    sommes_g
]}

    return result

list = [0,1,2,3,4,5,6,7,8]
print(calculate(list))