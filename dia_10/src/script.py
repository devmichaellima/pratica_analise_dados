# LEITURA DOS ARQUIVOS CSV

import pandas as pd

clientes = pd.read_csv('../data/clientes.csv')

ordens_servico = pd.read_csv('../data/ordens_servico.csv')  # tabela fato

servicos = pd.read_csv('../data/servicos.csv')


# UNIÃO DAS TABELAS

df = ordens_servico.merge(
    clientes,
    how='left',
    on='id_cliente'
)

df = df.merge(
    servicos,
    how='left',
    on='id_servico'
)


# FILTRANDO ORDENS FINALIZADAS

df = df[df['status'] == 'Finalizado']


# ORDENANDO COLUNAS

df = df[
    [
        'id_os',
        'id_cliente',
        'id_servico',
        'nome_cliente',
        'cidade',
        'categoria',
        'nome_servico',
        'valor',
        'data_os',
        'status'
    ]
]



# FATURAMENTO TOTAL

faturamento_total = df['valor'].sum()



# QUANTIDADE DE ORDENS FINALIZADAS

ordens_finalizadas = df['id_os'].count()



# TICKET MÉDIO GERAL

ticket_medio = df['valor'].mean()



# CLIENTE COM MAIOR FATURAMENTO

top_cliente = df.groupby(
    'nome_cliente'
)['valor'].sum().idxmax()



# CIDADE COM MAIOR FATURAMENTO

top_cidade = df.groupby(
    'cidade'
)['valor'].sum().idxmax()



# CATEGORIA COM MAIOR FATURAMENTO

top_categoria = df.groupby(
    'categoria'
)['valor'].sum().idxmax()



# PRIMEIRA DATA DE VENDA FINALIZADA

df['data_os'] = pd.to_datetime(
    df['data_os']
)

primeira_data = df.groupby(
    'data_os'
)['data_os'].first().idxmin()



# ÚLTIMA DATA DE VENDA FINALIZADA

ultima_data = df.groupby(
    'data_os'
)['data_os'].first().idxmax()



# RELATÓRIO DE CLIENTES

relatorio_clientes = (
    df.groupby('nome_cliente')
    .agg(
        id_cliente=('id_cliente', 'first'),
        cidade=('cidade', 'first'),
        faturamento_total=('valor', 'sum'),
        qtd_ordens=('id_os', 'count'),
        ticket_medio=('valor', 'mean')
    )
    .reset_index()
    .sort_values(
        'faturamento_total',
        ascending=False
    )
)



# RELATÓRIO DE CATEGORIAS

relatorio_categorias = df.groupby(
    'categoria'
).agg(
    faturamento_total=('valor', 'sum'),
    qtd_ordens=('id_os', 'count'),
    ticket_medio=('valor', lambda x: x.mean().round(2))
)

relatorio_categorias['participacao_percentual'] = (
    (
        (
            df.groupby('categoria')['valor'].sum()
        )
        / faturamento_total
    ) * 100
).round(2)

relatorio_categorias = (
    relatorio_categorias
    .reset_index()
    .sort_values(
        'faturamento_total',
        ascending=False
    )
)



# RELATÓRIO DE CIDADES

relatorio_cidades = df.groupby(
    'cidade'
).agg(
    faturamento_total=('valor', 'sum'),
    qtd_ordens=('id_os', 'count'),
    ticket_medio=('valor', lambda x: x.mean().round(2))
)

relatorio_cidades['participacao_percentual'] = (
    (
        (
            df.groupby('cidade')['valor'].sum()
        )
        / faturamento_total
    ) * 100
).round(2)

relatorio_cidades = (
    relatorio_cidades
    .reset_index()
    .sort_values(
        'faturamento_total',
        ascending=False
    )
)



# RESUMO EXECUTIVO

resumo_executivo = pd.DataFrame({
    'metrica': [
        'faturamento_total',
        'qtd_ordens_finalizadas',
        'ticket_medio_geral',
        'cliente_maior_faturamento',
        'cidade_maior_faturamento',
        'categoria_maior_faturamento',
        'primeira_data_finalizada',
        'ultima_data_finalizada'
    ],
    'valor': [
        faturamento_total,
        ordens_finalizadas,
        ticket_medio,
        top_cliente,
        top_cidade,
        top_categoria,
        primeira_data,
        ultima_data
    ]
})


# EXPORTAÇÃO DOS RELATÓRIOS

resumo_executivo.to_csv(
    '../output/resumo_executivo.csv',
    index=False,
    date_format='%d/%m/%Y'
)

relatorio_clientes.to_csv(
    '../output/relatorio_clientes.csv',
    index=False,
    date_format='%d/%m/%Y'
)

relatorio_categorias.to_csv(
    '../output/relatorio_categorias.csv',
    index=False,
    date_format='%d/%m/%Y'
)

relatorio_cidades.to_csv(
    '../output/relatorio_cidades.csv',
    index=False,
    date_format='%d/%m/%Y'
)