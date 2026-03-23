import pandas as pd
import matplotlib.pyplot as plt


# 1. Carregar dados
df = pd.read_csv("100_Sales_Records.csv")

# 2. Visualizar dados
print("Primeiras linhas:")
print(df.head())

# 3. Estatísticas básicas
print("\nResumo estatístico:")
print(df.describe())

# 4. Produto mais vendido
produto_mais_vendido = df.groupby("Item Type")["Units Sold"].sum().idxmax()
print(f"\nProduto mais vendido: {produto_mais_vendido}")

# 5. Receita total por produto
receita_por_produto = df.groupby("Item Type")["Total Revenue"].sum()
print("\nReceita por produto:")
print(receita_por_produto.sort_values(ascending=False))

# 6. País com maior faturamento
pais_top = df.groupby("Country")["Total Revenue"].sum().idxmax()
print(f"\nPaís com maior faturamento: {pais_top}")

# 7. Margem de lucro média
df["Profit Margin"] = df["Total Profit"] / df["Total Revenue"]
print(f"\nMargem média de lucro: {df['Profit Margin'].mean():.2f}")

# 8. Insight simples
print("\nInsight:")
print("Produtos com maior receita podem não ser os mais vendidos — observe preço vs volume.")

# 9. Visualização de dados
plt.figure(figsize=(10, 6))
df.groupby("Item Type")["Total Revenue"].sum().sort_values(ascending=False).plot(kind="bar")
plt.title("Receita por Produto", pad=20)
plt.xlabel("Produto")
plt.ylabel("Receita")
plt.xticks(rotation=45)

plt.tight_layout()
plt.subplots_adjust(top=0.9) 

plt.show(block = True)