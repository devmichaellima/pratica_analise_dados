#--------------------------------------------------
# IMPORTAÇÃO DE BIBLIOTECAS

import pandas as pd


#--------------------------------------------------
# LEITURA DO ARQUIVO CSV

df = pd.read_csv(
    '../data/clientes_faturamento.csv'
)


#--------------------------------------------------
# FATURAMENTO TOTAL DA EMPRESA

faturamento_total = df['valor'].sum()


#--------------------------------------------------
# FATURAMENTO POR CLIENTE

faturamento_cliente = (
    df
    .groupby('cliente')['valor']
    .sum()
)


#--------------------------------------------------
# CLIENTE COM MAIOR FATURAMENTO

melhor_cliente = faturamento_cliente.idxmax()

maior_faturamento = faturamento_cliente.max()


#--------------------------------------------------
# FATURAMENTO MÉDIO POR CLIENTE

media_cliente = faturamento_cliente.mean()


#--------------------------------------------------
# TOP 3 CLIENTES COM MAIOR FATURAMENTO

top_clientes = (
    faturamento_cliente
    .sort_values(ascending=False)
    .head(3)
)


#--------------------------------------------------
# CRIAÇÃO DO RELATÓRIO FINAL

relatorio = pd.DataFrame({

    'metrica': [
        'faturamento_total',
        'cliente_maior_faturamento',
        'valor_maior_faturamento',
        'faturamento_medio_cliente'
    ],

    'valor': [
        faturamento_total,
        melhor_cliente,
        maior_faturamento,
        media_cliente
    ]
})


#--------------------------------------------------
# EXPORTAÇÃO DO RELATÓRIO

relatorio.to_csv(
    '../output/relatorio.csv',
    index=False
)


#--------------------------------------------------
# MENSAGEM DE SUCESSO

print('Relatório exportado com sucesso!')