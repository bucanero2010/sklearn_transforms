from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
class NewColumns(BaseEstimator, TransformerMixin):
    def __init__(self,columns=None):
        self.columns = columns
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        data['FLAG_B_DS']=(data.AVG_SCORE_DATASCIENCE*data.NUM_COURSES_BEGINNER_DATASCIENCE)
        data['FLAG_B_FE']=(data.AVG_SCORE_FRONTEND*data.NUM_COURSES_BEGINNER_FRONTEND)
        data['FLAG_B_BE']=(data.AVG_SCORE_BACKEND*data.NUM_COURSES_BEGINNER_BACKEND)
        data['FLAG_A_DS']=(data.AVG_SCORE_DATASCIENCE*data.NUM_COURSES_ADVANCED_DATASCIENCE)
        data['FLAG_A_FE']=(data.AVG_SCORE_FRONTEND*data.NUM_COURSES_ADVANCED_FRONTEND)
        data['FLAG_A_BE']=(data.AVG_SCORE_BACKEND*data.NUM_COURSES_ADVANCED_BACKEND)
        data['FLAG_A_DS_COMP']=(data.AVG_SCORE_DATASCIENCE*(data.NUM_COURSES_ADVANCED_DATASCIENCE
                                                                 +data.NUM_COURSES_BEGINNER_DATASCIENCE)*data.HOURS_DATASCIENCE)
        data['FLAG_A_FE_COMP']=(data.AVG_SCORE_FRONTEND*(data.NUM_COURSES_ADVANCED_FRONTEND
                                                              +data.NUM_COURSES_BEGINNER_FRONTEND)*data.HOURS_FRONTEND)
        data['FLAG_A_BE_COMP']=(data.AVG_SCORE_BACKEND*(data.NUM_COURSES_ADVANCED_BACKEND
                                                             +data.NUM_COURSES_BEGINNER_BACKEND)*data.HOURS_BACKEND)
        suma_ds=(data.NUM_COURSES_BEGINNER_DATASCIENCE+data.NUM_COURSES_ADVANCED_DATASCIENCE)
        suma_be=(data.NUM_COURSES_BEGINNER_BACKEND+data.NUM_COURSES_ADVANCED_BACKEND)
        suma_fe=(data.NUM_COURSES_BEGINNER_FRONTEND+data.NUM_COURSES_ADVANCED_FRONTEND)
        data['HORAS P CURSO DS']=(data.HOURS_DATASCIENCE)/suma_ds
        data['HORAS P CURSO BE']=(data.HOURS_BACKEND)/suma_be
        data['HORAS P CURSO FE']=(data.HOURS_FRONTEND)/suma_fe
        data['HORAS P CURSO']=(data.HOURS_DATASCIENCE+data.HOURS_BACKEND+data.HOURS_FRONTEND)/(suma_ds+suma_be+suma_fe)
        data=data.replace([np.inf, -np.inf,np.nan],0)
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        return data
