# Proyecto competición Kaggle del dataset Diamantes.

![Diamantes] "/home/sergio/bootcamp/ProyectDiamond/Output/Diamantes.jpg"

Este proyecto trata de desde un dataset de kaggle. Limpiar sus datos, estudiar lo que necesitan esos datos para poder sacar una buena predición de cuanto costaran esos diamantes según:
    
    price:  precio en Dolares (USD)
    carat:  peso del diamante
    cut:    calidad de corte (Fair, Good, Very Good, Premium, Ideal)
    color:  color del diamante  de  J (peor) a D (mejor)
    clarity: una medida de cuán claro es (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best)
    x:       longitud en  mm
    y:       anchura en mm
    z:       profundidad en mm
    profundidad:   total profundidad percentage = z / media(x, y) = 2 * z / (x + y) (43--79)
    table:   La mesa del diamante es la superficie plana en la parte superior de la piedra que se asemeja a una mesa real. Tamaño entre (43--95)



## Limpieza de datos
Empiezo cargando el dataset, comprobando el numero de filas y columnas. Compruebo nulos y si hay alguna columna categorica. Paso a númerica las columnas que no lo son.
Estandarizo y normalizo las columnas.
Compruebo la semejanza entre las columnas por si puedo desacerme de alguna de ellas.

##  Machine learning.
Con distintos metodos de sklearn saco los acurracy de los módelos para ver con cual me quedo para optimizarlo.
Optimizo varios modelos de regresión y los llevo a un csv para la competición en Kaggle