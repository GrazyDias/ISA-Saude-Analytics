
from pathlib import Path
import pandas as pd
import unicodedata

# 1. LOCALIZAR OS ARQUIVOS
raiz = Path(__file__).resolve().parent.parent
origem = raiz / "data" / "raw" / "ISA Case Base de dados.xlsx"
saida = raiz / "data" / "processed"
saida.mkdir(parents=True, exist_ok=True)

# 2. CARREGAR A PLANILHA
df = pd.read_excel(origem, sheet_name="Base_Pacientes")
contratos = pd.read_excel(
    origem, sheet_name="Operadoras_Contratos"
)

print("=== TRATAMENTO DE DADOS - ISA SAÚDE ===")
print("Registros originais:", len(df))

# 3. IDENTIFICAR DUPLICAÇÕES EXATAS
duplicados = df.loc[df.duplicated(keep="first")].copy()
duplicados.to_csv(
    saida / "duplicados_auditoria.csv",
    index=False, encoding="utf-8-sig"
)

# Base analítica provisória
df = df.drop_duplicates().copy()
print("Duplicações exatas:", len(duplicados))
print("Registros após deduplicação:", len(df))

# 4. NORMALIZAR NOMES PARA COMPARAÇÃO
def normalizar(texto):
    if pd.isna(texto):
        return ""
    texto = str(texto).strip().upper()
    return "".join(
        c for c in unicodedata.normalize("NFKD", texto)
        if not unicodedata.combining(c)
    )

df["Operadora Original"] = df["Operadora"]
contratos["Chave"] = contratos["Operadora"].map(normalizar)

# Identificar nomes que podem representar
# a mesma operadora
mapa = {
    "VITALIS": "VITALIS SAUDE",
    "VITALIS SAUDE": "VITALIS SAUDE"
}

df["Chave"] = df["Operadora"].map(normalizar)
df["Chave"] = df["Chave"].replace(mapa)

# Cruzar com o cadastro contratual
cadastro = contratos.drop_duplicates(subset=["Chave"])
nomes = cadastro.set_index("Chave")["Operadora"]

df["Operadora Padronizada"] = df["Chave"].map(nomes)
df["Operadora Padronizada"] = (
    df["Operadora Padronizada"].fillna(df["Operadora"])
)

df["Contrato Encontrado"] = df["Chave"].isin(
    cadastro["Chave"]
)

# 5. AUDITORIA DOS CAMPOS
df["Custo Ausente"] = df["Custo (R$)"].isna()
df["SLA Ausente"] = df["SLA Aceite (dias)"].isna()
df["Data Alta Ausente"] = df["Data Alta"].isna()

# 6. INDICADORES FINANCEIROS
df["Receita Líquida (R$)"] = (
    df["Receita Bruta (R$)"] - df["Glosa (R$)"]
)

df["Margem (R$)"] = (
    df["Receita Líquida (R$)"] - df["Custo (R$)"]
)

df["Margem (%)"] = (
    df["Margem (R$)"] /
    df["Receita Líquida (R$)"].replace(0, float("nan"))
) * 100

# 7. RESUMO POR OPERADORA
resumo = df.groupby(
    "Operadora Padronizada", dropna=False
).agg(
    Registros=("ID Paciente", "size"),
    Receita=("Receita Bruta (R$)", "sum"),
    Glosas=("Glosa (R$)", "sum"),
    Custos_Conhecidos=("Custo (R$)", "sum"),
    Custos_Ausentes=("Custo Ausente", "sum")
).reset_index()

resumo["Taxa Glosa (%)"] = (
    resumo["Glosas"] /
    resumo["Receita"].replace(0, float("nan"))
) * 100

# Não calcular margem total com custos ausentes
resumo["Margem (R$)"] = (
    resumo["Receita"] -
    resumo["Glosas"] -
    resumo["Custos_Conhecidos"]
)
resumo.loc[
    resumo["Custos_Ausentes"] > 0, "Margem (R$)"
] = float("nan")

# 8. EXPORTAR RESULTADOS
df.to_csv(
    saida / "base_tratada.csv",
    index=False, encoding="utf-8-sig"
)

resumo.to_csv(
    saida / "indicadores_operadoras.csv",
    index=False, encoding="utf-8-sig"
)

# 9. EXIBIR RESULTADOS
print("\n=== RESULTADOS ===")
print("Registros tratados:", len(df))
print("Operadoras padronizadas:",
      df["Operadora Padronizada"].nunique())
print("Custos ausentes:", df["Custo Ausente"].sum())
print("Contratos não encontrados:",
      (~df["Contrato Encontrado"]).sum())

print("\nReceita bruta: R$",
      round(df["Receita Bruta (R$)"].sum(), 2))
print("Glosas: R$",
      round(df["Glosa (R$)"].sum(), 2))

print("\n=== TAXAS DE GLOSA POR OPERADORA ===")
print(
    resumo[
        ["Operadora Padronizada", "Registros",
         "Taxa Glosa (%)", "Custos_Ausentes"]
    ].to_string(index=False)
)

print("\nArquivos salvos em:", saida)
print("=== TRATAMENTO CONCLUÍDO ===")
