
from pathlib import Path
import pandas as pd

# Localização dos arquivos
projeto = Path(__file__).resolve().parent.parent
arquivo = projeto / "data" / "raw" / "ISA Case Base de dados.xlsx"
saida = projeto / "data" / "processed"
saida.mkdir(parents=True, exist_ok=True)

# Importação
df = pd.read_excel(arquivo, sheet_name="Base_Pacientes")

print("\n=== ANÁLISE FINANCEIRA ISA SAÚDE ===")
print(f"Registros originais: {len(df)}")

# Identificar e retirar duplicações exatas
duplicados = df.duplicated().sum()
df = df.drop_duplicates().copy()

print(f"Duplicações exatas removidas: {duplicados}")
print(f"Registros para análise: {len(df)}")

# Converter campos financeiros
campos = [
    "Receita Bruta (R$)",
    "Glosa (R$)",
    "Custo (R$)"
]

for campo in campos:
    df[campo] = pd.to_numeric(df[campo], errors="coerce")

# Receita líquida após glosas
df["Receita Líquida"] = (
    df["Receita Bruta (R$)"] - df["Glosa (R$)"]
)

# Margem: somente quando o custo estiver disponível
df["Margem R$"] = (
    df["Receita Líquida"] - df["Custo (R$)"]
)

# Indicadores gerais
receita = df["Receita Bruta (R$)"].sum()
glosas = df["Glosa (R$)"].sum()
custos = df["Custo (R$)"].sum()

print("\n--- INDICADORES GERAIS ---")
print(f"Receita bruta: R$ {receita:,.2f}")
print(f"Glosas: R$ {glosas:,.2f}")
print(f"Custos conhecidos: R$ {custos:,.2f}")

if receita > 0:
    print(f"Taxa de glosa: {glosas / receita * 100:.2f}%")

# Consolidar por operadora
resumo = df.groupby("Operadora").agg(
    Registros=("ID Paciente", "size"),
    Pacientes=("ID Paciente", "nunique"),
    Receita=("Receita Bruta (R$)", "sum"),
    Glosas=("Glosa (R$)", "sum"),
    Custos=("Custo (R$)", "sum"),
    Custos_Ausentes=("Custo (R$)", lambda x: x.isna().sum())
).reset_index()

resumo["Receita_Liquida"] = resumo["Receita"] - resumo["Glosas"]

resumo["Margem_R$"] = (
    resumo["Receita_Liquida"] - resumo["Custos"]
)

# Evitar margens distorcidas por custos ausentes
resumo.loc[
    resumo["Custos_Ausentes"] > 0, "Margem_R$"
] = float("nan")

resumo["Taxa_Glosa_%"] = (
    resumo["Glosas"] / resumo["Receita"] * 100
).round(2)

resumo["Margem_%"] = (
    resumo["Margem_R$"] / resumo["Receita_Liquida"] * 100
).round(2)

resumo = resumo.sort_values("Receita", ascending=False)

print("\n--- RESULTADOS POR OPERADORA ---")
print(resumo.to_string(index=False))

# Exportação para Excel
resumo.to_excel(
    saida / "analise_financeira_operadoras.xlsx",
    index=False
)

print("\n=== ANÁLISE CONCLUÍDA ===")
print("Arquivo salvo em data/processed/")
