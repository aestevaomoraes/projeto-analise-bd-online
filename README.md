# Projeto de Análise de Bases de Dados Online

Bem-vindo ao projeto de análise da base operacional corporativa. Este projeto foi estruturado seguindo as melhores práticas de Data Science, focado em agilidade para extração de relatórios automatizados de SLA e Tempos.

## 📁 Estrutura de Pastas

* **data/raw/**: Pasta para os arquivos brutos. Coloque o seu `bd_Online.csv` mais recente aqui.
* **reports/**: Pasta onde os relatórios gerados em Markdown serão salvos.
* **src/data/**: Contém o script Python para geração do relatório diário automatizado.
* **notebooks/**: Para futuras explorações de dados no Jupyter.

## 🚀 Como Executar o Relatório Diário

Seu principal fluxo de trabalho diário será:
1. Extrair a base mais recente (`bd_Online.csv`).
2. Substituir o arquivo existente na pasta `data/raw/bd_Online.csv`.
3. Executar o script `generate_report.py`.

### Passo a Passo no Terminal/CMD:

Abra o terminal nesta pasta e instale as dependências (somente na primeira vez):
```bash
pip install -r requirements.txt
```

Para rodar a automação diária, execute:
```bash
python src/data/generate_report.py
```

O script lerá a base atualizada, fará todos os cálculos e salvará um novo arquivo de relatório na pasta `reports/` com a data do dia. Você pode simplesmente abrir este arquivo, copiar o conteúdo e colar no corpo do e-mail para a sua gerência!

## 📦 Envio para o GitHub (Portfólio)
Este projeto já possui o Git inicializado. Para enviar para o GitHub:
1. Crie um repositório vazio no seu GitHub.
2. Rode os comandos:
```bash
git add .
git commit -m "Initial commit - Estrutura do projeto e script de relatório diário"
git remote add origin SUA_URL_DO_GITHUB_AQUI
git push -u origin main
```
