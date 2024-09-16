def gerar_previsoes_modelo():
    import numpy as np
    import pandas as pd
    import seaborn as sb
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, mean_absolute_error
    from sklearn.preprocessing import StandardScaler
    import matplotlib.pyplot as plt
    from sklearn.metrics import r2_score
    import joblib

    clf = joblib.load('modelotreinado.pk')
    dados = pd.read_csv('novo_dataframe.csv')

    dados.head()


    x = dados.drop('price', axis=1)
    

   

    previsoes = clf.predict(x)
    dados = dados.drop(dados.columns[14:39], axis=1)
    dados['PREVISOES'] = previsoes
    
         

    dados.to_excel('previsoes_preçoscarro.xlsx')
    print("Previsoes Geradas com Sucesso!")    

    

def main():
    gerar_previsoes_modelo()    


if __name__ == "__main__":
    main()    
