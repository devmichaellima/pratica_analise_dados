# Desafio 01 - Análise de Ordens de Serviço

## Contexto

Uma empresa do setor automotivo precisava entender quais clientes geram maior faturamento e quais serviços possuem maior valor médio nas ordens de serviço finalizadas.

O objetivo deste desafio é simular uma situação real de trabalho onde um analista de dados recebe um arquivo exportado do ERP e precisa transformar os dados em informações úteis para gestão.

---

## Objetivo

Desenvolver uma análise simples utilizando Python e pandas para gerar indicadores operacionais da empresa.

Você deverá:

- Ler um arquivo CSV
- Filtrar apenas ordens finalizadas
- Gerar métricas de negócio
- Exportar um relatório final em CSV

---

## Estrutura Esperada do Projeto

```txt
/desafio-01-analise-os
│
├── data/
│   └── ordens_servico.csv
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

Crie manualmente o arquivo `ordens_servico.csv` dentro da pasta `data/`.

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
```

---

## Regras

- Utilizar Python
- Utilizar pandas
- Ignorar ordens pendentes
- Utilizar nomes de variáveis claros
- Organizar o projeto corretamente
- O código deve rodar sem alterações manuais

---

## Sua Missão

Gerar as seguintes informações:

### 1. Cliente com maior faturamento

Exemplo esperado:

```txt
João - 970
```

---

### 2. Serviço com maior valor médio

Exemplo esperado:

```txt
Revisão - 500
```

---

### 3. Total faturado considerando apenas ordens finalizadas

---

### 4. Quantidade de ordens finalizadas

---

### 5. Exportar um relatório CSV

O arquivo `relatorio.csv` deve conter as métricas finais calculadas.

Exemplo de estrutura:

```csv
metrica,valor
total_faturado,2430
qtd_os_finalizadas,8
cliente_maior_faturamento,João
servico_maior_ticket,Revisão
```

---

## Tecnologias Utilizadas

- Python
- pandas

---

## Competências Treinadas

- Manipulação de dados com pandas
- Leitura de arquivos CSV
- Filtragem de dados
- Group By
- Agregações
- Exportação de arquivos
- Organização de projeto
- Pensamento analítico
- Visão de negócio

---

## O Que Era Esperado

Esperava-se uma solução organizada, legível e capaz de transformar dados operacionais em informações úteis para tomada de decisão.

O foco principal deste desafio é começar a desenvolver mentalidade analítica e organização profissional de projetos de dados.

