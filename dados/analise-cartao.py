#%%
import pandas as pd

# 1. Carregar os dados

df = pd.read_csv("D:/User/Desktop/case cartao credito/dados/dadoscartao.csv", sep=";")

# 2. Converter a coluna de data

df["dtTransacao"] = pd.to_datetime(df["dtTransacao"])

# 3. Calcular o valor de cada parcela

df["vlParcela"] = df["vlVenda"] / df["qtParcelas"]

# 4. Criar a lista com o número de parcelas
# Ex: se qtParcelas = 3 -> [0, 1, 2]

df["ordemParcela"] = df.apply(
    lambda row: list(range(row["qtParcelas"])),
    axis=1
)

# 5. Explodir as parcelas
# Cada parcela vira uma linha
df_explode = df.explode("ordemParcela")

# 6. Função para calcular a data da parcela
# Cada parcela soma N meses à data da compra

def calcDtParcela(row):
    return row["dtTransacao"] + pd.DateOffset(months=int(row["ordemParcela"]))

df_explode["dtParcela"] = df_explode.apply(calcDtParcela, axis=1)


# 7. Agrupar por cliente e por mês
# Soma o valor de todas as parcelas de cada cliente

df_result = (
    df_explode
        .groupby(["idCliente", "dtParcela"])["vlParcela"]
        .sum()
        .reset_index()
)

# 8. Mostrar o resultado final
print("\n===== RESULTADO FINAL =====\n")
print(df_result)




# %%
