# Limpeza e Tratamento de Dados para Regressão Logística

Olá! Bem-vindo ao meu projeto de Limpeza e Tratamento de Dados para Regressão Logística! 📊 Como um cientista de dados júnior, estou animado para compartilhar como preparei um conjunto de dados para prever o churn de clientes usando regressão logística. O objetivo aqui é transformar os dados brutos em um formato que possa ser utilizado para análise e modelagem.

## Conjunto de Dados

O conjunto de dados utilizado contém informações sobre clientes, como pontuação, estado, gênero, idade, patrimônio e saldo. Esses dados são essenciais para entender o perfil dos clientes e prever se eles deixarão a empresa.

## Etapas do Projeto

Aqui está um resumo das etapas que segui neste projeto:

1. **Carregamento e Exploração dos Dados**: Carreguei o conjunto de dados e examinei suas características e possíveis inconsistências.
2. **Pré-processamento**:
   - Renomeei colunas para facilitar a manipulação.
   - Realizei a limpeza de dados, tratando valores nulos, duplicados e outliers.
   - Apliquei o `LabelEncoder` para converter variáveis categóricas em valores numéricos.
3. **Balanceamento dos Dados**: Utilizei a técnica SMOTE para lidar com o desbalanceamento de classes.
4. **Divisão dos Dados**: Separei os dados em conjuntos de treinamento e teste.
5. **Construção do Modelo**: Treinei um modelo de regressão logística com os dados processados.
6. **Avaliação do Modelo**: Utilizei métricas de desempenho para avaliar a acurácia do modelo e visualizei os resultados.

## Tecnologias Utilizadas

Para desenvolver este projeto, utilizei várias tecnologias úteis:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn

## Como Executar o Projeto

Se você quiser experimentar, siga estes passos simples:

1. Faça o download do conjunto de dados e do notebook.
2. Abra o notebook no Google Colab ou em um ambiente Jupyter Notebook.
3. Execute as células do notebook em sequência e veja o modelo em ação!

## Análise dos Gráficos

### 1. Gráfico de Dispersão: Idade vs. Saldo

![Dispersão](Imagens/scatterplotlog.png)

*Este gráfico ilustra a relação entre a idade e o saldo dos clientes, ajudando a visualizar a distribuição do churn.*

Insights:
Pode revelar como o saldo e a idade interagem, indicando se clientes mais velhos com maior saldo têm menos chances de churn, ou vice-versa.
Uma concentração de pontos em certas áreas pode indicar perfis de clientes mais propensos ao churn.

### 2. Gráficos de Pizza: Distribuição de Churn por Faixa Etária e Saldo

![Distribuição de Churn](Imagens/grafpizzalogidade.png)
![Distribuição de Churn](Imagens/grafpizzalogsaldo.png)


*Esses gráficos mostram a distribuição de clientes que saíram ou não, segmentados por faixas etárias e saldo, oferecendo insights valiosos para estratégias de retenção.*

Insights:
Identifica qual faixa etária apresenta maior rotatividade, ajudando na personalização de estratégias de retenção.
Por exemplo, se a faixa <30% mostra uma alta taxa de churn, isso pode indicar a necessidade de intervenções específicas para essa demografia.

Insights:
Permite entender se o saldo dos clientes impacta suas decisões de sair ou permanecer.
Se clientes com saldo >100.000 apresentam baixas taxas de churn, isso pode indicar que clientes mais ricos tendem a ser mais leais.

## Observações

- O modelo é um ponto de partida! Ajustes em hiperparâmetros e a inclusão de mais características podem melhorar a performance.
- É importante analisar criticamente os resultados e o contexto ao interpretar as previsões.

## Contribuições

Estou aberto a contribuições! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir issues ou pull requests.

Este projeto é um exemplo de como a limpeza e o tratamento de dados são essenciais na construção de modelos preditivos. As técnicas e ferramentas aqui apresentadas podem ser úteis para outros problemas de classificação. Vamos explorar juntos o universo da ciência de dados! 🌟
