# Desafio 08 - Validação de Dados entre Clientes e Ordens

## Contexto

No desafio anterior, você cruzou dados de clientes e ordens de serviço utilizando o campo `id_cliente`.

Agora o cenário será mais realista. A empresa recebeu uma nova exportação do ERP, mas existem problemas de qualidade nos dados. Algumas ordens fazem referência a clientes que não existem na base de clientes.

Esse tipo de problema é comum em empresas que possuem dados cadastrados manualmente, sistemas antigos ou integrações mal controladas.

O papel do analista é identificar essas inconsistências antes de gerar indicadores, porque relatórios criados com dados incompletos podem gerar decisões erradas.

---

## Objetivo

Desenvolver uma análise utilizando Python e pandas para validar a relação entre clientes e ordens de serviço.

Você deverá cruzar as tabelas, identificar ordens sem cadastro de cliente correspondente e gerar relatórios separados para dados válidos e dados inconsistentes.

---

## Estrutura Esperada do Projeto

```txt
dia_08/
│
├── data/
│   ├── clientes.csv
│   └── ordens_servico.csv
│
├── src/
│   └── analise.py
│
├── output/
│   ├── relatorio_clientes.csv
│   └── ordens_sem_cliente.csv
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
16,99,Revisão,600,Finalizado
17,100,Freio,400,Finalizado
```

---

## Problema

A gestão quer gerar um relatório de faturamento por cliente, mas antes disso é necessário validar se todas as ordens possuem cliente cadastrado.

A empresa precisa responder:

Quantas ordens possuem cliente válido?

Quantas ordens estão sem cliente cadastrado?

Quais ordens possuem `id_cliente` sem correspondência na tabela de clientes?

Qual foi o faturamento total válido considerando apenas ordens finalizadas com cliente cadastrado?

Quanto cada cliente válido faturou?

---

## Regras

Utilize Python e pandas.

Leia os dois arquivos CSV.

Faça o cruzamento entre ordens e clientes utilizando `id_cliente`.

Use um tipo de merge que permita identificar ordens que não encontraram cliente correspondente.

Considere como inconsistentes as ordens que possuem `id_cliente` sem cadastro na base de clientes.

O relatório final de clientes deve considerar apenas ordens finalizadas e com cliente válido.

As ordens inconsistentes devem ser exportadas em um arquivo separado chamado `ordens_sem_cliente.csv`.

O relatório de clientes deve ser exportado em um arquivo chamado `relatorio_clientes.csv`.

---

## Sua Missão

Criar dois arquivos de saída.

O primeiro arquivo deve ser `relatorio_clientes.csv`, contendo o faturamento por cliente válido.

Estrutura esperada:

```csv
id_cliente,nome_cliente,cidade,faturamento_total,qtd_ordens,ticket_medio
```

O segundo arquivo deve ser `ordens_sem_cliente.csv`, contendo as ordens que não possuem cliente correspondente na base de clientes.

Estrutura esperada:

```csv
id_os,id_cliente,servico,valor,status
```

Além dos arquivos, o script deve calcular no código:

Quantidade de ordens com cliente válido.

Quantidade de ordens sem cliente cadastrado.

Faturamento total válido.

---

## Dica Técnica

Neste desafio, pesquise e teste o parâmetro `indicator=True` no `merge`.

Ele permite criar uma coluna indicando se o registro apareceu nas duas tabelas ou apenas em uma delas.

Exemplo conceitual:

```python
df = ordens.merge(
    clientes,
    how='left',
    on='id_cliente',
    indicator=True
)
```

A coluna criada ajuda a identificar registros com ou sem correspondência.

---

## Entregáveis

Ao finalizar o desafio, entregue o arquivo `analise.py`, o arquivo `relatorio_clientes.csv`, o arquivo `ordens_sem_cliente.csv` e o README do desafio na pasta do projeto.

---

## Tecnologias Utilizadas

Python e pandas.

---

## Competências Treinadas

Neste desafio serão treinadas as seguintes competências:

Leitura de múltiplos arquivos CSV.

Relacionamento entre tabelas.

Uso de `merge` com validação.

Identificação de registros sem correspondência.

Tratamento de inconsistências entre bases.

Filtragem de dados válidos.

Criação de relatórios separados.

Cálculo de métricas confiáveis.

Pensamento de qualidade de dados.

Preparação para conceitos de JOIN em SQL.

---

## O Que Era Esperado

Era esperado que o analista conseguisse identificar problemas de relacionamento entre tabelas antes de gerar relatórios de negócio.

A solução deve demonstrar capacidade de validar dados, separar registros inconsistentes e gerar indicadores apenas com dados confiáveis.

O foco deste desafio é entender que análise de dados também envolve controle de qualidade, não apenas cálculo de métricas.
