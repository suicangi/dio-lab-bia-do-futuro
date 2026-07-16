# 🦆 Pato: O Facilitador e Educador Financeiro

O **Pato** é um agente inteligente e proativo de inteligência artificial generativa, desenvolvido como um projeto prático para o desafio de projeto da **DIO (Digital Innovation One)**. Ele foi projetado para transformar a relação das pessoas com o dinheiro, atuando não apenas como um chatbot tradicional reativo, mas como um consultor proativo focado em educação financeira de forma simples, acessível e segura.

---

## 🚀 Objetivos do Projeto
*   **Facilitação:** Traduzir termos financeiros complexos em conceitos simples do dia a dia.
*   **Proatividade:** Antecipar necessidades e sugerir alertas de gastos com base no comportamento do usuário.
*   **Educação Financeira:** Propor rotinas de poupança, investimentos adequados e planejamento de metas.
*   **Segurança (Anti-Alucinação):** Garantir respostas extremamente confiáveis baseadas estritamente em dados reais e bases de conhecimento controladas.

---

## 📂 Estrutura do Repositório

O desenvolvimento está dividido de maneira organizada entre código, dados simulados e documentação de arquitetura:

```text
📁 dio-lab-pato-do-futuro/
│
├── 📁 docs/                        # Documentação do Agente e Engenharia de Prompt
│   ├── 📄 01-documentacao-agente.md # Caso de uso, Persona (Pato), Tom de Voz e Fluxos
│   ├── 📄 02-base-conhecimento.md  # Estruturação e indexação dos dados mockados
│   ├── 📄 03-prompts.md            # System Prompts utilizados e técnicas de Few-Shot
│   ├── 📄 04-metricas.md           # Métricas de avaliação de segurança e respostas
│   └── 📄 05-pitch-apresentacao.md # Roteiro e pitch final do projeto
│
├── 📁 data/                        # Base de Dados Mockados do Cliente (RAG)
│   ├── 📊 transacoes.csv           # Histórico financeiro e comportamento de consumo
│   ├── 📊 historico_atendimento.csv # Interações anteriores para análise de contexto
│   ├── ⚙️ perfil_investidor.json   # Tolerância a riscos e preferências do usuário
│   └── ⚙️ produtos_financeiros.json # Portfólio de produtos disponíveis para recomendação
│
└── 📄 README.md                    # Visão geral do projeto