#--------------------------------------------------
# IMPORTAÇÃO DE BIBLIOTECAS

import pandas as pd


#--------------------------------------------------
# LEITURA DO ARQUIVO CSV

df = pd.read_csv('../data/clientes_faturamento.csv')


#--------------------------------------------------
# FATURAMENTO TOTAL DA EMPRESA

faturamento_total = df['valor'].sum()


#--------------------------------------------------
# FATURAMENTO POR CLIENTE

faturamento_cliente = df.groupby('cliente')['valor'].sum()


#--------------------------------------------------
# QUANTIDADE DE ORDENS POR CLIENTE

ordens_cliente = df.groupby('cliente')['valor'].count()


#--------------------------------------------------
# PARTICIPAÇÃO PERCENTUAL POR CLIENTE

porcentagem_cliente = []

for cliente, valor in faturamento_cliente.items():

    dados_cliente = {
        'cliente': cliente,
        '%_faturamento': valor / faturamento_total * 100
    }

    porcentagem_cliente.append(dados_cliente)

porcentagem_cliente = pd.DataFrame(porcentagem_cliente)

porcentagem_cliente = porcentagem_cliente.sort_values('%_faturamento')

porcentagem_cliente['%_faturamento'] = porcentagem_cliente['%_faturamento'].round(1)


#--------------------------------------------------
# EXPORTAÇÃO DA PARTICIPAÇÃO POR CLIENTE

porcentagem_cliente.to_csv(
    '../output/porcentagem_cliente.csv',
    index=False
)


#--------------------------------------------------
# CLIENTE COM MAIOR PARTICIPAÇÃO

melhor_cliente = faturamento_cliente.idxmax()


#--------------------------------------------------
# CRIAÇÃO DO RELATÓRIO

relatorio = pd.DataFrame({
    'faturamento_total': faturamento_cliente,
    'qtd_ordens': ordens_cliente,
    'participacao_percentual': faturamento_cliente / faturamento_total * 100
})

relatorio['participacao_percentual'] = relatorio['participacao_percentual'].round(1)

relatorio = relatorio.sort_values(
    by='participacao_percentual',
    ascending=False
)


#--------------------------------------------------
# EXPORTAÇÃO DO RELATÓRIO

relatorio.to_csv('../output/relatorio_clientes.csv')
