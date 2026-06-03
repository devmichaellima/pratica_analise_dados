# Desafio 09 - Cruzamento de Clientes, Ordens e Serviços

## Contexto

Nos desafios anteriores, você aprendeu a cruzar clientes e ordens de serviço. Agora o cenário ficará mais próximo de um ambiente real de dados.

Em muitos sistemas, as informações não ficam todas em uma única tabela. O ERP pode ter uma tabela de clientes, uma tabela de ordens e uma tabela de serviços. Para gerar uma análise completa, o analista precisa relacionar essas tabelas corretamente.

Neste desafio, você deverá cruzar três arquivos para construir uma visão analítica de faturamento por cliente, cidade e categoria de serviço.

---

## Objetivo

Desenvolver uma análise utilizando Python e pandas para relacionar três bases de dados: clientes, ordens de serviço e cadastro de serviços.

Você deverá usar os campos de relacionamento corretos para consolidar os dados e gerar indicadores de negócio.

---

## Estrutura Esperada do Projeto

```txt
dia_09/
│
├── data/
│   ├── clientes.csv
│   ├── servicos.csv
│   └── ordens_servico.csv
│
├── src/
│   └── analise.py
│
├── output/
│   ├── relatorio_clientes.csv
│   ├── relatorio_categorias.csv
│   └── relatorio_cidades.csv
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

Crie manualmente o arquivo `servicos.csv` dentro da pasta `data/`.

```csv
id_servico,nome_servico,categoria
1,Troca de Óleo,Manutenção
2,Alinhamento,Serviços Rápidos
3,Freio,Segurança
4,Revisão,Manutenção
5,Bateria,Elétrica
```

Crie manualmente o arquivo `ordens_servico.csv` dentro da pasta `data/`.

```csv
id_os,id_cliente,id_servico,valor,status,data_os
1,1,1,120,Finalizado,2026-01-05
2,2,2,80,Finalizado,2026-01-05
3,1,3,350,Finalizado,2026-01-06
4,4,1,120,Pendente,2026-01-06
5,2,3,300,Finalizado,2026-01-08
6,3,4,500,Finalizado,2026-01-08
7,1,4,500,Finalizado,2026-01-10
8,4,2,80,Finalizado,2026-01-10
9,3,3,320,Pendente,2026-01-12
10,2,4,500,Finalizado,2026-01-12
11,5,5,450,Finalizado,2026-01-12
12,6,1,120,Finalizado,2026-01-15
13,6,3,380,Finalizado,2026-01-15
14,5,5,420,Cancelado,2026-01-18
15,3,2,90,Finalizado,2026-01-18
16,2,1,130,Finalizado,2026-01-20
17,1,5,470,Finalizado,2026-01-20
18,6,4,550,Finalizado,2026-01-22
```

---

## Problema

A gestão quer uma análise mais completa sobre o faturamento, agora considerando cliente, cidade, serviço e categoria do serviço.

A empresa precisa responder:

Qual foi o faturamento total considerando apenas ordens finalizadas?

Quanto cada cliente faturou?

Quanto cada cidade faturou?

Quanto cada categoria de serviço faturou?

Qual categoria teve maior faturamento?

Qual foi o ticket médio por categoria?

Quantas ordens finalizadas existem por categoria?

---

## Regras

Utilize Python e pandas.

Leia os três arquivos CSV.

Considere apenas ordens com status `Finalizado`.

Relacione ordens com clientes utilizando `id_cliente`.

Relacione ordens com serviços utilizando `id_servico`.

Converta a coluna `data_os` para data.

Gere três relatórios finais:

`relatorio_clientes.csv`

`relatorio_categorias.csv`

`relatorio_cidades.csv`

Todos os relatórios devem estar ordenados pelo faturamento total em ordem decrescente.

---

## Sua Missão

Criar três arquivos de saída.

O primeiro arquivo deve ser `relatorio_clientes.csv`, com a estrutura:

```csv
id_cliente,nome_cliente,cidade,faturamento_total,qtd_ordens,ticket_medio
```

O segundo arquivo deve ser `relatorio_categorias.csv`, com a estrutura:

```csv
categoria,faturamento_total,qtd_ordens,ticket_medio,participacao_percentual
```

O terceiro arquivo deve ser `relatorio_cidades.csv`, com a estrutura:

```csv
cidade,faturamento_total,qtd_ordens,ticket_medio,participacao_percentual
```

Além dos arquivos, o script deve calcular no código:

Faturamento total da empresa.

Categoria com maior faturamento.

Cidade com maior faturamento.

Cliente com maior faturamento.

---

## Dica Técnica

Você pode fazer os cruzamentos em etapas.

Primeiro, relacione ordens e clientes:

```python
df = ordens.merge(
    clientes,
    how='left',
    on='id_cliente'
)
```

Depois, relacione o resultado com serviços:

```python
df = df.merge(
    servicos,
    how='left',
    on='id_servico'
)
```

Após isso, filtre apenas ordens finalizadas e crie os relatórios.

---

## Entregáveis

Ao finalizar o desafio, entregue o arquivo `analise.py` e os três arquivos CSV exportados na pasta `output`.

O README do desafio deve estar na pasta do projeto.

---

## Tecnologias Utilizadas

Python e pandas.

---

## Competências Treinadas

Neste desafio serão treinadas as seguintes competências:

Leitura de múltiplos arquivos CSV.

Relacionamento entre três tabelas.

Uso de `merge` em etapas.

Conceito de tabela fato e tabelas dimensão.

Filtragem de dados.

Conversão de datas.

Agrupamento por cliente.

Agrupamento por cidade.

Agrupamento por categoria.

Cálculo de faturamento total.

Cálculo de quantidade de ordens.

Cálculo de ticket médio.

Cálculo de participação percentual.

Exportação de múltiplos relatórios.

Pensamento de modelagem analítica.

Preparação para SQL JOIN e relacionamentos no Power BI.

---

## O Que Era Esperado

Era esperado que o analista conseguisse consolidar dados espalhados em três tabelas diferentes e transformar essas informações em relatórios úteis para gestão.

A solução deve demonstrar entendimento de relacionamento entre bases, consolidação de dados e criação de indicadores a partir de múltiplas fontes.

O foco deste desafio é aproximar o treinamento de um cenário real de modelagem de dados, preparando a transição para SQL, banco de dados e Power BI.
