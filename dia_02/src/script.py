#--------------------------------------------------
# IMPORTAÇÃO DE BIBLIOTECAS

import pandas as pd


#--------------------------------------------------
# LEITURA DO ARQUIVO CSV

ordens_servico_sujas = pd.read_csv(
    'dia_02/data/ordens_servico_sujas.csv'
)


#--------------------------------------------------
# LIMPEZA DA COLUNA STATUS

ordens_servico_sujas['status'] = (
    ordens_servico_sujas['status']
    .fillna('Pendente')
    .str.strip()
    .str.lower()
    .str.capitalize()
)


#--------------------------------------------------
# PREENCHIMENTO DE VALORES AUSENTES

ordens_servico_sujas['valor'] = (
    ordens_servico_sujas['valor']
    .fillna(0)
)


#--------------------------------------------------
# CONVERSÃO DE DATAS

ordens_servico_sujas['data_os'] = pd.to_datetime(
    ordens_servico_sujas['data_os']
)


#--------------------------------------------------
# CRIAÇÃO DA TABELA TRATADA

ordens_tratadas = ordens_servico_sujas.copy()


#--------------------------------------------------
# FILTRAR APENAS ORDENS FINALIZADAS

ordens_tratadas = ordens_tratadas[
    ordens_tratadas['status'] == 'Finalizado'
]


#--------------------------------------------------
# TOTAL FATURADO

total_faturado = ordens_tratadas['valor'].sum()


#--------------------------------------------------
# QUANTIDADE DE ORDENS FINALIZADAS

quantidade_os = ordens_tratadas.shape[0]


#--------------------------------------------------
# CLIENTE COM MAIOR FATURAMENTO

faturamento_cliente = (
    ordens_tratadas
    .groupby('cliente')['valor']
    .sum()
)

top_cliente = faturamento_cliente.idxmax()

top_faturamento_cliente = faturamento_cliente.max()


#--------------------------------------------------
# SERVIÇO COM MAIOR VALOR MÉDIO

media_servico = (
    ordens_tratadas
    .groupby('servico')['valor']
    .mean()
)

top_servico = media_servico.idxmax()

top_media_servico = media_servico.max()


#--------------------------------------------------
# PRIMEIRA E ÚLTIMA DATA DE FINALIZAÇÃO

primeira_data = ordens_tratadas['data_os'].min()

ultima_data = ordens_tratadas['data_os'].max()


#--------------------------------------------------
# CRIAÇÃO DO RELATÓRIO FINAL

relatorio = pd.DataFrame({

    'metrica': [
        'total_faturado',
        'qtd_os_finalizadas',
        'cliente_maior_faturamento',
        'valor_cliente_maior_faturamento',
        'servico_maior_media',
        'valor_servico_maior_media',
        'primeira_data_finalizada',
        'ultima_data_finalizada'
    ],

    'valor': [
        total_faturado,
        quantidade_os,
        top_cliente,
        top_faturamento_cliente,
        top_servico,
        top_media_servico,
        primeira_data,
        ultima_data
    ]
})


#--------------------------------------------------
# EXPORTAÇÃO DO RELATÓRIO

relatorio.to_csv(
    'dia_02/output/relatorio.csv',
    index=False
)

print('Relatório exportado com sucesso')