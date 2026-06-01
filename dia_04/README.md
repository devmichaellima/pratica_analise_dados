# Desafio 04 - Ranking de Clientes e Análise de Receita

## Contexto

Após analisar o faturamento por período, a gestão da empresa quer entender quais clientes possuem maior impacto financeiro no negócio.

O objetivo é identificar os clientes mais relevantes para a empresa e gerar um ranking de faturamento.

Essa análise será utilizada futuramente para campanhas comerciais, programas de fidelização e ações de relacionamento com clientes.

---

## Objetivo

Desenvolver uma análise utilizando Python e pandas para identificar os clientes mais importantes da operação através do faturamento gerado.

Você deverá calcular indicadores e criar um ranking de clientes.

---

## Estrutura Esperada do Projeto

```txt
dia_04/
│
├── data/
│   └── clientes_faturamento.csv
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

Crie manualmente o arquivo `clientes_faturamento.csv` dentro da pasta `data/`.

Conteúdo:

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

A empresa quer responder as seguintes perguntas:

- Qual foi o faturamento total da empresa?
- Quanto cada cliente faturou?
- Quem foi o cliente que mais gerou receita?
- Qual foi o faturamento médio por cliente?
- Quais são os 3 clientes com maior faturamento?

---

## Regras

Utilize Python e pandas.

A análise deve ser feita utilizando agrupamentos por cliente.

O ranking deve ser criado em ordem decrescente de faturamento.

O código deve exportar um arquivo `relatorio.csv`.

Utilize nomes de variáveis claros e mantenha a organização do projeto.

---

## Sua Missão

Gerar as seguintes informações.

### 1. Faturamento total

Calcule o faturamento total da empresa.

---

### 2. Faturamento por cliente

Agrupe os dados por cliente e calcule o faturamento total de cada um.

---

### 3. Cliente com maior faturamento

Identifique o cliente que mais gerou receita.

Também informe o valor faturado.

---

### 4. Faturamento médio por cliente

Calcule a média de faturamento considerando todos os clientes.

---

### 5. Top 3 clientes

Crie um ranking contendo os 3 clientes com maior faturamento.

---

## Exemplo de Estrutura do Relatório

```csv
metrica,valor
faturamento_total,4190
cliente_maior_faturamento,João
valor_maior_faturamento,1170
faturamento_medio_cliente,838
```

---

## Tecnologias Utilizadas

- Python
- pandas

---

## Competências Treinadas

- Group By
- Ordenação de dados
- Ranking
- Agregações
- Métricas de negócio
- Análise de receita
- Exportação de relatórios
- Organização de projetos
- Pensamento analítico

---

## O Que Era Esperado

Era esperado que o analista conseguisse transformar dados operacionais em informações úteis para tomada de decisão comercial.

O foco deste desafio é desenvolver a capacidade de criar rankings, comparar desempenhos e identificar quais clientes possuem maior impacto financeiro no negócio.
