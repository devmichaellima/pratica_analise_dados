# Desafio 06 - Relatório Executivo de Serviços

## Contexto

A gestão da empresa já analisou clientes, faturamento por período e participação no faturamento. Agora o próximo passo é entender o desempenho dos serviços oferecidos.

Essa análise é importante para identificar quais serviços geram mais receita, quais possuem maior ticket médio e quais são mais frequentes na operação.

Em uma empresa real, esse tipo de relatório ajuda a tomar decisões sobre promoções, prioridade comercial, precificação e planejamento operacional.

---

## Objetivo

Desenvolver uma análise utilizando Python e pandas para criar um relatório executivo de serviços.

Você deverá consolidar os dados por serviço e gerar indicadores de faturamento, quantidade de ordens, ticket médio e participação percentual no faturamento total.

---

## Estrutura Esperada do Projeto

```txt
dia_06/
│
├── data/
│   └── servicos_faturamento.csv
│
├── src/
│   └── analise.py
│
├── output/
│   └── relatorio_servicos.csv
└── README.md
```

---

## Dados do CSV

Crie manualmente o arquivo `servicos_faturamento.csv` dentro da pasta `data/`.

Conteúdo:

```csv
id_os,cliente,servico,valor,status
1,João,Troca de Óleo,120,Finalizado
2,Maria,Alinhamento,80,Finalizado
3,João,Freio,350,Finalizado
4,Carlos,Troca de Óleo,120,Pendente
5,Maria,Freio,300,Finalizado
6,Ana,Revisão,500,Finalizado
7,João,Revisão,500,Finalizado
8,Carlos,Alinhamento,80,Finalizado
9,Ana,Freio,320,Pendente
10,Maria,Revisão,500,Finalizado
11,Pedro,Bateria,450,Finalizado
12,Ana,Troca de Óleo,120,Finalizado
13,João,Freio,380,Finalizado
14,Carlos,Bateria,420,Cancelado
15,Maria,Alinhamento,90,Finalizado
16,Ana,Revisão,550,Finalizado
```

---

## Problema

A empresa quer entender o desempenho dos serviços realizados.

A gestão precisa responder:

Qual foi o faturamento total considerando apenas ordens finalizadas?

Quanto cada serviço faturou?

Quantas ordens finalizadas cada serviço teve?

Qual foi o ticket médio de cada serviço?

Qual percentual do faturamento total cada serviço representa?

Qual serviço teve maior faturamento?

Qual serviço teve maior ticket médio?

---

## Regras

Utilize Python e pandas.

Considere apenas ordens com status `Finalizado`.

Agrupe os dados por serviço.

Calcule faturamento total por serviço.

Calcule quantidade de ordens por serviço.

Calcule ticket médio por serviço.

Calcule participação percentual de cada serviço no faturamento total.

Ordene o relatório final pelo faturamento total em ordem decrescente.

Exporte o resultado em um arquivo chamado `relatorio_servicos.csv`.

---

## Sua Missão

Criar um relatório final por serviço com as seguintes colunas:

```csv
servico,faturamento_total,qtd_ordens,ticket_medio,participacao_percentual
```

O relatório deve permitir que a gestão entenda quais serviços são mais relevantes financeiramente para a empresa.

---

## Exemplo de Saída Esperada

```csv
servico,faturamento_total,qtd_ordens,ticket_medio,participacao_percentual
Revisão,2050,4,512.50,39.42
Freio,1030,3,343.33,19.81
Bateria,450,1,450.00,8.65
Alinhamento,250,3,83.33,4.81
Troca de Óleo,240,2,120.00,4.62
```

Os valores acima servem como referência de estrutura. Valide os resultados com base nos dados do CSV.

---

## Entregáveis

Ao finalizar o desafio, entregue o arquivo `analise.py`, o arquivo `relatorio_servicos.csv` exportado na pasta `output` e o README do desafio na pasta do projeto.

---

## Tecnologias Utilizadas

Python e pandas.

---

## Competências Treinadas

Neste desafio serão treinadas as seguintes competências:

Leitura de arquivos CSV.

Filtragem de dados por status.

Agrupamento por categoria de negócio.

Agregação com soma, contagem e média.

Criação de colunas calculadas.

Cálculo de ticket médio.

Cálculo de participação percentual.

Ordenação de dados.

Exportação de relatório executivo.

Construção de visão analítica por serviço.

---

## O Que Era Esperado

Era esperado que o analista conseguisse criar uma visão consolidada por serviço, transformando dados operacionais em indicadores úteis para a gestão.

A solução deve demonstrar domínio dos fundamentos treinados no Bloco 1: leitura, filtro, agrupamento, agregação, cálculo percentual, ranking e exportação.

Este desafio encerra o primeiro bloco do treinamento e prepara a transição para análises com múltiplas tabelas.
