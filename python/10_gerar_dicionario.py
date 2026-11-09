
from pathlib import Path
import pandas as pd

raiz = Path(__file__).resolve().parent.parent
arquivo = raiz / "data" / "processed" / "base_tratada.csv"

df = pd.read_csv(
    arquivo,
    sep=None,
    engine="python",
    encoding="utf-8-sig"
)

linhas = [
    "# Dicionário de Dados — ISA Saúde Analytics",
    "",
    "Base de dados fictícia para demonstração de competências técnicas.",
    "",
    f"**Registros:** {len(df)}",
    f"**Colunas:** {len(df.columns)}",
    "",
    "| Coluna | Tipo identificado | Valores ausentes | Descrição / regra de negócio |",
    "|---|---|---:|---|"
]

for coluna in df.columns:
    tipo = str(df[coluna].dtype)
    ausentes = int(df[coluna].isna().sum())
    nome = str(coluna).replace("|", r"\|")
    linhas.append(
        f"| {nome} | {tipo} | {ausentes} | A documentar |"
    )

saida = raiz / "DICIONARIO_DADOS.md"
saida.write_text("\n".join(linhas) + "\n", encoding="utf-8")

print(f"Dicionário criado: {saida}")
print(f"Total de colunas documentadas: {len(df.columns)}")
