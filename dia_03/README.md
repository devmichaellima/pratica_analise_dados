# Desafio 03 - Análise de Vendas por Período

## Contexto

Após a limpeza dos dados realizada anteriormente, a gestão da empresa deseja entender como o faturamento evoluiu ao longo do tempo.

O gerente acredita que existem dias com desempenho muito diferente dos demais e quer identificar padrões básicos de faturamento para apoiar futuras decisões comerciais.

Você recebeu uma nova exportação do ERP contendo apenas ordens finalizadas.

Seu trabalho é transformar os dados em indicadores que permitam uma análise temporal simples.

---

## Objetivo

Desenvolver uma análise utilizando Python e pandas para responder perguntas relacionadas ao faturamento diário da empresa.

O foco deste desafio é começar a trabalhar com agrupamentos por data e análises temporais.

---

## Estrutura Esperada do Projeto

```txt
dia_03/
│
├── data/
│   └── vendas_periodo.csv
│
├── src/
│   └── analise.py
│
├── output/
│   └── relatorio.csv
│
└── README.md
```

---

## Dados do CSV

Crie manualmente o arquivo `vendas_periodo.csv` dentro da pasta `data/`.

Conteúdo:

```csv
id_os,cliente,servico,valor,data_os
1,João,Troca de Óleo,120,2026-01-05
2,Maria,Alinhamento,80,2026-01-05
3,João,Freio,350,2026-01-06
4,Carlos,Troca de Óleo,120,2026-01-06
5,Maria,Freio,300,2026-01-08
6,Ana,Revisão,500,2026-01-08
7,João,Revisão,500,2026-01-10
8,Carlos,Alinhamento,80,2026-01-10
9,Ana,Freio,320,2026-01-12
10,Maria,Revisão,500,2026-01-12
11,Pedro,Bateria,450,2026-01-12
12,Ana,Troca de Óleo,120,2026-01-15
```

---

## Problema

A empresa quer entender o comportamento das vendas ao longo do período analisado.

O gerente precisa responder:

- Qual foi o faturamento total?
- Qual dia teve maior faturamento?
- Qual dia teve menor faturamento?
- Qual foi o faturamento médio por dia?
- Quantos dias tiveram vendas registradas?

---

## Regras

Utilize Python e pandas.

A coluna `data_os` deve ser convertida para o tipo data.

As análises devem ser feitas agrupando os registros por dia.

O código deve exportar um arquivo `relatorio.csv`.

Utilize nomes de variáveis claros e mantenha a organização do projeto.

---

## Sua Missão

Gerar as seguintes informações.

### 1. Total faturado no período

Calcule o valor total faturado considerando todos os registros.

---

### 2. Dia com maior faturamento

Identifique a data com maior faturamento.

Também informe o valor faturado nesse dia.

---

### 3. Dia com menor faturamento

Identifique a data com menor faturamento.

Também informe o valor faturado nesse dia.

---

### 4. Faturamento médio diário

Calcule a média de faturamento considerando apenas os dias que tiveram vendas.

---

### 5. Quantidade de dias com vendas

Calcule quantos dias possuem registros de vendas.

---

## Exemplo de Estrutura do Relatório

```csv
metrica,valor
total_faturado,3440
dia_maior_faturamento,2026-01-12
valor_dia_maior_faturamento,1270
dia_menor_faturamento,2026-01-15
valor_dia_menor_faturamento,120
faturamento_medio_diario,573.33
dias_com_vendas,6
```

---

## Tecnologias Utilizadas

- Python
- pandas

---

## Competências Treinadas

- Conversão de datas
- Agrupamento temporal
- Group By
- Agregações
- Métricas de negócio
- Análise temporal
- Exportação de relatórios
- Organização de projetos
- Pensamento analítico

---

## O Que Era Esperado

Era esperado que o analista conseguisse transformar registros operacionais em indicadores temporais que ajudassem a gestão a entender o comportamento das vendas.

O foco deste desafio é desenvolver a capacidade de analisar dados ao longo do tempo, uma das competências mais utilizadas no dia a dia de um Analista de Dados.