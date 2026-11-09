
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

raiz = Path(__file__).resolve().parent.parent
arquivo = raiz / "data" / "processed" / "indicadores_operadoras.csv"
saida = raiz / "graficos"
saida.mkdir(exist_ok=True)

df = pd.read_csv(arquivo)
df = df.sort_values("Taxa Glosa (%)")

cores = [
    "#F5A65B" if taxa >= 15 else "#22D3C5"
    for taxa in df["Taxa Glosa (%)"]
]

fig, ax = plt.subplots(figsize=(12, 6.5))
fig.patch.set_facecolor("#0B1729")
ax.set_facecolor("#0B1729")

barras = ax.barh(
    df["Operadora Padronizada"],
    df["Taxa Glosa (%)"],
    color=cores,
    height=0.65
)

for barra in barras:
    valor = barra.get_width()
    ax.text(
        valor + 0.3,
        barra.get_y() + barra.get_height()/2,
        f"{valor:.2f}%".replace(".", ","),
        va="center", color="white", fontsize=11
    )

ax.set_title(
    "ISA SAÚDE | TAXA DE GLOSA POR OPERADORA",
    color="white", fontsize=17, fontweight="bold", pad=25
)

ax.set_xlabel("Taxa de glosa (%)", color="white")
ax.tick_params(colors="white")
ax.set_xlim(0, 24)

for lado in ax.spines.values():
    lado.set_visible(False)

ax.grid(axis="x", alpha=0.12)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig(
    saida / "taxa_glosa_operadoras.png",
    dpi=300,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)
plt.show()

print("Gráfico gerado com sucesso!")
