#--------------------------------------------------
# IMPORTAÇÃO DE BIBLIOTECAS

import pandas as pd


#--------------------------------------------------
# LEITURA DOS ARQUIVOS CSV

clientes = pd.read_csv('../data/clientes.csv')

ordens = pd.read_csv('../data/ordens_servico.csv')


#--------------------------------------------------
# UNIÃO DAS TABELAS

df = clientes.merge(
    ordens,
    how='right',
    on='id_cliente'
)


#--------------------------------------------------
# FILTRANDO ORDENS FINALIZADAS

df = df[df['status'] == 'Finalizado']


#--------------------------------------------------
# FATURAMENTO TOTAL

faturamento_total = df['valor'].sum()


#--------------------------------------------------
# FATURAMENTO POR CLIENTE

faturamento_cliente = df.groupby('nome_cliente')['valor'].sum()


#--------------------------------------------------
# QUANTIDADE DE ORDENS POR CLIENTE

ordens_cliente = df.groupby('nome_cliente')['id_os'].count()


#--------------------------------------------------
# TICKET MÉDIO POR CLIENTE

media_cliente = df.groupby('nome_cliente')['valor'].mean().round(1)


#--------------------------------------------------
# FATURAMENTO POR CIDADE

faturamento_cidade = df.groupby('cidade')['valor'].sum()


#--------------------------------------------------
# CIDADE COM MAIOR FATURAMENTO

top_cidade = faturamento_cidade.idxmax()

maior_faturamento_cidade = faturamento_cidade.max()


#--------------------------------------------------
# CIDADE DE CADA CLIENTE

cidade_cliente = df.groupby('nome_cliente')['cidade'].first()


#--------------------------------------------------
# ID DE CADA CLIENTE

id_cliente = df.groupby('nome_cliente')['id_cliente'].first()


#--------------------------------------------------
# CRIAÇÃO DO RELATÓRIO

relatorio = pd.DataFrame({
    'id_cliente': id_cliente,
    'cidade': cidade_cliente,
    'faturamento_total': faturamento_cliente,
    'qtd_ordens': ordens_cliente,
    'ticket_medio': media_cliente
})

relatorio = (
    relatorio
    .reset_index()
    .sort_values('id_cliente')
)


#--------------------------------------------------
# EXPORTAÇÃO DO RELATÓRIO

relatorio.to_csv(
    '../output/relatorio.csv',
    index=False
)


#--------------------------------------------------
# MENSAGEM DE SUCESSO

print('Relatório exportado com sucesso 🚀')