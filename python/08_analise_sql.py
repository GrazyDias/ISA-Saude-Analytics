
import sqlite3
import pandas as pd
from pathlib import Path

# Localizar o banco de dados
raiz = Path(__file__).resolve().parent.parent
banco = raiz / "data" / "isa_saude.db"

# Consulta SQL
consulta = """
SELECT
    operadora_padronizada AS operadora,
    COUNT(*) AS atendimentos,
    ROUND(SUM(receita_bruta_r), 2) AS receita_bruta,
    ROUND(SUM(glosa_r), 2) AS glosas,
    ROUND(
        100.0 * SUM(glosa_r) /
        NULLIF(SUM(receita_bruta_r), 0), 2
    ) AS taxa_glosa_pct,
    ROUND(SUM(custo_r), 2) AS custos_conhecidos
FROM atendimentos
GROUP BY operadora_padronizada
ORDER BY taxa_glosa_pct DESC
"""

with sqlite3.connect(banco) as conexao:
    resultado = pd.read_sql_query(consulta, conexao)

print("\n=== ANÁLISE FINANCEIRA SQL ===")
print(resultado.to_string(index=False))

# Exportar resultados para Excel
saida = raiz / "data" / "processed"
saida.mkdir(parents=True, exist_ok=True)

arquivo = saida / "analise_financeira_sql.xlsx"
resultado.to_excel(arquivo, index=False)

print("\nArquivo gerado com sucesso:")
print(arquivo)
