
"""
**Importando as bibliotecas necessárias como pandas, numpy, matplotlib e scikit-learn.**
"""

# Importa as bibliotecas necessárias
def criacao_treinamento_modelo():
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

    """**Carregando o conjunto de dados e vendo as váriaveis.**"""

    data = pd.read_csv('CarPrice_Assignment.csv')
    data.head()

    """**Explorar e pré-processando os dados verificando se tem dados nulos ou duplicados**"""

    data.isnull().sum() # Verifica se há valores nulos em cada coluna

    data.duplicated() #Verifica se há linhas duplicadas

    """**Visualizando a correlação entre os dados para ter uma compreensão sobre as caracteristicas mais importantes.**"""

    dummie = list(data.select_dtypes('object').columns) #Cria uma lista "dummie" com as colunas que são do tipo "object"

    for col in dummie: # Itera sobre cada coluna na lista "dummie"
        onehot = pd.get_dummies(data[col], prefix= col, dtype= int)# Cria variáveis dummy para a coluna "col" e em "onehot"
        data = pd.concat( [data, onehot], axis = 1)# Concatena dataframe data com o dataframe "onehot" ao longo das colunas

    data = data.drop(dummie, axis =1) # Remove as colunas originais da lista "dummie" do DataFrame "data"

    # Calcula a matriz de correlação
    correlation_matrix = data.corr()['price']
    correlation_matrix.sort_values(ascending=False)
    print(correlation_matrix.to_string())

    """**Carregando novamente o conjunto.**"""

    data = pd.read_csv('CarPrice_Assignment.csv')
    data.head()

    """**Visualizando as caracteristicas com o auxilio de histograma.**"""

    # Cria um histograma para cada coluna numérica do DataFrame "data"
    data.hist(figsize = (14,10), bins = 20)

    """**Excluindo as caracteristicas com pouco valor preditório.**"""

    # Remove as colunas pouco uteis para previsão do DataFrame "data"
    data = data.drop(['drivewheel','car_ID','symboling','CarName','enginelocation','fuelsystem'], axis = 1)
    data.info()

    """**Alocando as caracteristicas preditoras em X.**"""

    X = data.iloc[:, :-1]  # Cria um DataFrame "X" com todas as colunas do DataFrame "data", exceto a última
    X

    """**Alocando a caracteristica a ser prevista em y.**"""

    y = data.iloc[:, -1] # Cria um DataFrame "y" com a última coluna do DataFrame "data"
    y

    """**Aplicando o one-hot encoding nas colunas de tipo não-numéricas.**"""

    dummie = list(data.select_dtypes('object').columns)

    for col in dummie:
        onehot = pd.get_dummies(X[col], prefix= col, dtype= int)
        X = pd.concat( [X, onehot], axis = 1)

    X = X.drop(dummie, axis =1)

    """**Visualizando as classes preditoras após o one-hot.**"""

    X

    X.info()  # Exibe informações sobre o DataFrame "X", como tipo de dados de cada coluna e número de valores não nulos

    """**Dividindo as váriaveis de treino e teste utilizando o train_test_split.**"""

    # Divide os dados em conjuntos de treinamento e teste, com 80% dos dados para treinamento e 20% para teste com uma seed '42'
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state= 42)
    (x_train.shape, x_test.shape, y_train.shape, y_test.shape) # Exibe o formato dos conjuntos de treinamento e teste

    """**Iniciando o modelo de regressão linear e o ajustando aos dados de treinamento.**"""

    modelo = LinearRegression() # Cria um modelo de regressão linear
    modelo.fit(x_train, y_train) # Treina o modelo de regressão linear com os dados de treinamento

    joblib.dump(modelo, 'modelotreinado.pk')
    print("Modelo Criado e Salvo com Sucesso")

def main():
    criacao_treinamento_modelo()    


if __name__ == "__main__":
    main()    

