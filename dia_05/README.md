# Desafio 05 - Participação de Clientes no Faturamento

## Contexto

Depois de identificar os clientes com maior faturamento, a gestão quer entender quanto cada cliente representa no faturamento total da empresa.

Essa análise é importante para identificar concentração de receita, dependência de poucos clientes e oportunidades comerciais.

Em empresas reais, não basta saber quem mais faturou. Também é necessário entender o peso de cada cliente no resultado geral.

---

## Objetivo

Desenvolver uma análise utilizando Python e pandas para calcular a participação percentual de cada cliente no faturamento total.

Você deverá criar uma tabela consolidada por cliente contendo faturamento, quantidade de ordens e percentual de participação no faturamento.

---

## Estrutura Esperada do Projeto

```txt
dia_05/
│
├── data/
│   └── clientes_faturamento.csv
│
├── src/
│   └── analise.py
│
├── output/
│   └── relatorio_clientes.csv
└── README.md
```

---

## Dados do CSV

Utilize o mesmo arquivo do Desafio 04.

Caso prefira criar novamente, use o conteúdo abaixo:

```csv
id_os,cliente,valor
1,João,120
2,Maria,80
3,João,350
4,Carlos,120
5,Maria,300
6,Ana,500
7,João,500
8,Carlos,80
9,Ana,320
10,Maria,500
11,Pedro,450
12,Ana,120
13,João,200
14,Maria,250
15,Pedro,300
```

---

## Problema

A empresa quer responder às seguintes perguntas:

Qual foi o faturamento total?

Quanto cada cliente faturou?

Quantas ordens cada cliente realizou?

Qual percentual do faturamento total cada cliente representa?

Qual cliente tem maior participação no faturamento?

---

## Regras

Utilize Python e pandas.

Agrupe os dados por cliente.

Calcule o faturamento total de cada cliente.

Calcule a quantidade de ordens de cada cliente.

Calcule a participação percentual de cada cliente no faturamento total.

Ordene o resultado do maior para o menor faturamento.

Exporte o resultado em um arquivo chamado `relatorio_clientes.csv`.

---

## Sua Missão

Criar um relatório final por cliente com as seguintes colunas:

```csv
cliente,faturamento_total,qtd_ordens,participacao_percentual
```

A coluna `participacao_percentual` deve mostrar quanto cada cliente representa no faturamento total da empresa.

---

## Exemplo de Saída Esperada

```csv
cliente,faturamento_total,qtd_ordens,participacao_percentual
João,1170,4,27.92
Maria,1130,4,26.97
Ana,940,3,22.43
Pedro,750,2,17.90
Carlos,200,2,4.77
```

---

## Tecnologias Utilizadas

Python e pandas.

---

## Competências Treinadas

Neste desafio serão treinadas as seguintes competências:

Agrupamento de dados por cliente.

Cálculo de faturamento consolidado.

Contagem de registros por grupo.

Criação de colunas calculadas.

Cálculo de participação percentual.

Ordenação de dados.

Exportação de relatório analítico.

Análise de concentração de receita.

Pensamento analítico voltado a negócio.

---

## O Que Era Esperado

Era esperado que o analista conseguisse transformar dados de faturamento em uma visão consolidada por cliente.

A solução deve demonstrar capacidade de calcular participação percentual, interpretar concentração de receita e gerar uma tabela útil para tomada de decisão comercial.

O foco deste desafio é avançar da análise de ranking para uma análise de representatividade financeira.
