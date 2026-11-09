# ISA Saúde | Business Intelligence & Healthcare Analytics

### Inteligência de Dados, Performance Operacional e Simulação de Cenários Financeiros

**Projeto de portfólio em Data Analytics e Business Intelligence aplicado à gestão em saúde.**

**Tecnologias:** Python | SQL | SQLite | Power BI | Databricks | PySpark | Git | GitHub

> **Aviso:** Este projeto utiliza dados 100% fictícios, desenvolvidos para fins educacionais e demonstração de competências técnicas. Os resultados não representam informações financeiras ou assistenciais reais da ISA Saúde.

---

## 1. Visão geral

Este projeto demonstra a aplicação de técnicas de Business Intelligence, análise exploratória, tratamento de dados, modelagem e visualização para apoiar decisões estratégicas no setor de saúde.

A solução integra análises assistenciais, operacionais e financeiras, com foco na identificação de oportunidades de melhoria, eficiência operacional e sustentabilidade financeira.

O projeto contempla desde a preparação e validação dos dados até a construção de dashboards e simulações de cenários.

## 2. Objetivos do projeto

- Estruturar uma base analítica para avaliação de atendimentos domiciliares.
- Identificar inconsistências, duplicidades e dados ausentes.
- Desenvolver indicadores operacionais, assistenciais e financeiros.
- Analisar receita, custos, glosas e margens por modalidade e operadora.
- Construir dashboards interativos para apoio à gestão.
- Simular diferentes condições financeiras e avaliar seus impactos.
- Garantir rastreabilidade, consistência e transparência metodológica.

## 3. Arquitetura da solução

**Fonte de dados sintéticos → Python/Pandas → Tratamento e validação → SQLite/SQL → Power BI**

**Dados preparados → Databricks/PySpark → Indicadores financeiros → Simulação de cenários → Dashboard executivo**

O Git e o GitHub são utilizados para versionamento, organização e documentação dos artefatos do projeto.

## 4. Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Exploração, tratamento, análise e automação |
| Pandas | Manipulação, limpeza e agregação de dados |
| SQL | Consultas, consolidação e indicadores |
| SQLite | Armazenamento e análise relacional |
| Power BI | Visualização de indicadores e dashboards |
| Databricks | Processamento e análise de dados |
| PySpark | Transformações e cálculos distribuídos |
| Git e GitHub | Versionamento e documentação |

## 5. Qualidade e governança dos dados

A etapa de qualidade contempla a avaliação de integridade, completude, duplicidade e consistência dos registros.

Na análise financeira auditada no Databricks, foram avaliados **910 registros sintéticos**, dos quais:

- 865 registros (95,05%) apresentavam custo conhecido.
- 45 registros (4,95%) apresentavam custo ausente.
- Não foram identificados IDs duplicados no universo auditado.
- Os custos ausentes não foram automaticamente interpretados como zero.

A receita associada aos registros sem custo foi excluída dos indicadores de margem financeira para preservar a consistência entre receitas e despesas elegíveis.

## 6. Indicadores financeiros

Os resultados auditados, considerando exclusivamente registros com custo conhecido, foram:

| Indicador | Resultado |
|---|---:|
| Receita líquida elegível | R$ 27.139.468,10 |
| Custos conhecidos | R$ 21.157.304,46 |
| Margem financeira | R$ 5.982.163,64 |
| Margem financeira percentual | 22,04% |

**Definições metodológicas:**

Margem financeira = Receita líquida elegível − Custos conhecidos

Margem percentual = Margem financeira ÷ Receita líquida elegível × 100

Os indicadores foram reconciliados com os registros originais e com os resultados agregados por modalidade.

## 7. Simulação de cenários financeiros

Foram desenvolvidos três cenários hipotéticos para avaliar a sensibilidade da margem financeira às variações de receita e custo.

| Cenário | Receita | Custo |
|---|---:|---:|
| Base | Sem alteração | Sem alteração |
| Otimista | +5% | −5% |
| Pressão | −5% | +10% |

A simulação foi aplicada às modalidades:

- Internação Domiciliar (ID).
- Assistência Domiciliar (AD).
- Atendimento por Visitas.

**Principais resultados:**

A Internação Domiciliar apresentou maior sensibilidade financeira relativa, com variação de margem de +52,38% no cenário otimista e −76,08% no cenário de pressão.

O Atendimento por Visitas apresentou redução relativa de −28,93% no cenário de pressão, a menor entre as modalidades analisadas.

Esses resultados são exercícios de sensibilidade baseados em premissas definidas, e não previsões estatísticas de desempenho futuro.

## 8. Dashboards e visualizações

### Power BI — Inteligência operacional e financeira

Desenvolvimento de visualizações voltadas ao acompanhamento de indicadores, qualidade dos dados, análise de glosas e performance financeira.

**Arquivo:** `ISA_Saude_Dashboard.pbix`

### Databricks — Inteligência financeira e simulação de cenários

Painel executivo contendo:

- Receita líquida elegível.
- Custos conhecidos.
- Margem financeira absoluta e percentual.
- Margem por modalidade.
- Simulação de cenários.
- Impacto percentual por cenário.
- Insights estratégicos e observações metodológicas.

*As imagens e o notebook exportado do Databricks serão incorporados à documentação do projeto.*

## 9. Validação e auditoria metodológica

Foi realizada uma auditoria técnica dos indicadores financeiros, incluindo:

- Reconciliação entre receita, custos e margem.
- Comparação dos resultados agregados com os registros originais.
- Verificação do tratamento dos custos ausentes.
- Avaliação dos denominadores dos indicadores percentuais.
- Validação das premissas e dos resultados das simulações.
- Verificação da consistência entre cartões e gráficos.

**Resultado:** nenhuma divergência financeira identificada nos testes executados.

**Limitação identificada:** na versão auditada, o dashboard Databricks não possuía filtros globais. A implementação de filtros e sua propagação para os datasets de simulação constituem uma evolução funcional.

## 10. Organização do repositório

```text
ISA_Saude_Case/
├── data/
│   ├── raw/
│   └── processed/
├── graficos/
├── python/
│   ├── 01_exploracao.py
│   ├── 02_qualidade_dados.py
│   ├── 03_analise_financeira.py
│   ├── 04_grafico_qualidade.py
│   ├── 05_tratamento_dados.py
│   ├── 06_grafico_glosas.py
│   ├── 07_criar_banco_sql.py
│   ├── 08_analise_sql.py
│   └── 09_grafico_financeiro.py
├── ISA_Saude_Dashboard.pbix
├── .gitignore
└── README.md
```

## 11. Competências demonstradas

- Business Intelligence e Data Analytics.
- Data Quality e preparação de dados.
- SQL e modelagem analítica.
- Desenvolvimento de indicadores financeiros.
- Visualização e comunicação executiva.
- Simulação de cenários e análise de sensibilidade.
- Validação metodológica e rastreabilidade.
- Pensamento analítico orientado à tomada de decisão.

## 12. Próximas evoluções

- Documentação e exportação do notebook Databricks.
- Inclusão de imagens dos dashboards.
- Implementação e validação de filtros interativos.
- Criação de um módulo demonstrativo de CRM com HubSpot e dados sintéticos.
- Ampliação da documentação de arquitetura e regras de negócio.

---

**Projeto desenvolvido para demonstração de competências em Business Intelligence, Analytics e Inteligência em Saúde.**

*Todos os dados utilizados são fictícios.*