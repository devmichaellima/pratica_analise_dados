# Desafio 02 - Limpeza e Análise de Ordens de Serviço

## Contexto

A empresa recebeu uma nova exportação do ERP com dados de ordens de serviço, mas o arquivo contém inconsistências comuns em bases reais.

Alguns status estão escritos de formas diferentes, alguns valores estão ausentes, existem espaços desnecessários em textos e as datas precisam ser tratadas corretamente para permitir análise por período.

O objetivo deste desafio é preparar os dados antes de gerar os indicadores. Em uma empresa real, nem sempre os dados chegam prontos para análise. Parte importante do trabalho do analista é identificar problemas, corrigir inconsistências e garantir que os resultados sejam confiáveis.

---

## Objetivo

Desenvolver um script em Python utilizando pandas para limpar os dados de ordens de serviço e gerar indicadores operacionais a partir das ordens finalizadas.

Você deverá ler um arquivo CSV, tratar inconsistências, filtrar os dados corretos, calcular métricas e exportar um relatório final.

---

## Estrutura Esperada do Projeto

```txt
dia_02/
│
├── data/
│   └── ordens_servico_sujas.csv
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

Crie manualmente o arquivo `ordens_servico_sujas.csv` dentro da pasta `data/`.

Conteúdo:

```csv
id_os,cliente,servico,valor,status,data_os
1,João,Troca de Óleo,120,Finalizado,2026-01-05
2,Maria,Alinhamento,80,finalizado,2026-01-06
3,João,Freio,350,Finalizado ,2026-01-08
4,Carlos,Troca de Óleo,120,Pendente,2026-01-09
5,Maria,Freio,,Finalizado,2026-01-10
6,Ana,Revisão,500,Finalizado,2026-01-12
7,João,Revisão,500,FINALIZADO,2026-01-15
8,Carlos,Alinhamento,80,Finalizado,2026-01-16
9,Ana,Freio,320,Pendente,2026-01-18
10,Maria,Revisão,500,Finalizado,2026-01-20
11,Pedro,Bateria,450,Cancelado,2026-01-21
12,Ana,Troca de Óleo,120,finalizado,2026-01-22
```

---

## Problema

A gestão quer saber o desempenho das ordens de serviço finalizadas, mas os dados possuem problemas que precisam ser corrigidos antes da análise.

O arquivo contém status com letras maiúsculas e minúsculas misturadas, status com espaços extras, valores ausentes, datas em formato de texto e ordens pendentes ou canceladas que não devem entrar no faturamento.

---

## Regras

Você deve utilizar Python e pandas.

O script deve limpar a coluna `status`, removendo espaços desnecessários e padronizando os valores para permitir o filtro correto das ordens finalizadas.

A coluna `valor` deve ser tratada para permitir cálculos. Caso existam valores ausentes, substitua por zero.

A coluna `data_os` deve ser convertida para o tipo de data.

A análise deve considerar apenas ordens com status finalizado.

O código deve exportar um arquivo `relatorio.csv` dentro da pasta `output`.

---

## Sua Missão

Gerar as seguintes informações.

### 1. Total faturado

Calcule o total faturado considerando apenas ordens finalizadas.

### 2. Quantidade de ordens finalizadas

Calcule quantas ordens de serviço foram finalizadas.

### 3. Cliente com maior faturamento

Identifique qual cliente gerou maior faturamento nas ordens finalizadas.

### 4. Serviço com maior valor médio

Identifique qual serviço teve o maior valor médio nas ordens finalizadas.

### 5. Primeiro e último dia com ordem finalizada

Identifique a menor e a maior data entre as ordens finalizadas.

---

## Exemplo de Estrutura do Relatório

O arquivo `relatorio.csv` pode seguir a estrutura abaixo:

```csv
metrica,valor
total_faturado,2250
qtd_os_finalizadas,9
cliente_maior_faturamento,João
valor_cliente_maior_faturamento,970
servico_maior_media,Revisão
valor_servico_maior_media,500
primeira_data_finalizada,2026-01-05
ultima_data_finalizada,2026-01-22
```

---

## Tecnologias Utilizadas

Python e pandas.

---

## Competências Treinadas

Neste desafio serão treinadas as seguintes competências:

Leitura de arquivos CSV com pandas.

Limpeza e padronização de dados textuais.

Tratamento de valores ausentes.

Conversão de colunas para tipo de data.

Filtragem de registros.

Agrupamentos e agregações.

Criação de métricas operacionais.

Exportação de relatório em CSV.

Pensamento analítico aplicado a dados reais de negócio.

---

## O Que Era Esperado

Era esperado que o script conseguisse transformar uma base inconsistente em uma análise confiável.

A solução deve demonstrar que o analista consegue lidar com problemas comuns de dados antes de gerar indicadores para tomada de decisão.

O foco deste desafio é entender que análise de dados não começa nos gráficos. Ela começa na qualidade da base utilizada.
