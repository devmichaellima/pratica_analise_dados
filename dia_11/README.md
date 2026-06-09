# Desafio 11 - Primeiras Consultas SQL em Ordens de Serviço

## Contexto

Após consolidar os fundamentos de análise com Python e pandas, o treinamento avança para SQL.

SQL é uma das competências mais importantes para Analista de Dados, porque grande parte dos dados reais das empresas está armazenada em bancos relacionais.

Neste desafio, você começará a consultar dados de ordens de serviço usando comandos básicos de SQL, conectando o raciocínio que já treinou em pandas com a linguagem usada em bancos de dados.

---

## Objetivo

Desenvolver consultas SQL para analisar uma tabela de ordens de serviço.

Você deverá criar uma tabela, inserir dados e escrever consultas para responder perguntas de negócio sobre faturamento, quantidade de ordens, clientes e serviços.

---

## Estrutura Esperada do Projeto

```txt
dia_11/
│
├── sql/
│   └── consultas.sql
└── README.md
```

---

## Tabela Utilizada

Crie uma tabela chamada `ordens_servico`.

A tabela deve conter as seguintes colunas:

```sql
id_os INTEGER
cliente TEXT
servico TEXT
valor NUMERIC
status TEXT
data_os DATE
```

---

## Script de Criação da Tabela

Utilize este script para criar a tabela:

```sql
CREATE TABLE ordens_servico (
    id_os INTEGER,
    cliente TEXT,
    servico TEXT,
    valor NUMERIC,
    status TEXT,
    data_os DATE
);
```

---

## Dados para Inserção

Insira os dados abaixo na tabela:

```sql
INSERT INTO ordens_servico (id_os, cliente, servico, valor, status, data_os) VALUES
(1, 'João', 'Troca de Óleo', 120, 'Finalizado', '2026-01-05'),
(2, 'Maria', 'Alinhamento', 80, 'Finalizado', '2026-01-05'),
(3, 'João', 'Freio', 350, 'Finalizado', '2026-01-06'),
(4, 'Carlos', 'Troca de Óleo', 120, 'Pendente', '2026-01-06'),
(5, 'Maria', 'Freio', 300, 'Finalizado', '2026-01-08'),
(6, 'Ana', 'Revisão', 500, 'Finalizado', '2026-01-08'),
(7, 'João', 'Revisão', 500, 'Finalizado', '2026-01-10'),
(8, 'Carlos', 'Alinhamento', 80, 'Finalizado', '2026-01-10'),
(9, 'Ana', 'Freio', 320, 'Pendente', '2026-01-12'),
(10, 'Maria', 'Revisão', 500, 'Finalizado', '2026-01-12'),
(11, 'Pedro', 'Bateria', 450, 'Finalizado', '2026-01-12'),
(12, 'Ana', 'Troca de Óleo', 120, 'Finalizado', '2026-01-15'),
(13, 'João', 'Freio', 380, 'Finalizado', '2026-01-15'),
(14, 'Carlos', 'Bateria', 420, 'Cancelado', '2026-01-18'),
(15, 'Maria', 'Alinhamento', 90, 'Finalizado', '2026-01-18');
```

---

## Problema

A gestão quer começar a consultar os dados diretamente no banco.

Seu trabalho é escrever consultas SQL para responder perguntas simples de negócio, considerando apenas ordens com status `Finalizado` quando o indicador envolver faturamento ou ordens concluídas.

---

## Sua Missão

Crie um arquivo chamado `consultas.sql` e escreva as consultas para responder às perguntas abaixo.

### 1. Listar todas as ordens de serviço

Retorne todos os registros da tabela.

### 2. Listar apenas ordens finalizadas

Retorne apenas ordens com status `Finalizado`.

### 3. Calcular o faturamento total

Calcule o faturamento total considerando apenas ordens finalizadas.

### 4. Calcular a quantidade de ordens finalizadas

Calcule quantas ordens possuem status `Finalizado`.

### 5. Calcular o faturamento por cliente

Agrupe os dados por cliente e calcule o faturamento total de cada um.

O resultado deve estar ordenado do maior para o menor faturamento.

### 6. Calcular o faturamento por serviço

Agrupe os dados por serviço e calcule o faturamento total de cada serviço.

O resultado deve estar ordenado do maior para o menor faturamento.

### 7. Identificar o cliente com maior faturamento

Retorne apenas o cliente com maior faturamento total.

### 8. Identificar o serviço com maior ticket médio

Calcule o ticket médio por serviço e retorne o serviço com maior média.

---

## Regras

Utilize SQL.

Utilize `WHERE` para filtrar ordens finalizadas.

Utilize `SUM` para calcular faturamento.

Utilize `COUNT` para contar ordens.

Utilize `AVG` para calcular ticket médio.

Utilize `GROUP BY` para agrupar clientes e serviços.

Utilize `ORDER BY` para ordenar resultados.

Utilize `LIMIT` para retornar apenas o maior resultado quando necessário.

---

## Entregáveis

Ao finalizar o desafio, entregue o arquivo `consultas.sql`.

O arquivo deve conter:

Criação da tabela.

Inserção dos dados.

Consultas respondendo às perguntas do desafio.

Comentários identificando cada consulta.

---

## Tecnologias Utilizadas

SQL e PostgreSQL.

---

## Competências Treinadas

Neste desafio serão treinadas as seguintes competências:

Criação de tabela.

Inserção de registros.

Consulta de dados com `SELECT`.

Filtragem com `WHERE`.

Agregação com `SUM`, `COUNT` e `AVG`.

Agrupamento com `GROUP BY`.

Ordenação com `ORDER BY`.

Limitação de resultados com `LIMIT`.

Tradução de perguntas de negócio para consultas SQL.

Raciocínio analítico em banco de dados relacional.

---

## O Que Era Esperado

Era esperado que o analista conseguisse transformar perguntas simples de negócio em consultas SQL.

A solução deve demonstrar domínio inicial de leitura, filtro, agregação, agrupamento e ordenação em SQL.

Este desafio marca a transição do raciocínio feito em pandas para consultas em banco de dados.
