#--------------------------------------------------
# IMPORTAÇÃO DE BIBLIOTECAS

import pandas as pd


#--------------------------------------------------
# LEITURA DOS ARQUIVOS CSV

clientes = pd.read_csv('../data/clientes.csv')

ordens = pd.read_csv('../data/ordens_servico.csv')

servicos = pd.read_csv('../data/servicos.csv')


#--------------------------------------------------
# UNIÃO DAS TABELAS

df = ordens.merge(clientes, how='left', on='id_cliente')

df = df.merge(servicos, how='left', on='id_servico')


#--------------------------------------------------
# ORDENAÇÃO DAS COLUNAS

df = df[
    [
        'id_cliente',
        'nome_cliente',
        'cidade',
        'id_os',
        'id_servico',
        'categoria',
        'nome_servico',
        'valor',
        'data_os',
        'status'
    ]
]


#--------------------------------------------------
# FILTRANDO ORDENS FINALIZADAS

df = df[df['status'] == 'Finalizado']


#--------------------------------------------------
# FATURAMENTO TOTAL

faturamento_total = df['valor'].sum()


#--------------------------------------------------
# FATURAMENTO POR CLIENTE

faturamento_cliente = df.groupby('id_cliente')['valor'].sum()


#--------------------------------------------------
# FATURAMENTO POR CIDADE

faturamento_cidade = df.groupby('cidade')['valor'].sum()


#--------------------------------------------------
# FATURAMENTO POR CATEGORIA

faturamento_categoria = df.groupby('categoria')['valor'].sum()


#--------------------------------------------------
# CATEGORIA COM MAIOR FATURAMENTO

melhor_categoria = faturamento_categoria.idxmax()

maior_faturamento_categoria = faturamento_categoria.max()


#--------------------------------------------------
# TICKET MÉDIO POR CATEGORIA

media_categoria = df.groupby('categoria')['valor'].mean().round(1)


#--------------------------------------------------
# QUANTIDADE DE ORDENS POR CATEGORIA

os_categoria = df.groupby('categoria')['id_os'].count()


#--------------------------------------------------
# RELATÓRIO DE CLIENTES

relatorio_clientes = pd.DataFrame({
    'id_cliente': faturamento_cliente.index,
    'nome_cliente': df.groupby('id_cliente')['nome_cliente'].first(),
    'cidade': df.groupby('id_cliente')['cidade'].first(),
    'faturamento_total': faturamento_cliente,
    'qtd_ordens': df.groupby('id_cliente')['id_os'].count(),
    'ticket_medio': df.groupby('id_cliente')['valor'].mean().round(1)
})

relatorio_clientes.to_csv('../output/relatorio_clientes.csv', index=False)


#--------------------------------------------------
# RELATÓRIO DE CATEGORIAS

relatorio_categorias = pd.DataFrame({
    'categoria': faturamento_categoria.index,
    'faturamento_total': faturamento_categoria,
    'qtd_ordens': os_categoria,
    'ticket_medio': media_categoria,
    'participacao_percentual': (faturamento_categoria / faturamento_total * 100).round(1)
})

relatorio_categorias.to_csv('../output/relatorio_categorias.csv', index=False)


#--------------------------------------------------
# RELATÓRIO DE CIDADES

relatorio_cidades = pd.DataFrame({
    'cidade': faturamento_cidade.index,
    'faturamento_total': faturamento_cidade,
    'qtd_ordens': df.groupby('cidade')['id_os'].count(),
    'ticket_medio': df.groupby('cidade')['valor'].mean().round(1),
    'participacao_percentual': (faturamento_cidade / faturamento_total * 100).round(1)
})

relatorio_cidades.to_csv('../output/relatorio_cidades.csv', index=False)


#--------------------------------------------------
# MENSAGEM DE SUCESSO

print('Relatórios exportados com sucesso')