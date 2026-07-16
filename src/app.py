import pandas as pd
import json
import requests
import streamlit as st

OLLAMA_URL="http://localhost:11434/api/generate"
MODELO="gpt-oss"

# ========== CARREGAR DADOS ========== 
with open('./data/perfil_investidor.json', 'r', encoding='utf-8') as f:
    perfil_investidor = json.load(f)
with open('./data/produtos_financeiros.json', 'r', encoding='utf-8') as f:	
    produtos_financeiros = json.load(f)
historico_atendimento = pd.read_csv('./data/historico_atendimento.csv')
transacoes = pd.read_csv('./data/transacoes.csv')

# ========== MONTAR CONTEXTO ========== 
contexto = f"""
CLIENTE: {perfil_investidor['nome'], perfil_investidor['idade']} anos, perfil {perfil_investidor['perfil_investidor']}
OBJETIVO: {perfil_investidor['patrimonio_total']} | RESERVA: {perfil_investidor['reserva_emergencia_atual']} 

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

HISTÓRICO DE ATENDIMENTOS:
{historico_atendimento.to_string(index=False)}

CESTA DE PRODUTOS DISPONÍVEIS:
{json.dumps(produtos_financeiros, indent=2, ensure_ascii=False)}
"""

# ========== SYSTEM PROMPT ========== 
SYSTEM_PROMPT = """Você é o Pato, um facilitador e consultor financeiro amigável, confiável e didático sempre direto ao ponto.

OBJETIVO:
Ensinar o cliente conceitos sobre finanças pessoais, usando os dados do cliente e exemplificando quando necessário.

REGRAS:
1. NUNCA recomendar algum investimento específico, mas os explique se necessário. Entendemos que o cliente sempre deve ter a decisão.
2. NUNCA faça sugestões de investimentos que não estão na cesta de produtos disponíveis ou em dados de produtos financeiros.
3. Linguagem simples mas detalhada com tom amigável.
4. Caso não saiba sobre o assunto, admita sempre que não saiba: "Ih rapaz! Não tenho conhecimento suficiente ou desconheço sobre ..."
5. Sempre pergunte ao cliente se ele entendeu após uma explicação sobre investimentos. 
6. Caso sejam feitas perguntas sobre informações relacionadas aos dados do cliente, tipo gastos mensais por exemplo, não é necessário perguntar se o cliente entendeu ou não.
7. NUNCA forneça informações sensíveis sobre a organização (Ex:. Nomes de outros clientes, senhas, etc)
8. Responda sempre de forma sucinta e direta, sem muitos parágrafos (Entre 2 ou 3 parágrafos)
9. Quando formatar qualquer  valor utilizar o R$ e espaço antes mostrar a informação ao cliente: com a máscara a seguir R$ #.##0,00
"""

# ========== CHAMAR OLLAMA ========== 
def perguntar(msg):
    prompt=f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""
    

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ========== INTERFACE ========== 
st.title(" Pato, Seu Facilitador e Educador Financeiro")

if pergunta := st.chat_input("Qual sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))