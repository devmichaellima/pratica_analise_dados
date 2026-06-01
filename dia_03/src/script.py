#--------------------------------------------------
# IMPORTAÇÃO DE BIBLIOTECAS

import pandas as pd


#--------------------------------------------------
# LEITURA DO ARQUIVO CSV

vendas_periodo = pd.read_csv(
    '../data/vendas_periodo.csv'
)


#--------------------------------------------------
# CONVERSÃO DA COLUNA DE DATA

vendas_periodo['data_os'] = pd.to_datetime(
    vendas_periodo['data_os']
)


#--------------------------------------------------
# FATURAMENTO TOTAL

faturamento_total = vendas_periodo['valor'].sum()


#--------------------------------------------------
# FATURAMENTO POR DIA

faturamento_dia = (
    vendas_periodo
    .groupby('data_os')['valor']
    .sum()
)


#--------------------------------------------------
# DIA COM MAIOR FATURAMENTO

melhor_dia = faturamento_dia.idxmax()

faturamento_melhor_dia = faturamento_dia.max()


#--------------------------------------------------
# DIA COM MENOR FATURAMENTO

pior_dia = faturamento_dia.idxmin()

faturamento_pior_dia = faturamento_dia.min()


#--------------------------------------------------
# FATURAMENTO MÉDIO POR DIA

media_dia = faturamento_dia.mean()


#--------------------------------------------------
# QUANTIDADE DE DIAS COM VENDAS REGISTRADAS

contagem_dias_registrado = faturamento_dia.count()


#--------------------------------------------------
# CRIAÇÃO DO RELATÓRIO FINAL

relatorio = pd.DataFrame({

    'metrica': [
        'total_faturado',
        'dia_maior_faturamento',
        'valor_dia_maior_faturamento',
        'dia_menor_faturamento',
        'valor_dia_menor_faturamento',
        'faturamento_medio_diario',
        'dias_com_vendas'
    ],

    'valor': [
        faturamento_total,
        melhor_dia,
        faturamento_melhor_dia,
        pior_dia,
        faturamento_pior_dia,
        media_dia,
        contagem_dias_registrado
    ]
})


#--------------------------------------------------
# EXPORTAÇÃO DO RELATÓRIO

relatorio.to_csv(
    '../output/relatorio.csv',
    index=False
)

print('Relatório exportado com sucesso!')