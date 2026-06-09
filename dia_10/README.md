# Desafio 10 - Resumo Executivo Automatizado

## Contexto

A empresa já possui relatórios separados por cliente, cidade e categoria de serviço. Agora a gestão quer um resumo executivo com os principais indicadores do período em um único arquivo.

Esse tipo de entrega é comum em empresas, porque nem sempre o gestor quer analisar tabelas detalhadas. Muitas vezes ele precisa de uma visão rápida com os principais números do negócio.

Neste desafio, você deverá criar relatórios detalhados e também um resumo executivo consolidado.

---

## Objetivo

Desenvolver uma análise utilizando Python e pandas para consolidar dados de clientes, ordens de serviço e serviços, gerando relatórios detalhados e um resumo executivo.

Você deverá cruzar três tabelas, calcular indicadores principais e exportar múltiplos arquivos de saída.

---

## Estrutura Esperada do Projeto

```txt
dia_10/
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
│   ├── resumo_executivo.csv
│   ├── relatorio_clientes.csv
│   ├── relatorio_categorias.csv
│   └── relatorio_cidades.csv
└── README.md
```

---

## Dados do CSV

Utilize os mesmos arquivos do Desafio 09.

Caso prefira criar novamente, use as bases abaixo.

Arquivo `clientes.csv`:

```csv
id_cliente,nome_cliente,cidade
1,João,São Paulo
2,Maria,São Paulo
3,Ana,Guarulhos
4,Carlos,Suzano
5,Pedro,Mogi das Cruzes
6,Juliana,Guarulhos
```

Arquivo `servicos.csv`:

```csv
id_servico,nome_servico,categoria
1,Troca de Óleo,Manutenção
2,Alinhamento,Serviços Rápidos
3,Freio,Segurança
4,Revisão,Manutenção
5,Bateria,Elétrica
```

Arquivo `ordens_servico.csv`:

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

A gestão quer receber um resumo com os principais indicadores do período.

A empresa precisa responder:

Qual foi o faturamento total?

Quantas ordens foram finalizadas?

Qual foi o ticket médio geral?

Qual foi o cliente com maior faturamento?

Qual foi a cidade com maior faturamento?

Qual foi a categoria com maior faturamento?

Qual foi a primeira data de venda finalizada?

Qual foi a última data de venda finalizada?

---

## Regras

Utilize Python e pandas.

Leia os três arquivos CSV.

Relacione ordens com clientes utilizando `id_cliente`.

Relacione ordens com serviços utilizando `id_servico`.

Converta a coluna `data_os` para data.

Considere apenas ordens com status `Finalizado`.

Crie relatórios detalhados por cliente, cidade e categoria.

Crie também um arquivo `resumo_executivo.csv`.

Todos os relatórios detalhados devem estar ordenados pelo faturamento total em ordem decrescente.

---

## Sua Missão

Criar quatro arquivos de saída.

O arquivo `resumo_executivo.csv` deve conter a seguinte estrutura:

```csv
metrica,valor
faturamento_total,4690
qtd_ordens_finalizadas,15
ticket_medio_geral,312.67
cliente_maior_faturamento,João
cidade_maior_faturamento,São Paulo
categoria_maior_faturamento,Manutenção
primeira_data_finalizada,2026-01-05
ultima_data_finalizada,2026-01-22
```

O arquivo `relatorio_clientes.csv` deve conter:

```csv
id_cliente,nome_cliente,cidade,faturamento_total,qtd_ordens,ticket_medio
```

O arquivo `relatorio_categorias.csv` deve conter:

```csv
categoria,faturamento_total,qtd_ordens,ticket_medio,participacao_percentual
```

O arquivo `relatorio_cidades.csv` deve conter:

```csv
cidade,faturamento_total,qtd_ordens,ticket_medio,participacao_percentual
```

Os valores de exemplo servem como referência de estrutura. Valide os resultados com base nos dados do CSV.

---

## Dica Técnica

Para evitar repetição excessiva, você pode criar os relatórios usando `groupby().agg()`.

Exemplo:

```python
relatorio_categorias = (
    df
    .groupby('categoria')
    .agg(
        faturamento_total=('valor', 'sum'),
        qtd_ordens=('id_os', 'count'),
        ticket_medio=('valor', 'mean')
    )
    .reset_index()
)
```

Depois você pode criar a coluna de participação percentual:

```python
relatorio_categorias['participacao_percentual'] = (
    relatorio_categorias['faturamento_total']
    / faturamento_total
    * 100
).round(2)
```

---

## Entregáveis

Ao finalizar o desafio, entregue o arquivo `analise.py` e os quatro arquivos CSV exportados na pasta `output`.

O README do desafio deve estar na pasta do projeto.

---

## Tecnologias Utilizadas

Python e pandas.

---

## Competências Treinadas

Neste desafio serão treinadas as seguintes competências:

Leitura de múltiplos arquivos CSV.

Relacionamento entre três tabelas.

Uso de `merge`.

Uso de `groupby().agg()`.

Criação de relatórios detalhados.

Criação de resumo executivo.

Conversão de datas.

Cálculo de indicadores principais.

Cálculo de ticket médio.

Cálculo de participação percentual.

Ordenação de relatórios.

Exportação de múltiplos arquivos.

Comunicação de indicadores para gestão.

Pensamento analítico orientado a negócio.

---

## O Que Era Esperado

Era esperado que o analista conseguisse transformar bases relacionais em relatórios detalhados e em uma visão executiva resumida.

A solução deve demonstrar capacidade de consolidar dados, automatizar relatórios e comunicar os principais indicadores de negócio.

O foco deste desafio é aproximar o trabalho técnico da entrega gerencial, conectando manipulação de dados com tomada de decisão.
