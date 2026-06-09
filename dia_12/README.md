# Desafio 12 - SQL JOIN entre Clientes e Ordens de Serviço

## Contexto

No desafio anterior, você começou a consultar dados em SQL utilizando uma única tabela de ordens de serviço.

Agora o cenário fica mais próximo de um banco de dados real. Em sistemas de ERP, os dados geralmente ficam separados em tabelas diferentes. Uma tabela armazena os clientes e outra armazena as ordens de serviço.

Para gerar análises completas, o analista precisa cruzar essas tabelas usando `JOIN`.

Esse conceito é essencial para SQL, Power BI, modelagem de dados e bancos relacionais.

---

## Objetivo

Desenvolver consultas SQL utilizando `JOIN` para relacionar clientes e ordens de serviço.

Você deverá criar duas tabelas, inserir dados e escrever consultas para responder perguntas de negócio envolvendo faturamento por cliente e por cidade.

---

## Estrutura Esperada do Projeto

```txt
dia_12/
│
├── sql/
│   └── consultas.sql
└── README.md
```

---

## Tabelas Utilizadas

Neste desafio serão utilizadas duas tabelas.

A tabela `clientes` representa o cadastro dos clientes.

```sql
id_cliente INTEGER
nome_cliente VARCHAR(50)
cidade VARCHAR(50)
```

A tabela `ordens_servico` representa as ordens realizadas.

```sql
id_os INTEGER
id_cliente INTEGER
servico VARCHAR(50)
valor NUMERIC
status VARCHAR(50)
data_os DATE
```

---

## Script de Criação das Tabelas

Utilize este script para criar as tabelas:

```sql
CREATE TABLE clientes (
    id_cliente INTEGER,
    nome_cliente VARCHAR(50),
    cidade VARCHAR(50)
);

CREATE TABLE ordens_servico (
    id_os INTEGER,
    id_cliente INTEGER,
    servico VARCHAR(50),
    valor NUMERIC,
    status VARCHAR(50),
    data_os DATE
);
```

---

## Dados para Inserção

Insira os dados abaixo na tabela `clientes`:

```sql
INSERT INTO clientes (id_cliente, nome_cliente, cidade) VALUES
(1, 'João', 'São Paulo'),
(2, 'Maria', 'São Paulo'),
(3, 'Ana', 'Guarulhos'),
(4, 'Carlos', 'Suzano'),
(5, 'Pedro', 'Mogi das Cruzes'),
(6, 'Juliana', 'Guarulhos');
```

Insira os dados abaixo na tabela `ordens_servico`:

```sql
INSERT INTO ordens_servico (id_os, id_cliente, servico, valor, status, data_os) VALUES
(1, 1, 'Troca de Óleo', 120, 'Finalizado', '2026-01-05'),
(2, 2, 'Alinhamento', 80, 'Finalizado', '2026-01-05'),
(3, 1, 'Freio', 350, 'Finalizado', '2026-01-06'),
(4, 4, 'Troca de Óleo', 120, 'Pendente', '2026-01-06'),
(5, 2, 'Freio', 300, 'Finalizado', '2026-01-08'),
(6, 3, 'Revisão', 500, 'Finalizado', '2026-01-08'),
(7, 1, 'Revisão', 500, 'Finalizado', '2026-01-10'),
(8, 4, 'Alinhamento', 80, 'Finalizado', '2026-01-10'),
(9, 3, 'Freio', 320, 'Pendente', '2026-01-12'),
(10, 2, 'Revisão', 500, 'Finalizado', '2026-01-12'),
(11, 5, 'Bateria', 450, 'Finalizado', '2026-01-12'),
(12, 6, 'Troca de Óleo', 120, 'Finalizado', '2026-01-15'),
(13, 6, 'Freio', 380, 'Finalizado', '2026-01-15'),
(14, 5, 'Bateria', 420, 'Cancelado', '2026-01-18'),
(15, 3, 'Alinhamento', 90, 'Finalizado', '2026-01-18');
```

---

## Problema

A gestão quer analisar o faturamento das ordens finalizadas, mas agora considerando os dados cadastrais dos clientes.

A empresa precisa responder:

Quais ordens finalizadas existem com nome do cliente e cidade?

Quanto cada cliente faturou?

Quanto cada cidade faturou?

Qual cliente teve maior faturamento?

Qual cidade teve maior faturamento?

Qual foi o ticket médio por cliente?

---

## Sua Missão

Crie um arquivo chamado `consultas.sql` e escreva as consultas para responder às perguntas abaixo.

### 1. Listar ordens finalizadas com dados do cliente

Retorne as colunas:

```sql
id_os
id_cliente
nome_cliente
cidade
servico
valor
status
data_os
```

A consulta deve trazer apenas ordens com status `Finalizado`.

---

### 2. Calcular faturamento por cliente

Retorne:

```sql
id_cliente
nome_cliente
cidade
faturamento_total
```

Considere apenas ordens finalizadas.

Ordene pelo maior faturamento.

---

### 3. Calcular quantidade de ordens por cliente

Retorne:

```sql
id_cliente
nome_cliente
qtd_ordens
```

Considere apenas ordens finalizadas.

Ordene pela maior quantidade de ordens.

---

### 4. Calcular ticket médio por cliente

Retorne:

```sql
id_cliente
nome_cliente
ticket_medio
```

Considere apenas ordens finalizadas.

Ordene pelo maior ticket médio.

---

### 5. Calcular faturamento por cidade

Retorne:

```sql
cidade
faturamento_total
```

Considere apenas ordens finalizadas.

Ordene pelo maior faturamento.

---

### 6. Identificar cliente com maior faturamento

Retorne apenas o cliente com maior faturamento.

---

### 7. Identificar cidade com maior faturamento

Retorne apenas a cidade com maior faturamento.

---

## Regras

Utilize SQL.

Utilize `INNER JOIN` para relacionar clientes e ordens.

Utilize `ON` para definir a chave de ligação entre as tabelas.

Utilize `WHERE` para filtrar ordens finalizadas.

Utilize `SUM`, `COUNT` e `AVG` para calcular métricas.

Utilize `GROUP BY` para agrupar dados.

Utilize `ORDER BY` para ordenar resultados.

Utilize `LIMIT` para retornar o maior resultado quando necessário.

Finalize cada consulta com ponto e vírgula.

---

## Dica Técnica

O relacionamento entre as tabelas deve ser feito pelo campo `id_cliente`.

Exemplo:

```sql
SELECT
    o.id_os,
    c.nome_cliente,
    c.cidade,
    o.servico,
    o.valor
FROM ordens_servico AS o
INNER JOIN clientes AS c
    ON o.id_cliente = c.id_cliente;
```

Neste exemplo:

`o` é um apelido para `ordens_servico`.

`c` é um apelido para `clientes`.

Esses apelidos são chamados de aliases e ajudam a deixar a consulta mais curta e legível.

---

## Entregáveis

Ao finalizar o desafio, entregue o arquivo `consultas.sql`.

O arquivo deve conter:

Criação das tabelas.

Inserção dos dados.

Consultas respondendo às perguntas do desafio.

Comentários identificando cada consulta.

---

## Tecnologias Utilizadas

SQL e PostgreSQL.

---

## Competências Treinadas

Neste desafio serão treinadas as seguintes competências:

Criação de múltiplas tabelas.

Inserção de dados em tabelas relacionadas.

Uso de `INNER JOIN`.

Uso de aliases em SQL.

Relacionamento entre tabelas por chave.

Filtragem com `WHERE`.

Agregação com `SUM`, `COUNT` e `AVG`.

Agrupamento com `GROUP BY`.

Ordenação com `ORDER BY`.

Limitação de resultados com `LIMIT`.

Tradução do `merge()` do pandas para `JOIN` em SQL.

Pensamento relacional aplicado à análise de dados.

---

## O Que Era Esperado

Era esperado que o analista conseguisse relacionar duas tabelas em SQL e gerar indicadores de negócio a partir dessa união.

A solução deve demonstrar entendimento de relacionamento entre tabelas, leitura de dados relacionais e construção de consultas analíticas.

Este desafio consolida a transição entre pandas e SQL, usando o mesmo raciocínio de cruzamento de dados já treinado anteriormente.
