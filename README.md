# Pato: O Facilitador e Educador Financeiro 🦆

Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para agentes inteligentes e proativos.

O **Pato** é um agente financeiro inteligente que utiliza IA Generativa para:
- **Antecipar necessidades** ao invés de apenas responder perguntas (avisos proativos sobre gastos e investimentos).
- **Personalizar sugestões** com base no contexto de cada cliente utilizando dados locais estruturados.
- **Cocriar soluções financeiras** de forma consultiva com analogias leves e simples ("não pague o pato").
- **Garantir segurança e confiabilidade** nas respostas (estratégias rigorosas anti-alucinação).

Este projeto é um fork modificado a partir do template original `dio-lab-bia-do-futuro` da DIO.

---

## 📂 Estrutura do Projeto

O desenvolvimento do agente está organizado seguindo o mesmo padrão do template original:

```text
📁 dio-lab-pato-do-futuro/
│
├── 📁 data/                          # Dados mockados do cliente (RAG local)
│   ├── 📊 transacoes.csv             # Histórico de transações do cliente
│   ├── 📊 historico_atendimento.csv   # Histórico de atendimentos anteriores
│   ├── ⚙️ perfil_investidor.json     # Perfil e preferências do cliente
│   └── ⚙️ produtos_financeiros.json   # Produtos e serviços disponíveis
│
├── 📁 docs/                          # Documentação e Engenharia de Prompt do Pato
│   ├── 📄 01-documentacao-agente.md   # Caso de uso, Persona, Tom de Voz e Fluxo do Agente
│   ├── 📄 02-base-conhecimento.md    # Estrutura lógica da base de dados e RAG
│   ├── 📄 03-prompts.md              # System Prompts estruturados e técnicas aplicadas
│   ├── 📄 04-metricas.md             # Métricas de avaliação de segurança do modelo
│   └── 📄 05-pitch-apresentacao.md   # Roteiro/Pitch de apresentação do projeto
│
└── 📄 README.md                      # Visão geral do projeto

```

---

## 🛠️ Arquitetura e Engenharia do Agente

Para garantir uma simulação realista e segura de um assistente financeiro baseado em IA, o Pato foi modelado sob os seguintes pilares técnicos:

1. **Contextualização Fiel (Grounding):** O agente foi instruído a restringir suas análises e recomendações estritamente aos limites dos dados presentes na pasta `data/`.
2. **Engenharia de Prompt Robusta:** Utilização de técnicas avançadas de estruturação de prompts, incluindo:
* *System Prompts* estritos com regras de segurança comportamental.
* Cenários estruturados de *Few-Shot Prompting* para calibração fina da sua identidade verbal.
* Instruções de *Chain-of-Thought* para raciocínio lógico em análises numéricas e recomendações de produtos.


3. **Segurança e Anti-Alucinação:** Bloqueio ativo de respostas fora do contexto financeiro do cliente e salvaguardas para que o agente não crie (alucine) novos serviços ou ofertas que não estejam indexados no catálogo oficial.

---

## 👥 Persona: Quem é o Pato?

Diferente de assistentes tradicionais formais e engessados, o **Pato** adota uma identidade comunicativa irreverente, didática e motivadora. Ele simplifica jargões pesados do mercado usando metáforas do dia a dia e está sempre focado em guiar o usuário em direção a uma saúde financeira sustentável de forma bem-humorada.

---

## ▶️ Pitch: Apresentação do Pato

[\[Link do vídeo\]](https://youtu.be/R_kRxETGGUM)

---

## ✒️ Créditos e Origem

Este projeto foi desenvolvido por [Inacio Araújo Magalhães Campos de Azevedo](https://www.google.com/search?q=https://github.com/suicangi) como solução para o desafio prático de IA Generativa da **DIO (Digital Innovation One)**.