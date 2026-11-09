
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent

arquivo = raiz / "data" / "processed" / "analise_financeira_sql.xlsx"
df = pd.read_excel(arquivo)

df = df.sort_values("glosas", ascending=True)

fig, ax = plt.subplots(figsize=(12, 6))

y = range(len(df))

ax.barh(
    y,
    df["receita_bruta"] / 1_000_000,
    height=0.65,
    label="Receita bruta"
)

ax.barh(
    y,
    df["glosas"] / 1_000_000,
    height=0.35,
    label="Glosas"
)

ax.set_yticks(list(y))
ax.set_yticklabels(df["operadora"])

ax.set_xlabel("Valores em R$ milhões")
ax.set_title(
    "ISA Saúde | Receita e Glosas por Operadora",
    fontsize=15,
    fontweight="bold"
)

ax.legend()
ax.grid(axis="x", alpha=0.2)

plt.tight_layout()

saida = raiz / "graficos" / "impacto_financeiro.png"
plt.savefig(saida, dpi=300, bbox_inches="tight")

print("Gráfico gerado com sucesso!")
print(saida)

plt.show()
