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
    how='inner',
    on='id_cliente'
)


#--------------------------------------------------
# FILTRANDO ORDENS FINALIZADAS

df = df[df['status'] == 'Finalizado']


#--------------------------------------------------
# QUANTIDADE DE ORDENS COM CLIENTE VÁLIDO

ordens_cliente = df.groupby('nome_cliente')['id_os'].count()


#--------------------------------------------------
# ORDENS SEM CLIENTE CADASTRADO

os_ausente = clientes.merge(
    ordens,
    how='right',
    on='id_cliente'
)

os_ausente = os_ausente.fillna(
    'Ausente'
)

os_ausente = os_ausente[
    os_ausente['nome_cliente'] == 'Ausente'
]

ordens_sem_cliente = os_ausente.shape[0]


#--------------------------------------------------
# ORDENS COM ID_CLIENTE SEM CORRESPONDÊNCIA

os_cliente_ausente = os_ausente['id_os']


#--------------------------------------------------
# FATURAMENTO TOTAL VÁLIDO

faturamento_total = df['valor'].sum()


#--------------------------------------------------
# FATURAMENTO POR CLIENTE

faturamento_cliente = df.groupby('nome_cliente')['valor'].sum()


#--------------------------------------------------
# ID DO CLIENTE

id_cliente = df.groupby('nome_cliente')['id_cliente'].first()


#--------------------------------------------------
# CIDADE DO CLIENTE

cidade_cliente = df.groupby('nome_cliente')['cidade'].first()


#--------------------------------------------------
# QUANTIDADE DE ORDENS POR CLIENTE

qtd_ordens = df.groupby('nome_cliente')['id_os'].count()


#--------------------------------------------------
# TICKET MÉDIO POR CLIENTE

ticket_medio = df.groupby('nome_cliente')['valor'].mean().round(1)


#--------------------------------------------------
# CRIAÇÃO DO RELATÓRIO

relatorio = pd.DataFrame({
    'id_cliente': id_cliente,
    'cidade': cidade_cliente,
    'faturamento_total': faturamento_cliente,
    'qtd_ordens': qtd_ordens,
    'ticket_medio': ticket_medio
})

relatorio = relatorio.reset_index()

relatorio = relatorio.sort_values(
    'id_cliente'
)


#--------------------------------------------------
# EXPORTAÇÃO DO RELATÓRIO

relatorio.to_csv(
    '../output/relatorio.csv',
    index=False
)


#--------------------------------------------------
# EXPORTAÇÃO DAS ORDENS SEM CLIENTE

os_ausente.to_csv(
    '../output/ordens_sem_cliente.csv',
    index=False
)


#--------------------------------------------------
# MENSAGEM DE SUCESSO

print('Relatórios exportados com sucesso ')