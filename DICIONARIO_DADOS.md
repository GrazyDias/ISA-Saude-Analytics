# Dicionário de Dados — ISA Saúde Analytics

Base de dados fictícia para demonstração de competências técnicas.

**Registros:** 910
**Colunas:** 27

## Estrutura e descrição das variáveis

| Coluna | Tipo identificado | Valores ausentes | Descrição / regra de negócio |
|---|---|---:|---|
| ID Paciente | str | 0 | Identificador do paciente ou registro na base fictícia. |
| Operadora | str | 0 | Operadora de saúde vinculada ao atendimento. |
| Modalidade | str | 0 | Tipo de assistência: Internação Domiciliar (ID), Assistência Domiciliar (AD) ou Atendimento por Visitas. |
| Patologia Principal | str | 0 | Condição clínica principal associada ao atendimento. |
| Região | str | 0 | Região geográfica de referência do atendimento. |
| CFS | int64 | 0 | Campo numérico CFS. Definição operacional a validar. |
| Data Implantação | str | 0 | Data de implantação ou início do atendimento. |
| Data Alta | str | 112 | Data de encerramento do atendimento, quando registrada. |
| Status | str | 0 | Situação do atendimento conforme classificação da base. |
| Dias Atendimento | int64 | 0 | Quantidade de dias de atendimento registrada. |
| Diária (R$) | int64 | 0 | Valor monetário da diária de atendimento registrado na base. A unidade, a composição e a regra de cobrança devem ser validadas. |
| OPME (R$) | int64 | 0 | Valor registrado de órteses, próteses e materiais especiais. |
| Receita Bruta (R$) | int64 | 0 | Receita bruta registrada antes das deduções aplicáveis. |
| Glosa (R$) | float64 | 0 | Valor de glosa registrado no atendimento. |
| Custo (R$) | float64 | 45 | Custo registrado do atendimento. Valores ausentes não devem ser automaticamente substituídos por zero. |
| Reinternação | str | 0 | Indicador de reinternação conforme classificação da base. |
| SLA Aceite (dias) | float64 | 27 | Prazo registrado para aceite, em dias. |
| Operadora Original | str | 0 | Nome da operadora antes da padronização. |
| Chave | str | 0 | Campo auxiliar utilizado na integração ou padronização. Regra exata a validar. |
| Operadora Padronizada | str | 0 | Nome da operadora após tratamento e padronização. |
| Contrato Encontrado | bool | 0 | Indicador de correspondência contratual encontrada na integração. |
| Custo Ausente | bool | 0 | Indicador de ausência do valor de custo no registro. |
| SLA Ausente | bool | 0 | Indicador de ausência do prazo de aceite. |
| Data Alta Ausente | bool | 0 | Indicador de ausência da data de alta. |
| Receita Líquida (R$) | float64 | 0 | Receita após deduções. Fórmula exata a validar no processamento. |
| Margem (R$) | float64 | 45 | Resultado financeiro do atendimento. Fórmula exata a validar no processamento. |
| Margem (%) | float64 | 45 | Margem financeira percentual. Fórmula e tratamento de receita zero a validar. |

## Regras de qualidade e interpretação

- Os dados utilizados neste projeto são fictícios.
- Valores ausentes são identificados e contabilizados automaticamente.
- Custos ausentes não devem ser interpretados como custo zero.
- Indicadores financeiros que dependem do custo devem utilizar registros com custo conhecido, conforme a metodologia do dashboard.
- A margem percentual agregada deve ser calculada a partir dos totais financeiros, e não pela soma ou média simples das margens percentuais.
- As regras exatas de cálculo dos campos financeiros devem ser conferidas nos scripts de tratamento e análise.

## Simulação de cenários

O dashboard apresenta cenários hipotéticos de sensibilidade financeira:

- **Base:** receita e custo sem alterações.
- **Otimista:** receita multiplicada por 1,05 e custo por 0,95.
- **Pressão:** receita multiplicada por 0,95 e custo por 1,10.

Os cenários são simulações hipotéticas e não previsões estatísticas.

## Tecnologias

Python, Pandas, SQL, PySpark, Databricks, Power BI e GitHub.

## Observação

As descrições são preliminares e devem ser validadas contra as regras de negócio e os scripts de processamento.
