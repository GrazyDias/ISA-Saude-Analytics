
from pathlib import Path
import pandas as pd

# Caminhos do projeto
projeto = Path(__file__).resolve().parent.parent
arquivo = projeto / "data" / "raw" / "ISA Case Base de dados.xlsx"
saida = projeto / "data" / "processed"
saida.mkdir(parents=True, exist_ok=True)

# Importar a base
df = pd.read_excel(arquivo, sheet_name="Base_Pacientes")

print("\n=== AUDITORIA DE QUALIDADE - ISA SAÚDE ===")

print(f"\nTotal de registros: {len(df)}")
print(f"Total de colunas: {len(df.columns)}")

# Verificar valores ausentes
nulos = df.isna().sum().sort_values(ascending=False)
print("\nVALORES AUSENTES:")
print(nulos[nulos > 0].to_string())

# Verificar linhas completamente duplicadas
duplicados = df.duplicated().sum()
print(f"\nLinhas totalmente duplicadas: {duplicados}")

# Verificar identificadores repetidos
if "id_paciente" in df.columns:
    ids_repetidos = df["id_paciente"].duplicated(keep=False)
    print(f"Registros com ID repetido: {ids_repetidos.sum()}")

# Verificar tipos de dados
print("\nTIPOS DE DADOS:")
print(df.dtypes.to_string())

# Verificar valores numéricos negativos
colunas_numericas = df.select_dtypes(include="number").columns

print("\nVALORES NEGATIVOS:")
for coluna in colunas_numericas:
    quantidade = (df[coluna] < 0).sum()
    if quantidade > 0:
        print(f"{coluna}: {quantidade}")

# Gerar relatório
relatorio = pd.DataFrame({
    "coluna": df.columns,
    "tipo_dado": df.dtypes.astype(str).values,
    "valores_nulos": df.isna().sum().values,
    "percentual_nulos": (
        df.isna().mean().values * 100
    ).round(2)
})

relatorio.to_excel(
    saida / "relatorio_qualidade.xlsx",
    index=False
)

print("\nRelatório salvo em data/processed/")
print("\n=== AUDITORIA CONCLUÍDA ===")

