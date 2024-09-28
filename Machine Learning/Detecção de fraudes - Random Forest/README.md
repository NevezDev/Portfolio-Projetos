# Previsão de Fraude em Transações de Cartão de Crédito com Random Forest

Olá! Bem-vindo ao meu projeto de Previsão de Fraude em Transações de Cartão de Crédito! 🚀 Como um cientista de dados júnior, estou animado para compartilhar como utilizei um modelo de Random Forest para detectar transações fraudulentas, ajudando a proteger usuários e instituições financeiras.

## Conjunto de Dados

O conjunto de dados utilizado contém informações sobre transações de cartão de crédito, com um foco especial na identificação de transações fraudulentas. As características incluídas permitem uma análise abrangente do comportamento dos usuários.

## Etapas do Projeto

Aqui está um resumo das etapas que segui neste projeto:

1. **Exploração de Dados**: Realizei uma análise descritiva e visualizei dados para entender melhor a estrutura do conjunto.
2. **Preparação de Dados**: 
   - Dividi os dados em features (variáveis independentes) e target (variável dependente).
   - Realizei a divisão do conjunto em treinamento e teste, garantindo uma distribuição balanceada das classes.
3. **Construção do Modelo**: 
   - Utilizei o RandomForestClassifier com pesos balanceados para lidar com o desbalanceamento das classes.
4. **Treinamento do Modelo**: 
   - Treinei o modelo com os dados de treinamento.
5. **Avaliação do Modelo**: 
   - Avaliei o desempenho utilizando métricas como acurácia, precisão, recall e matriz de confusão.
6. **Visualização de Resultados**: 
   - Criei gráficos para visualizar a curva de precisão-recall e a matriz de confusão, facilitando a análise do desempenho do modelo.

## Tecnologias Utilizadas

Para desenvolver este projeto, utilizei várias tecnologias úteis:

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

## Como Executar o Projeto

Se você quiser experimentar, siga estes passos simples:

1. Faça o download do conjunto de dados e do notebook.
2. Abra o notebook no Google Colab ou em um ambiente Jupyter Notebook.
3. Execute as células do notebook em sequência e veja o modelo em ação!

## Análise dos Gráficos

### 1. Curva de Precisão-Recall

![Curva de Precisão-Recall](Imagens/curva_precisao_recall.png)

*Este gráfico mostra a relação entre precisão e recall, ajudando a entender o desempenho do modelo em diferentes limiares de classificação.*

### 2. Matriz de Confusão

![Matriz de Confusão](Imagens/confmatrix.png)

*Aqui temos a matriz de confusão, que ilustra a performance do modelo, mostrando quantas previsões foram corretas e incorretas em cada classe.*

## Observações

- O modelo é um ponto de partida! Ele pode ser aprimorado com ajustes em hiperparâmetros e técnicas de pré-processamento.
- É importante analisar criticamente os resultados e considerar o contexto ao interpretar as previsões.

## Contribuições

Estou aberto a contribuições! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir issues ou pull requests.

Este projeto é um exemplo de como algoritmos de aprendizado de máquina podem ser aplicados na detecção de fraudes. As técnicas e ferramentas aqui apresentadas podem ser úteis para outros problemas de classificação binária. Vamos explorar juntos o universo da ciência de dados! 🌟
