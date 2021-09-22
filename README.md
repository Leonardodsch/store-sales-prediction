Link para o notebook através do nbviewer (Recomendado para uma melhor visualização): 

[![image](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)](https://nbviewer.jupyter.org/github/Leonardodsch/store-sales-prediction/blob/main/store_sales_prediction.ipynb)

# Store Sales Prediction

**Disclaimer:** O Contexto a seguir, é completamente fictício, a empresa, o contexto, as perguntas de negócio foram criadas apenas para o desenvolvimento do projeto, e se baseiam em um desafio do Kaggle. 


<p align="center">
  <img width="1000" height="400" src="https://miro.medium.com/max/1000/0*IpUXpwNleNMgpPFr.png"/>
</p>


## Contexto de negócio

A empresa Rossmann opera mais de 3.000 drogarias em 7 países europeus. Atualmente, os gerentes de loja da Rossmann têm a tarefa de prever suas vendas diárias com até seis semanas de antecedência. As vendas da loja são influenciadas por muitos fatores, incluindo promoções, competição, feriados escolares e estaduais, sazonalidade e localidade. 

Com milhares de gerentes prevendo vendas com base em suas circunstâncias únicas, a precisão dos resultados pode ser bastante variada. A necessidade de fazer uma previsão de vendas vem de um pedido do CFO  que deseja fazer uma reforma nas lojas, porém não sabe o quanto de dinheiro pode ser destinado para esta reforma. Sua intenção é saber o faturamento das lojas para as próximas 6 semanas para assim poder adiantar o orçamento e realizar as reformas.


## Dados

O conjunto de dados que representam o contexto está disponível na plataforma do Kaggle. Esse é o link: https://www.kaggle.com/c/rossmann-store-sales/data. O dataset possui os seguintes atributos:

- **Id** - um Id que representa (Store, Date) dentro do conjunto de teste

- **Store** - Id único para cada loja

- **Sales** - o volume de negócios em um determinado dia.

- **Customers** - o número de clientes em um determinado dia

- **Open** - um indicador para saber se a loja estava aberta: 0 = fechada, 1 = aberta

- **StateHoliday** - indica um feriado estadual. Normalmente todas as lojas, com poucas exceções, fecham nos feriados estaduais. Observe que todas as escolas fecham nos feriados e finais de semana. a = feriado, b = feriado da Páscoa, c = Natal, 0 = Nenhum

- **SchoolHoliday** - indica se (Loja, Data) foi afetado pelo fechamento de escolas públicas

- **StoreType** - diferença entre 4 modelos de loja diferentes: a, b, c, d

- **Assortment** - descreve um nível de sortimento: a = básico, b = extra, c = estendido

- **CompetitionDistance** - distância em metros até a loja concorrente mais próxima

- **CompetitionOpenSince[Month/Year]** - o ano e mês aproximados em que o concorrente mais próximo foi aberto

- **Promo** - indica se uma loja está fazendo uma promoção naquele dia

- **Promo2** - Promo2 é uma promoção contínua e consecutiva para algumas lojas: 0 = a loja não está participando, 1 = a loja está participando

- **Promo2Since[Year/Week]** - descreve o ano e a semana em que a loja começou a participar da Promo2

- **PromoInterval** - descreve os intervalos consecutivos de início da promoção 2, nomeando os meses em que a promoção é iniciada novamente. Por exemplo. "Fev, maio, agosto, novembro" significa que cada rodada começa em fevereiro, maio, agosto, novembro de qualquer ano para aquela loja

## Planejamento da solução

1. Entendimento do negócio e problemas e serem resolvidos - Buscar entender os reais motivos da necessidade da previsão de vendas e como o probelma pode ser resolvido através de machine learning, quais aspectos serão considerados na hora da predição e quão melhor a solução proposta pode ser considerando os modelos de predição utilizados atualmente na empresa.    

2. Coleta de dados - Acesso a plataforma do Kaggle para download dos arquivos que serão usados.

3. Limpeza dos dados - Os dados são analisados usando diferentes técnicas para verificar a existência de dados faltantes, outliers (valor discrepantes) , ou qualquer tipo de inconsistências para que assim possam ser tratados devidamente e não impactar nas análises futuras. 

4. Exploração dos dados em busca de um melhor entendimento do negócio através da geração de insights e das variáveis mais importantes na modelagem do modelo de Machine Learning. Diversas hipóteses foram levantadas e validadas para obtenção de um conhecimento de negócio mais profundo, verificando também a correlação entre os atributos para que se possa ter uma ideia da importância de cada um para o modelo de machine learning. 

5. Preparação dos dados para os algoritmos de machine learning - Os dados foram transformados, balanceados e regularizados para que atendam as premissas de funcionamento dos algoritmos de machine learning, nesta etapa é importante deixar os dados preparados para que os algoritmos possam ter o melhor desempenho possível, e possíveis inconsistencias no dataset não interfiram no resultado final. 

6. Aplicação dos algoritmos de machine learning - Nesta etapa foram escolhidos os algoritmos de machine learning que seriam usados e então os mesmos foram treinados com os dados já preparados e prontos, cada algoritmo foi testado usando seus devidos parâmetros e posteriormente estratégias de cross validation foram usadas para verificar o real resultado do medelo, bem como tecnicas de hyperparameter fine tunning para encontrar os melhores parâmetros para o modelo escolhido. 

7. Avaliação do algoritmo - O algoritmo é avaliado com base em algumas métricas e nesse ponto verifica-se ou não a necessidade de realizar mais um ciclo para melhorar o desempenho final.

8. Tradução do erro em métricas de negócio - Com o melhor modelo escolhido, treinado e otimizado a taxa de erro encontrada é trasnformada em mátricas de negócio para que se saiba concretamente quanto de retorno financeiro aquela solução trouxe para a empresa. 

9. Deploy do modelo em produção - O modelo foi colocado em produção no ambiente cloud Heroku para que as predições possam ser utilizadas através de requisições a uma API. 

## Melhores Insights

**1. Lojas com maior sortimento vendem menos**

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129405567-7b3251c0-2dbd-4f2e-8773-8964c7de099b.png"/>
</p>


**2. Lojas com promoções ativas por mais tempo vendem menos, depois de um certo periodo de promoção**

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129405959-4fbc54c7-e809-4509-af89-77f9ee1428fd.png"/>
</p>


**3. Lojas vendem mais depois do dia 10 de cada mês**

<p align="center">
  <img width="650" height="500" src="https://user-images.githubusercontent.com/76128123/129406089-c9e451f4-4ebc-4142-9b5e-927aa626327e.png"/>
</p>


**4. Lojas com competidores mais proximos vendem mais**

<p align="center">
  <img width="650" height="500" src="https://user-images.githubusercontent.com/76128123/129406244-1aeeb0d4-4543-4f87-94a6-920d95360e2d.png"/>
</p>


## Machine Learning Models

Os algoritmos utilizados para fazer a predição foram: 
- Modelo de média para que fosse possível ter um modelo base de comparação, 
- Linear Regression;
- Linear Regression Regularized (Lasso);
- Random Forest Regressor;
- XGBoost Regressor. 

Após todos os testes e avaliações de performance dos modelos optou-se por utilizar o modelo XGBoost Regressor, que obteve uma performance muito satisfatória e é um modelo mais leve e rápido em comparação ao Random Forest, e que é um fator que pode fazer diferença quando colocado em produção.

Os resultados abaixo mostram a performance do modelo após realizar o fine tuning dos parâmetros. As métrics utilizadas foram:

- MAE (Mean Absolute error) - Mostra o erro médio absoluto do modelo, tanto para mais quanto para menos.
- MAPE (Mean Absolute percentage error) - Erro médio absoluto em percentual.
- RMSE (Root mean squared error) - Erro médio absoluto quadrado, erro médio absoluto elevado ao quadrado. Não é a melhor métrica para uma análise de negócios, porém é muito util para avaliar a performance do modelo em si.  

![image](https://user-images.githubusercontent.com/76128123/129407241-d692f85a-174f-48df-a59b-1c8eb118e410.png)


## Resultados 

Através da interpretação do erro do modelo de machine learning foi possível avalia-lo de meneira a agregar valor para o cliete, com os resultados financeiros apresentados a seguir: 

![image](https://user-images.githubusercontent.com/76128123/114114780-f0b89d80-98b7-11eb-86bc-fd840b17d4e4.png)

A tabela acima mostra algums lojas escolhidas aleatoriamente e as suas respectivas previsões vendas, com o cálculo de melhor e pior cenário possivel, utilizando a métrica MAE, que indica a mádia do erro absoluto que o modelo possui.

![image](https://user-images.githubusercontent.com/76128123/114115150-adaafa00-98b8-11eb-8f4b-47af8ab5b08c.png)

Na segunda tabela é possivel observar o valor total somado de faturamento para todas as lojas, também considerando um melhor e um pior cenário. 

## Conclusão

Após todas as análises feitas através da exploração de dados e entendimento do negócio chegou-se em resultado satisfatório para o probelma em questão, o modelo escolhido aprentou uma boa performance com um erro relativamente baixo para a grandeza dos valores que foram preditos, fazendo com que o time de negócios possa tomar decisões muito mais assertivas e ter uma boa previsibilidade da receita futura usando essa solução. Por se tratar de um problema de previsão de vendas essa solução poderia ter sido trabalhada utilizando algoritmos de séries temporais porém optou-se pela utilização de uma regressão por possuiu modelos simples que já poderiam trazer bons resultados rapidamente, por não se tratar de um problema simples um modelo de árvore ecabou sendo escolhido para implementação. 

Em possiveis aprimoramentos do trabalho seria interessante testar também modelos de séries temporais e comparar o desempenho com os já conhecidos para um possível atualização dos modelos caso necessário. Mas de maneira geral os resultados obtidos ficaram de acordo com as expectativas do CFO e agora a empresa pode tomar melhores decisões baseada em seus próprios dados.        

