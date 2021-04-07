# Store Sales Prediction

**Disclaimer:** O Contexto a seguir, é completamente fictício, a empresa, o contexto, as perguntas de negócio foram criadas apenas para o desenvolvimento do projeto, e se baseiam em um desafio do Kaggle. 


<p align="center">
  <img width="1000" height="400" src="https://howesoundpharmacy.ca/wp-content/uploads/health-medical-products-howe-sound-pharmacy-gibsons-bc.jpg" />
</p>


## Contexto de negócio

A empresa Rossmann opera mais de 3.000 drogarias em 7 países europeus. Atualmente, os gerentes de loja da Rossmann têm a tarefa de prever suas vendas diárias com até seis semanas de antecedência. As vendas da loja são influenciadas por muitos fatores, incluindo promoções, competição, feriados escolares e estaduais, sazonalidade e localidade. Com milhares de gerentes prevendo vendas com base em suas circunstâncias únicas, a precisão dos resultados pode ser bastante variada. A necessidade de fazer uma previsão de vendas vem de um pedido do CFO  que deseja fazer uma reforma nas lojas, porém não sabe o quanto de dinheiro pode ser destinado para esta reforma. Sua intenção é saber o faturamento das lojas para as próximas 6 semanas para assim poder adiantar o orçamento e realizar as reformas.


## Dados

O conjunto de dados que representam o contexto está disponível na plataforma do Kaggle. Esse é o link: https://www.kaggle.com/c/rossmann-store-sales/data. O dataset possui os seguintes atributos:

**Id** - um Id que representa (Store, Date) dentro do conjunto de teste

**Store** - Id único para cada loja

**Sales** - o volume de negócios em um determinado dia.

**Customers** - o número de clientes em um determinado dia

**Open** - um indicador para saber se a loja estava aberta: 0 = fechada, 1 = aberta

**StateHoliday** - indica um feriado estadual. Normalmente todas as lojas, com poucas exceções, fecham nos feriados estaduais. Observe que todas as escolas fecham nos feriados e finais de semana. a = feriado, b = feriado da Páscoa, c = Natal, 0 = Nenhum

**SchoolHoliday** - indica se (Loja, Data) foi afetado pelo fechamento de escolas públicas

**StoreType** - diferença entre 4 modelos de loja diferentes: a, b, c, d

**Assortment** - descreve um nível de sortimento: a = básico, b = extra, c = estendido

**CompetitionDistance** - distância em metros até a loja concorrente mais próxima

**CompetitionOpenSince[Month/Year]** - o ano e mês aproximados em que o concorrente mais próximo foi aberto

**Promo** - indica se uma loja está fazendo uma promoção naquele dia

**Promo2** - Promo2 é uma promoção contínua e consecutiva para algumas lojas: 0 = a loja não está participando, 1 = a loja está participando

**Promo2Since[Year/Week]** - descreve o ano e a semana em que a loja começou a participar da Promo2

**PromoInterval** - descreve os intervalos consecutivos de início da promoção 2, nomeando os meses em que a promoção é iniciada novamente. Por exemplo. "Fev, maio, agosto, novembro" significa que cada rodada começa em fevereiro, maio, agosto, novembro de qualquer ano para aquela loja

## Planejamento da solução

1. Entendimento do negócio e problemas e serem resolvidos

2. Coleta de dados

3. Limpeza dos dados

4. Exploração dos dados em busca de um melhor entendimento do negócio através da geração de insights e das variáveis mais importantes na modelagem do modelo de Machine Learning 

5. Preparação dos dados para os algoritmos de machine learning

6. Aplicação dos algoritmos de machine learning

7. Avaliação do algoritmo

8. Tradução do erro em métricas de negócio

9. Deploy do modelo em produção

## Melhores Insights

## Machine Learning Models

## Resultados 
