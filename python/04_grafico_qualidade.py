
from pathlib import Path
import matplotlib.pyplot as plt

projeto = Path(__file__).resolve().parent.parent
saida = projeto / "graficos"
saida.mkdir(exist_ok=True)

campos = ["Data de alta", "Custo", "SLA de aceite"]
percentuais = [12.31, 5.01, 3.05]

fig, ax = plt.subplots(figsize=(10, 5))
barras = ax.barh(campos, percentuais, color="#176B9A")
ax.invert_yaxis()
ax.set_xlim(0, 15)
ax.set_xlabel("Percentual de registros (%)")
ax.set_title("ISA Saúde | Qualidade dos Dados",
             fontsize=16, fontweight="bold")

for barra, valor in zip(barras, percentuais):
    ax.text(valor + 0.2,
            barra.get_y() + barra.get_height()/2,
            f"{valor:.2f}%".replace(".", ","),
            va="center")

plt.tight_layout()
plt.savefig(saida / "qualidade_dados.png", dpi=300)
plt.show()
