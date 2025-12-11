#%%
import pandas as pd

df = pd.read_csv(r"D:\User\Desktop\pandas\case-cartao-credito\dadoscartao.csv", sep=';')
df
# %%
df['dtTransacao'] = pd.to_datetime(df['dtTransacao'])
df

#%%
df['vlParcela'] = df['vlVenda'] / df['qtParcelas']
df

#%%
df['ordemParcela'] = df.apply(lambda row: [i for i in range(row['qtParcelas'])], axis=1)
df

#%%
df_explode = df.explode('ordemParcela')
df_explode                                                      

# %%
def calcDtParcela(row):
    # Data da transação
    dt = row["dtTransacao"]

    # Número da parcela (ex.: 1, 2, 3...)
    n = int(row["ordemParcela"])

    # Soma de meses
    dt = dt + pd.DateOffset(months=n)

    return dt

# Aplica a função
df_explode["dtParcela"] = df_explode.apply(calcDtParcela, axis=1)
df_explode

#%%
df_result = (
    df_explode
        .groupby(['idCliente', 'dtParcela'])['vlParcela']
        .sum()
        .reset_index()
)
df_result

# %%
