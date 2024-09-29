# Previsão de Temperatura com Análise Sazonal

Olá! Bem-vindo ao meu projeto de Previsão de Temperatura! 🌡️ Neste projeto, utilizei técnicas de análise de séries temporais para prever a temperatura média diária em Delhi, com base em dados históricos. O objetivo é entender padrões sazonais e facilitar previsões futuras.

## Conjunto de Dados

O conjunto de dados utilizado neste projeto é o "DailyDelhiClimateTrain.csv", que contém informações diárias sobre temperatura, umidade, velocidade do vento e pressão atmosférica. Esses dados são fundamentais para analisarmos as tendências climáticas.

## Etapas do Projeto

Aqui está um resumo das etapas que segui neste projeto:

1. **Importação de Bibliotecas**: Utilizei bibliotecas como pandas, numpy, seaborn, matplotlib e Prophet para manipulação de dados e modelagem.
2. **Carregamento e Visualização dos Dados**: Carreguei o conjunto de dados e visualizei suas primeiras linhas, além de verificar valores nulos e duplicados.
3. **Pré-processamento**:
   - Convertemos a coluna de data para o tipo datetime e a definimos como índice.
   - Extraí informações como ano, mês, dia e dia da semana.
4. **Visualização Inicial**: Criei gráficos de linha para temperatura média, umidade, velocidade do vento e pressão média, facilitando a análise visual.
5. **Decomposição Sazonal**: Realizei a decomposição sazonal da temperatura média, destacando componentes como tendência, sazonalidade e resíduos.
6. **Análise de Correlação**: Gere gráficos de correlação para entender a relação entre as variáveis meteorológicas.
7. **Criação do Modelo**: Utilizei o Prophet para modelar a série temporal e fiz previsões para os dados futuros.
8. **Avaliação do Modelo**: Calculei métricas como erro quadrático médio (MSE) e coeficiente de determinação (R²) para avaliar a precisão das previsões.
9. **Visualização das Previsões**: Criei gráficos comparativos entre os valores observados e previstos para entender a eficácia do modelo.

## Tecnologias Utilizadas

Para desenvolver este projeto, utilizei as seguintes tecnologias:

- Python
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Statsmodels
- Prophet

## Como Executar o Projeto

Se você deseja experimentar, siga estes passos:

1. Faça o download do conjunto de dados e do notebook.
2. Abra o notebook no Google Colab ou em um ambiente Jupyter Notebook.
3. Execute as células do notebook em sequência para ver o modelo em ação!

## Análise dos Gráficos

### 1. Gráficos de Linha para Variáveis Meteorológicas

![Gráfico de Temperatura Média](Imagens/graficodelinhatemporal.png)

*Este gráfico mostra a variação da temperatura média ao longo do tempo, evidenciando tendências e padrões sazonais.*

Temperatura Média

Insight: Este gráfico mostra como a temperatura média varia ao longo do tempo. Podemos observar padrões sazonais, como temperaturas mais altas em determinados meses.
Umidade Média

Insight: A umidade também exibe variações sazonais. A análise pode ajudar a entender a relação entre umidade e temperatura.
Velocidade do Vento Média

Insight: Este gráfico indica as oscilações na velocidade do vento, que podem ter implicações para a previsão do clima e atividades ao ar livre.
Pressão Média

Insight: A pressão atmosférica pode indicar mudanças climáticas. Um gráfico estável sugere um padrão previsível, enquanto flutuações abruptas podem indicar tempestades.

### 2. Gráficos de Decomposição Sazonal

![Decomposição Sazonal](Imagens/decomptemp.png)

*Aqui, visualizamos a decomposição da temperatura média em componentes de tendência, sazonalidade e resíduos, permitindo uma análise mais profunda dos padrões.*

Insight: A decomposição mostra a tendência, a sazonalidade e o resíduo da temperatura média. Isso permite identificar se as variações são sazonais ou se há uma tendência de longo prazo.

### 3. Gráficos de Correlação

![Mapa de Calor de Correlação](Imagens/corrtemp.png)

*Este mapa de calor ilustra a correlação entre as variáveis meteorológicas, ajudando a identificar relações importantes que podem influenciar as previsões.*

Insight: O mapa revela como as variáveis meteorológicas estão correlacionadas. Por exemplo, uma alta correlação entre temperatura e umidade sugere que, em meses quentes, a umidade tende a ser maior.

### 4. Gráficos de Previsão

![Previsão de Temperatura](Imagens/prevtemp.png)
![Previsão de Temperatura](Imagens/prev2temp.png)

*Este gráfico compara os valores reais e previstos da temperatura, permitindo uma avaliação visual do desempenho do modelo.*

Insight: Este gráfico compara os valores reais com as previsões do modelo. O ajuste do modelo pode ser avaliado pela proximidade das linhas. Um modelo bem ajustado deve apresentar previsões que seguem a tendência observada nos dados históricos.

Insight: Aqui, podemos avaliar como o modelo performa em dados não vistos. Uma boa previsão sugere que o modelo generaliza bem, enquanto desvios significativos indicam a necessidade de ajustes.

## Observações

- A modelagem de séries temporais é complexa e os resultados podem variar. Experimentar diferentes modelos e técnicas de pré-processamento pode levar a previsões melhores.
- Sempre considere o contexto dos dados ao interpretar os resultados.

## Contribuições

Estou aberto a contribuições! Se você tiver sugestões ou melhorias, fique à vontade para abrir issues ou pull requests.

Este projeto demonstra como a análise de dados e técnicas de modelagem podem ser aplicadas para entender e prever padrões climáticos. Vamos explorar juntos o fascinante mundo da ciência de dados! 🌟

--- 

Se precisar de ajustes ou mais informações, é só avisar!
