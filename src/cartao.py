#%%
import pandas as pd

# 1. Carrega o arquivo CSV
df = pd.read_csv(
    r"D:\User\Desktop\case-cartao-credito\dados\dadoscartao.csv",
    sep=';'
)
# 2. Converte a data da transação
df['dtTransacao'] = pd.to_datetime(df['dtTransacao'])

# 3. Calcula o valor de cada parcela
df['vlParcela'] = df['vlVenda'] / df['qtParcelas']

# 4. Cria a lista de parcelas (0, 1, 2, ...)
df['ordemParcela'] = df.apply(
    lambda row: list(range(row['qtParcelas'])),
    axis=1
)

# 5. Explode para gerar uma linha por parcela
df_explode = df.explode('ordemParcela')

# 6. Função para calcular a data de cada parcela
def calcDtParcela(row):
    dt = row['dtTransacao']
    n = int(row['ordemParcela'])
    return dt + pd.DateOffset(months=n)

# 7. Aplica a função e cria a nova coluna dtParcela
df_explode['dtParcela'] = df_explode.apply(calcDtParcela, axis=1)

# 8. Agrupa por cliente e data da parcela
df_result = (
    df_explode
        .groupby(['idCliente', 'dtParcela'])['vlParcela']
        .sum()
        .reset_index()
)

df_result
# %%
