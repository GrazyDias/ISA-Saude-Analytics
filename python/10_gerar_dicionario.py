
from pathlib import Path
import pandas as pd

# ============================================================
# 1. CONFIGURACAO DOS CAMINHOS
# ============================================================

raiz = Path(__file__).resolve().parent.parent
arquivo = raiz / "data" / "processed" / "base_tratada.csv"
saida = raiz / "DICIONARIO_DADOS.md"

if not arquivo.exists():
    raise FileNotFoundError(
        f"Base de dados nao encontrada: {arquivo}"
    )

# ============================================================
# 2. LEITURA DA BASE TRATADA
# ============================================================

df = pd.read_csv(
    arquivo,
    sep=None,
    engine="python",
    encoding="utf-8-sig"
)

# ============================================================
# 3. DICIONARIO DE DESCRICOES E REGRAS DE NEGOCIO
# ============================================================

descricoes = {
    "ID Paciente":
        "Identificador do paciente ou registro na base fictícia.",

    "Operadora":
        "Operadora de saúde vinculada ao atendimento.",

    "Modalidade":
        "Tipo de assistência: Internação Domiciliar (ID), Assistência Domiciliar (AD) ou Atendimento por Visitas.",

    "Patologia Principal":
        "Condição clínica principal associada ao atendimento.",

    "Região":
        "Região geográfica de referência do atendimento.",

    "CFS":
        "Campo numérico CFS. Definição operacional a validar.",

    "Data Implantação":
        "Data de implantação ou início do atendimento.",

    "Data Alta":
        "Data de encerramento do atendimento, quando registrada.",

    "Status":
        "Situação do atendimento conforme classificação da base.",

    "Dias Atendimento":
        "Quantidade de dias de atendimento registrada.",

    "OPME (R$)":
        "Valor registrado de órteses, próteses e materiais especiais.",

    "Receita Bruta (R$)":
        "Receita bruta registrada antes das deduções aplicáveis.",

    "Glosa (R$)":
        "Valor de glosa registrado no atendimento.",

    "Custo (R$)":
        "Custo registrado do atendimento. Valores ausentes não devem ser automaticamente substituídos por zero.",

    "Reinternação":
        "Indicador de reinternação conforme classificação da base.",

    "SLA Aceite (dias)":
        "Prazo registrado para aceite, em dias.",

    "Operadora Original":
        "Nome da operadora antes da padronização.",

    "Chave":
        "Campo auxiliar utilizado na integração ou padronização. Regra exata a validar.",

    "Operadora Padronizada":
        "Nome da operadora após tratamento e padronização.",

    "Contrato Encontrado":
        "Indicador de correspondência contratual encontrada na integração.",

    "Custo Ausente":
        "Indicador de ausência do valor de custo no registro.",

    "SLA Ausente":
        "Indicador de ausência do prazo de aceite.",

    "Data Alta Ausente":
        "Indicador de ausência da data de alta.",

    "Receita Líquida (R$)":
        "Receita após deduções. Fórmula exata a validar no processamento.",

    "Margem (R$)":
        "Resultado financeiro do atendimento. Fórmula exata a validar no processamento.",
        
"Diária (R$)": (
    "Valor monetário da diária de atendimento registrado na base. "
    "A unidade, a composição e a regra de cobrança devem ser validadas."
),


    "Margem (%)":
        "Margem financeira percentual. Fórmula e tratamento de receita zero a validar."
}

# ============================================================
# 4. CONSTRUCAO DO DICIONARIO EM MARKDOWN
# ============================================================

linhas = [
    "# Dicionário de Dados — ISA Saúde Analytics",
    "",
    "Base de dados fictícia para demonstração de competências técnicas.",
    "",
    f"**Registros:** {len(df)}",
    f"**Colunas:** {len(df.columns)}",
    "",
    "## Estrutura e descrição das variáveis",
    "",
    "| Coluna | Tipo identificado | Valores ausentes | Descrição / regra de negócio |",
    "|---|---|---:|---|"
]

for coluna in df.columns:
    tipo = str(df[coluna].dtype)
    ausentes = int(df[coluna].isna().sum())

    nome = str(coluna).replace("|", r"\|")

    descricao = descricoes.get(
        coluna,
        "Definição a validar"
    )

    descricao = descricao.replace("|", r"\|")

    linhas.append(
        f"| {nome} | {tipo} | {ausentes} | {descricao} |"
    )

# ============================================================
# 5. DOCUMENTACAO METODOLOGICA
# ============================================================

linhas.extend([
    "",
    "## Regras de qualidade e interpretação",
    "",
    "- Os dados utilizados neste projeto são fictícios.",
    "- Valores ausentes são identificados e contabilizados automaticamente.",
    "- Custos ausentes não devem ser interpretados como custo zero.",
    "- Indicadores financeiros que dependem do custo devem utilizar registros com custo conhecido, conforme a metodologia do dashboard.",
    "- A margem percentual agregada deve ser calculada a partir dos totais financeiros, e não pela soma ou média simples das margens percentuais.",
    "- As regras exatas de cálculo dos campos financeiros devem ser conferidas nos scripts de tratamento e análise.",
    "",
    "## Simulação de cenários",
    "",
    "O dashboard apresenta cenários hipotéticos de sensibilidade financeira:",
    "",
    "- **Base:** receita e custo sem alterações.",
    "- **Otimista:** receita multiplicada por 1,05 e custo por 0,95.",
    "- **Pressão:** receita multiplicada por 0,95 e custo por 1,10.",
    "",
    "Os cenários são simulações hipotéticas e não previsões estatísticas.",
    "",
    "## Tecnologias",
    "",
    "Python, Pandas, SQL, PySpark, Databricks, Power BI e GitHub.",
    "",
    "## Observação",
    "",
    "As descrições são preliminares e devem ser validadas contra as regras de negócio e os scripts de processamento."
])

# ============================================================
# 6. GRAVACAO DO ARQUIVO
# ============================================================

saida.write_text(
    "\n".join(linhas) + "\n",
    encoding="utf-8"
)

# ============================================================
# 7. VALIDACAO E RESULTADOS
# ============================================================

print("=" * 60)
print("DICIONARIO DE DADOS - ISA SAUDE ANALYTICS")
print("=" * 60)

print(f"Arquivo criado: {saida}")
print(f"Total de registros: {len(df)}")
print(f"Total de colunas documentadas: {len(df.columns)}")

sem_descricao = [
    coluna
    for coluna in df.columns
    if coluna not in descricoes
]

if sem_descricao:
    print("\nATENCAO: colunas sem descricao cadastrada:")
    for coluna in sem_descricao:
        print(f" - {coluna}")
else:
    print("Todas as colunas possuem descricao cadastrada.")

print("\nProcessamento finalizado com sucesso!")
