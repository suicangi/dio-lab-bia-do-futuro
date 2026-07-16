# Passo a passo do sistema

## Setup do Ollama

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar o funcionamento
ollama run gpt-oss "Olá!"
```

## Código completo

Todo o código-fonte está no arquivo `app.py`.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit)
└── requirements.txt    # Dependências
```

## Como Rodar

```bash
# Instalar dependências
pip install -r .\src\requirements.txt

# Rodar a aplicação
streamlit run .\src\app.py
```
