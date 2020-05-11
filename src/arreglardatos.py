from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.pipeline import make_pipeline
import pandas as pd

# Estandarizo y normalizo,
def stand_Normalize(df):
    pipeline = [    
        StandardScaler(),
        Normalizer(),]
    transformer = make_pipeline(*pipeline)
    X_new = transformer.fit_transform(df)
    return pd.DataFrame(X_new, columns=df.columns)

# Genera columnas categoricas si son tipo "object".
def category(df):
    for columna in df:
        
        if(df[columna].dtype == 'object'):
            df[columna] = df[columna].astype('category')
            df[columna] = df[columna].cat.codes
    return df