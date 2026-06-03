#--------------------------------------------------
# IMPORTAÇÃO DE BIBLIOTECAS

import pandas as pd


#--------------------------------------------------
# LEITURA DO ARQUIVO CSV

df = pd.read_csv('../data/servicos_faturamento.csv')


#--------------------------------------------------
# FILTRANDO ORDENS FINALIZADAS

df = df[df['status'] == 'Finalizado']


#--------------------------------------------------
# FATURAMENTO TOTAL

faturamento_total = df['valor'].sum()


#--------------------------------------------------
# FATURAMENTO POR SERVIÇO

faturamento_servico = df.groupby('servico')['valor'].sum()


#--------------------------------------------------
# QUANTIDADE DE ORDENS FINALIZADAS POR SERVIÇO

ordens_finalizadas = df.groupby('servico')['id_os'].count()


#--------------------------------------------------
# TICKET MÉDIO POR SERVIÇO

media_servico = df.groupby('servico')['valor'].mean().round(1)


#--------------------------------------------------
# PARTICIPAÇÃO NO FATURAMENTO

porcem_faturamento = (
    faturamento_servico
    / faturamento_total
    * 100
).round(1)


#--------------------------------------------------
# SERVIÇO COM MAIOR FATURAMENTO

top_servico = faturamento_servico.idxmax()

maior_faturamento_servico = faturamento_servico.max()


#--------------------------------------------------
# SERVIÇO COM MAIOR TICKET MÉDIO

melhor_ticket_servico = media_servico.idxmax()

maior_media_servico = media_servico.max()


#--------------------------------------------------
# CRIAÇÃO DO RELATÓRIO

relatorio = pd.DataFrame({
    'faturamento_total': faturamento_servico,
    'qtd_ordens': ordens_finalizadas,
    'ticket_medio': media_servico,
    'participacao_percentual': porcem_faturamento
})

relatorio = relatorio.sort_values(
    by='faturamento_total',
    ascending=False
)


#--------------------------------------------------
# EXPORTAÇÃO DO RELATÓRIO

relatorio.to_csv(
    '../output/relatorio.csv'
)


#--------------------------------------------------
# MENSAGEM DE SUCESSO

print('Relatório exportado com sucesso')