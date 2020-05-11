from time import time
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

# Genero una función para probar modelos
def probarModelo(X,y,modelos):     
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)        
    
    for name,m  in modelos.items():        
        print(f"Entrenando {name}...")
        m = m.fit(X_train, y_train)
        print(m)
        print("Entrenamiento completo")      
        y_pred = m.predict(X_test)
        print(f"Evaluando modelo {name}")
        print(r2_score(y_test, y_pred))
        return y_pred
   

#Función para optimizar modelos


def optimizar_modelos(tuning,X ,Y):
    X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2)  
    tuning_gradientGradient = GridSearchCV(estimator=tuning,param_grid=params,scoring="r2",verbose = 10, n_jobs=7, cv=5)

    t0 =time()
    observando = tuning.fit(X_train,y_train)
    y_pred = observando.predict(X_test)
    print(r2_score(y_test, y_pred))

    print("Hecho en %0.3fs" % (time() - t0))
    print("Mejor  estimator encontado en la busqueda es:")
    print(observando.best_estimator_)
    return y_pred