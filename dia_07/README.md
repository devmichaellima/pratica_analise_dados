# Desafio 07 - Cruzamento de Clientes e Ordens de Serviço

## Contexto

Até agora as análises foram feitas usando apenas um arquivo por vez. A partir deste desafio, o cenário fica mais próximo de uma empresa real.

No ERP, os dados geralmente ficam separados em tabelas diferentes. Uma tabela pode conter os dados dos clientes e outra pode conter as ordens de serviço. Para gerar uma análise completa, o analista precisa cruzar essas informações.

Neste desafio, você deverá relacionar uma base de clientes com uma base de ordens de serviço para criar uma visão analítica mais completa.

---

## Objetivo

Desenvolver uma análise utilizando Python e pandas para cruzar duas bases de dados: clientes e ordens de serviço.

Você deverá utilizar o campo `id_cliente` para relacionar os arquivos e gerar indicadores por cidade e por cliente.

---

## Estrutura Esperada do Projeto

```txt
dia_07/
│
├── data/
│   ├── clientes.csv
│   └── ordens_servico.csv
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

Crie manualmente o arquivo `clientes.csv` dentro da pasta `data/`.

```csv
id_cliente,nome_cliente,cidade
1,João,São Paulo
2,Maria,São Paulo
3,Ana,Guarulhos
4,Carlos,Suzano
5,Pedro,Mogi das Cruzes
6,Juliana,Guarulhos
```

Crie manualmente o arquivo `ordens_servico.csv` dentro da pasta `data/`.

```csv
id_os,id_cliente,servico,valor,status
1,1,Troca de Óleo,120,Finalizado
2,2,Alinhamento,80,Finalizado
3,1,Freio,350,Finalizado
4,4,Troca de Óleo,120,Pendente
5,2,Freio,300,Finalizado
6,3,Revisão,500,Finalizado
7,1,Revisão,500,Finalizado
8,4,Alinhamento,80,Finalizado
9,3,Freio,320,Pendente
10,2,Revisão,500,Finalizado
11,5,Bateria,450,Finalizado
12,6,Troca de Óleo,120,Finalizado
13,6,Freio,380,Finalizado
14,5,Bateria,420,Cancelado
15,3,Alinhamento,90,Finalizado
```

---

## Problema

A gestão quer entender o faturamento das ordens finalizadas, mas agora considerando os dados cadastrais dos clientes.

A empresa precisa responder:

Qual foi o faturamento total considerando apenas ordens finalizadas?

Quanto cada cliente faturou?

Quantas ordens finalizadas cada cliente realizou?

Qual foi o ticket médio por cliente?

Quanto cada cidade faturou?

Qual cidade teve maior faturamento?

---

## Regras

Utilize Python e pandas.

Leia os dois arquivos CSV.

Considere apenas ordens com status `Finalizado`.

Faça o cruzamento entre as ordens de serviço e os clientes utilizando a coluna `id_cliente`.

A análise final deve conter informações do cliente, cidade e faturamento.

Exporte o resultado em um arquivo chamado `relatorio_clientes.csv`.

---

## Sua Missão

Criar um relatório final por cliente com as seguintes colunas:

```csv
id_cliente,nome_cliente,cidade,faturamento_total,qtd_ordens,ticket_medio
```

O relatório deve estar ordenado pelo faturamento total em ordem decrescente.

Além do relatório por cliente, o script também deve calcular no código:

Faturamento total da empresa.

Faturamento por cidade.

Cidade com maior faturamento.

---

## Exemplo de Saída Esperada

```csv
id_cliente,nome_cliente,cidade,faturamento_total,qtd_ordens,ticket_medio
1,João,São Paulo,970,3,323.33
2,Maria,São Paulo,880,3,293.33
3,Ana,Guarulhos,590,2,295.00
6,Juliana,Guarulhos,500,2,250.00
5,Pedro,Mogi das Cruzes,450,1,450.00
4,Carlos,Suzano,80,1,80.00
```

Os valores acima servem como referência de estrutura. Valide os resultados com base nos dados do CSV.

---

## Entregáveis

Ao finalizar o desafio, entregue o arquivo `analise.py`, o arquivo `relatorio_clientes.csv` exportado na pasta `output` e o README do desafio na pasta do projeto.

---

## Tecnologias Utilizadas

Python e pandas.

---

## Competências Treinadas

Neste desafio serão treinadas as seguintes competências:

Leitura de múltiplos arquivos CSV.

Relacionamento entre tabelas.

Uso de `merge` no pandas.

Filtragem de dados.

Agrupamento por cliente.

Agrupamento por cidade.

Cálculo de faturamento total.

Cálculo de quantidade de ordens.

Cálculo de ticket médio.

Ordenação de dados.

Exportação de relatório analítico.

Pensamento de modelagem de dados.

---

## O Que Era Esperado

Era esperado que o analista conseguisse cruzar informações de duas bases diferentes e gerar uma visão analítica mais completa.

A solução deve demonstrar entendimento de relacionamento entre tabelas, conceito essencial para SQL, Power BI, bancos de dados e projetos reais de análise.

Este desafio inicia o Bloco 2 do treinamento, focado em cruzamento de dados, múltiplas fontes e preparação para modelagem analítica.
