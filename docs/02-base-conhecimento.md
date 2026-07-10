# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Para que serve no Pato? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, dar continuidade no atendimento (Histórico do cliente) |
| `perfil_investidor.json` | JSON | Personalização das recomendações para o cliente, ou seja, explicação sobre as dúvidas e necessidades do cliente |
| `produtos_financeiros.json` | JSON | Base de dados dos produtos a serem explicados, ensinados ou sugeridos ao cliente |
| `transacoes.csv` | CSV | Histórico dos gastos do cliente e com essas informações utilizá-las de forma didática |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Adicionei dois novos fundos de investimentos no arquivo `produtos_financeiro.json`. Um fundo imobiliário (Fii) e um fundo de investimento DI (mais simples). Somente para diversificar os dados e validar a saída dos dados.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Serão carregados os arquivos via código, mas poderá ser injetado dinamicamente se necessário (CTRL + C, CTRL + V).

```python
import pandas as pd
import json

# JSONs

with open('data/perfil_investidor.json', 'r', encoding="utf-8") as f:
	perfil_investidor = json.load(f)
	
with open('data/produtos_financeiros.json', 'r', encoding="utf-8") as f:
	produtos_financeiros = json.load(f)
	
# CSVs

historico_atendimento = pd.read_csv('data/historico_atendimento.csv')

transacoes = pd.read_csv('data/transacoes.csv')
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```text
PERFIL DO INVESTIDOR OU CLIENTE (JSON):

{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

HISTÓRICO DE ATENDIMENTO DO INVESTIDOR OU CLIENTE (CSV):

data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

TRANSAÇÕES DO INVESTIDOS OU CLIENTE (CSV):

data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

PRODUTOS FINANCEIROS PARA A EDUCAÇÃO FINANCEIRA (JSON):

[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Imobiliário (FII)",
    "categoria": "fundo",
    "risco": "moderado",
    "rentabilidade": "9%",
    "aporte_minimo": 10.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  },
  {
  "nome": "Fundo DI",
  "categoria": "fundo",
  "risco": "baixo",
  "rentabilidade": "Próxima de 100% do CDI",
  "aporte_minimo": 100.00,
  "indicado_para": "Quem busca liquidez e baixo risco para objetivos de curto prazo"
  }
]

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Os dados do exemplo abaixo é uma síntese das informações e dados disponíveis para o nosso contexto. Isso também é importante para a otimização do consumo dos tokens.

```
DADOS DO CLIENTE:
- Nome: João Silva
- Perfil: Moderado
- Objetivo Principal: Construir reserva de emergência 
- Reserva atual: R$ 10.000 (meta: R$ 15.000)

RESUMO DAS TRANSAÇÕES:
- 25/10: Combustível - R$ 250
- 20/10: Academia - R$ 99
- 15/10: Conta de Luz - R$ 180

PRODUTOS DISPONÍVEIS PARA O INVESTIDOR:
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Imobiliário (FII) (risco moderado)
- Fundo de Ações (risco alto)
- Fundo DI (risco baixo)

```
