
# Case Executivo — ISA Saúde Analytics

## 1. Contexto do projeto

Projeto demonstrativo de Business Intelligence e Healthcare Analytics, desenvolvido com dados sintéticos de atendimentos em saúde.

O objetivo é transformar dados operacionais e financeiros em informações relevantes para apoiar decisões estratégicas, monitorar desempenho e identificar oportunidades de melhoria.

## 2. Problema de negócio

Organizações de saúde precisam acompanhar simultaneamente:

- Receita e custos assistenciais.
- Rentabilidade por modalidade de atendimento.
- Qualidade e integridade das informações.
- Variações de desempenho entre operadoras.
- Exposição financeira a mudanças nas condições operacionais.

A ausência de uma visão integrada desses indicadores pode dificultar a identificação de riscos e oportunidades.

## 3. Objetivos analíticos

- Consolidar informações financeiras e operacionais.
- Avaliar a qualidade dos dados.
- Calcular indicadores de receita, custo e margem.
- Comparar modalidades de atendimento.
- Simular cenários de sensibilidade financeira.
- Disponibilizar dashboards para análise gerencial.

## 4. Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Processamento e análise |
| Pandas | Tratamento e exploração de dados |
| SQL | Consultas e agregações |
| SQLite | Armazenamento local |
| PySpark | Processamento analítico no Databricks |
| Databricks | Análise e dashboard financeiro |
| Power BI | Visualização de indicadores |
| Git/GitHub | Versionamento e documentação |

## 5. Base de dados

- 910 registros sintéticos.
- 27 variáveis documentadas.
- Informações clínicas, operacionais e financeiras.
- 865 registros com custo conhecido.
- 45 registros com custo ausente.

Para análises de margem, os registros com custos ausentes foram excluídos dos cálculos financeiros comparativos, evitando a substituição indevida de valores ausentes por zero.

## 6. Resultados financeiros

| Indicador | Resultado |
|---|---:|
| Receita líquida analisada | R$ 27,14 milhões |
| Custos conhecidos | R$ 21,16 milhões |
| Margem financeira | R$ 5,98 milhões |
| Margem financeira percentual | 22,04% |

Os valores apresentados correspondem aos registros com custos conhecidos, sem aplicação de filtros adicionais.

## 7. Análise por modalidade

### Internação Domiciliar (ID)

- Maior margem financeira absoluta.
- Margem aproximada de R$ 3,46 milhões.
- Maior sensibilidade relativa entre as modalidades nos cenários simulados.

### Assistência Domiciliar (AD)

- Margem financeira aproximada de R$ 2,14 milhões.
- Margem percentual superior à da Internação Domiciliar.

### Atendimento por Visitas

- Margem financeira aproximada de R$ 388 mil.
- Maior margem percentual entre as três modalidades.

## 8. Simulação de cenários

Foram desenvolvidos três cenários:

| Cenário | Variação da receita | Variação do custo |
|---|---:|---:|
| Base | 0% | 0% |
| Otimista | +5% | -5% |
| Pressão | -5% | +10% |

Na Internação Domiciliar, a margem financeira apresentou:

- Crescimento de aproximadamente 52,38% no cenário otimista.
- Redução de aproximadamente 76,08% no cenário de pressão.

Esses resultados representam sensibilidade às premissas definidas, e não projeções estatísticas.

## 9. Insights estratégicos

1. A Internação Domiciliar concentra a maior margem financeira absoluta e apresenta maior sensibilidade às premissas simuladas.

2. A avaliação dos direcionadores de custo pode contribuir para identificar oportunidades de eficiência operacional.

3. A comparação entre margem absoluta e percentual demonstra a importância de analisar rentabilidade sob diferentes perspectivas.

4. O tratamento adequado de dados ausentes contribui para maior confiabilidade dos indicadores.

## 10. Recomendações

- Monitorar periodicamente a margem por modalidade.
- Investigar os principais componentes dos custos.
- Acompanhar a completude das informações financeiras.
- Utilizar simulações como ferramenta de apoio à avaliação de riscos.
- Integrar indicadores financeiros e operacionais na tomada de decisão.

## 11. Competências demonstradas

- Business Intelligence e Analytics.
- Análise financeira em saúde.
- Modelagem e tratamento de dados.
- Python, SQL e PySpark.
- Desenvolvimento de dashboards.
- Qualidade e governança de dados.
- Pensamento analítico e visão estratégica de negócio.

## 12. Limitações

Este projeto utiliza exclusivamente dados fictícios.

Os resultados não representam o desempenho real da ISA Saúde ou de qualquer instituição.

As simulações são hipotéticas e não constituem previsões financeiras.

