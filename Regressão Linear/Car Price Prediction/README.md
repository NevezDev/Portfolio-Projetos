# Previsão dos Preços de Carros Usando Regressão Linear

Olá! Bem-vindo ao meu projeto de Previsão dos Preços de Carros! 🚗 Como um cientista de dados júnior, estou animado para compartilhar como utilizei regressão linear para prever os preços de carros com base em várias características. O objetivo aqui é desenvolver um modelo que ajude a entender quais fatores influenciam o preço dos veículos.

## Conjunto de Dados

O conjunto de dados utilizado contém informações sobre diferentes carros, incluindo características como tipo de motor, localização do motor, sistema de combustível e outros fatores relevantes. Essas informações são essenciais para treinar um modelo de previsão eficaz.

## Etapas do Projeto

Aqui está um resumo das etapas que segui neste projeto:

1. **Exploração de Dados**: Carreguei e analisei o conjunto de dados, verificando a presença de valores nulos ou duplicados.
2. **Pré-processamento de Dados**:
   - Realizei o one-hot encoding para variáveis categóricas.
   - Visualizei a correlação entre as características e o preço, identificando as mais importantes.
   - Removi colunas com pouco valor preditório.
3. **Divisão dos Dados**: Separei os dados em conjuntos de treinamento e teste, garantindo uma divisão equilibrada.
4. **Construção do Modelo**: Utilizei o `LinearRegression` da biblioteca Scikit-learn para criar e treinar o modelo.
5. **Avaliação do Modelo**: Avaliei o desempenho do modelo com métricas como MAE, MSE e R².
6. **Visualização de Resultados**: Criei gráficos para comparar os preços reais com os previstos, ajudando a entender a eficácia do modelo.

## Tecnologias Utilizadas

Para desenvolver este projeto, utilizei várias tecnologias úteis:

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## Como Executar o Projeto

Se você quiser experimentar, siga estes passos simples:

1. Faça o download do conjunto de dados e do notebook.
2. Abra o notebook no Google Colab ou em um ambiente Jupyter Notebook.
3. Execute as células do notebook em sequência e veja o modelo em ação!

## Análise dos Gráficos

### 1. Gráfico de Dispersão: Preços Reais vs. Preços Previstas

![Atual vs Previsto](Imagens/atual_vs_previsto.png)

*Este gráfico ilustra a relação entre os preços reais e os preços previstos pelo modelo, permitindo uma visualização clara da precisão das previsões.*

## Observações

- O modelo é um ponto de partida! Ele pode ser aprimorado com ajustes em hiperparâmetros e a inclusão de mais características.
- Sempre analise criticamente os resultados e leve em consideração o contexto ao interpretar as previsões.

## Contribuições

Estou aberto a contribuições! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir issues ou pull requests.

Este projeto é um exemplo de como a regressão linear pode ser aplicada na previsão de preços de carros. As técnicas e ferramentas aqui apresentadas podem ser úteis para outros problemas de regressão. Vamos explorar juntos o universo da ciência de dados! 🌟
