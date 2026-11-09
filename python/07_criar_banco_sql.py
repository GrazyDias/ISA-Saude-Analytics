
from pathlib import Path
import pandas as pd
import sqlite3

raiz = Path(__file__).resolve().parent.parent

arquivo = raiz / "data" / "processed" / "base_tratada.csv"
banco = raiz / "data" / "isa_saude.db"

df = pd.read_csv(arquivo, encoding="utf-8-sig")

# Padronizar nomes das colunas para SQL
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

with sqlite3.connect(banco) as conexao:
    df.to_sql(
        "atendimentos",
        conexao,
        if_exists="replace",
        index=False
    )

    resultado = pd.read_sql_query(
        "SELECT COUNT(*) AS total FROM atendimentos",
        conexao
    )

print("=== BANCO SQL CRIADO ===")
print("Arquivo:", banco)
print("Tabela: atendimentos")
print(resultado.to_string(index=False))
