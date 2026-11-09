
from pathlib import Path
import pandas as pd
import sys

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO = RAIZ / "data" / "processed" / "base_tratada.csv"

def validar():
    if not ARQUIVO.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {ARQUIVO}")

    df = pd.read_csv(
        ARQUIVO,
        sep=None,
        engine="python",
        encoding="utf-8-sig"
    )

    print("\nVALIDAÇÃO DO PROJETO ISA SAÚDE")
    print("=" * 45)

    erros = []

    if df.empty:
        erros.append("A base está vazia.")

    if len(df) != 910:
        print(f"AVISO: quantidade atual de registros: {len(df)}")

    if len(df.columns) != 27:
        print(f"AVISO: quantidade atual de colunas: {len(df.columns)}")

    if df.columns.duplicated().any():
        erros.append("Existem nomes de colunas duplicados.")

    for coluna in ["ID Paciente", "Modalidade", "Operadora"]:
        if coluna not in df.columns:
            erros.append(f"Coluna obrigatória ausente: {coluna}")

    if "Custo (R$)" in df.columns:
        custo = pd.to_numeric(df["Custo (R$)"], errors="coerce")
        print(f"Custos ausentes ou inválidos: {custo.isna().sum()}")

    if {"Receita Líquida (R$)", "Margem (R$)", "Custo (R$)"}.issubset(df.columns):
        receita = pd.to_numeric(df["Receita Líquida (R$)"], errors="coerce")
        margem = pd.to_numeric(df["Margem (R$)"], errors="coerce")
        custo = pd.to_numeric(df["Custo (R$)"], errors="coerce")

        validos = receita.notna() & margem.notna() & custo.notna()

        inconsistentes = (
            (receita[validos] - custo[validos] - margem[validos])
            .abs() > 0.02
        ).sum()

        print(f"Inconsistências na margem: {inconsistentes}")

        if inconsistentes:
            erros.append("Há divergências no cálculo da margem.")

    print(f"Registros analisados: {len(df)}")
    print(f"Colunas identificadas: {len(df.columns)}")

    if erros:
        for erro in erros:
            print(f"ERRO: {erro}")
        return 1

    print("\nValidações executadas sem erros críticos.")
    return 0

if __name__ == "__main__":
    sys.exit(validar())
