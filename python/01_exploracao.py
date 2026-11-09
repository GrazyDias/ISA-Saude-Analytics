
from pathlib import Path
import pandas as pd

# Localizar o arquivo Excel
pasta_projeto = Path(__file__).resolve().parent.parent
arquivo = pasta_projeto / "data" / "raw" / "ISA Case Base de dados.xlsx"

# Abrir a planilha
excel = pd.ExcelFile(arquivo)

print("\n=== PROJETO ISA SAÚDE ===")
print("\nABAS ENCONTRADAS:")
print(excel.sheet_names)

# Explorar todas as abas
for aba in excel.sheet_names:
    df = pd.read_excel(arquivo, sheet_name=aba)

    print(f"\n=== ABA: {aba} ===")
    print(f"Quantidade de linhas: {len(df)}")
    print(f"Quantidade de colunas: {len(df.columns)}")

    print("\nNOMES DAS COLUNAS:")
    for coluna in df.columns:
        print("-", coluna)

    print("\nPRIMEIROS 5 REGISTROS:")
    print(df.head().to_string(index=False))

print("\n=== EXPLORAÇÃO CONCLUÍDA ===")

