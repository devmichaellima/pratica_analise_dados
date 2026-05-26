#------------------------------------------------------------------------------------------------------------
#lendo o arquivo csv e armazenando em um dataframe

import pandas as pd 

df = pd.read_csv('dia_01/data/ordens_servico.csv')

#------------------------------------------------------------------------------------------------------------
#filtrar a tabela para mostrar apenas ordens com status 'Finalizado'

df_finalizado = df[df['status'] == 'Finalizado']

#------------------------------------------------------------------------------------------------------------
#faturamento total

total_faturado = df_finalizado['valor'].sum()

print(f'O valor total faturado é de R${total_faturado:.2f}')

#------------------------------------------------------------------------------------------------------------
#quantidade de OS finalizadas

total_ordens = df_finalizado.shape[0]
print(f'Foram registrados {total_ordens} pedidos finalizados')

#------------------------------------------------------------------------------------------------------------
#cliente com maior faturamento

#agrupar OS por cliente
faturamento_cliente = df_finalizado.groupby('cliente')['valor'].sum()

#rankear clientes
cliente_maior_faturamento = faturamento_cliente.idxmax()
maior_faturamento = faturamento_cliente.max()

print(f'O cliente {cliente_maior_faturamento} foi o que mais gerou faturamento: R${maior_faturamento:.2f}')

#------------------------------------------------------------------------------------------------------------
#serviço com maior valor medio

#agrupar por servico e tirar media
media_servico = df_finalizado.groupby('servico')['valor'].mean()

#rankear maior servico
servico_maior_media = media_servico.idxmax()
maior_media = media_servico.max()

print(f'{servico_maior_media} apresentou a melhor media de faturamento: R${maior_media:.2f}')

#------------------------------------------------------------------------------------------------------------
#gerar relatorio

relatorio = pd.DataFrame({
    'metrica': [
        'total_faturado',
        'total_ordens',
        'cliente_maior_faturamento',
        'maior_faturamento',
        'servico_maior_media',
        'maior_media'
    ],
    'valor': [
        total_faturado,
        total_ordens,
        cliente_maior_faturamento,
        maior_faturamento,
        servico_maior_media,
        maior_media
    ]}
)

#------------------------------------------------------------------------------------------------------------
#exportando relatorio

relatorio.to_csv('dia_01/output/relatorio.csv', index=False)
print('Relatório gerado com sucesso!')

