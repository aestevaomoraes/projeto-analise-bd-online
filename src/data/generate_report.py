import pandas as pd
import warnings
import os
from datetime import datetime

warnings.filterwarnings('ignore')

# Definir caminhos relativos para garantir que funcione em qualquer computador
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'bd_Online.csv')
REPORT_PATH = os.path.join(BASE_DIR, 'reports', f'relatorio_diario_{datetime.now().strftime("%Y-%m-%d")}.md')

def main():
    print("Iniciando a geração do relatório diário...")
    
    if not os.path.exists(CSV_PATH):
        print(f"Erro: Arquivo não encontrado em {CSV_PATH}")
        print("Lembre-se de substituir o arquivo CSV atualizado na pasta 'data/raw/'.")
        return

    # Ler dados
    df = pd.read_csv(CSV_PATH, sep=';', encoding='latin1', low_memory=False)

    # Lógica de negócio: agrupar dados e contar
    venc = df['TEMPO_PARA_VENCIMENTO'].value_counts().to_frame()
    venc.index.name = 'Status de SLA'
    venc.columns = ['Quantidade']

    faixa = df['TEMPO_ABERTURA'].value_counts().to_frame()
    faixa.index.name = 'Faixa de Tempo Abertura'
    faixa.columns = ['Quantidade']

    uf_sla = pd.crosstab(df['UF_A'], df['NO_PRAZO']).sort_values(by='N', ascending=False).head(10)
    uf_sla.index.name = 'Estado'

    vencidos = df[df['TEMPO_PARA_VENCIMENTO'] == 'Vencido']
    cli_venc = vencidos['NOME_CLIENTE'].value_counts().head(10).to_frame()
    cli_venc.columns = ['Quantidade Vencidos']

    serv = vencidos['PRODUTO'].value_counts().head(10).to_frame()
    serv.columns = ['Quantidade Vencidos']

    # Montar o Markdown final
    md_content = f"""# Relatório Diário de Casos e SLA - {datetime.now().strftime("%d/%m/%Y")}

Este relatório apresenta um resumo estatístico das atividades e vencimentos de SLA da base operacional.

## 1. Status de Vencimento de SLA Geral
{venc.to_markdown()}

> 🚨 **Atenção:** Uma grande quantidade de casos consta como "Vencido".

## 2. Faixa de Tempo de Abertura (Todos os Casos)
{faixa.to_markdown()}

## 3. Estados com Mais Casos Fora do Prazo (Top 10)
*(N = Fora do Prazo / S = No Prazo)*
{uf_sla.to_markdown()}

## 4. Clientes com Mais Casos Vencidos (Top 10)
{cli_venc.to_markdown()}

## 5. Tipos de Serviço com Mais Casos Vencidos (Top 10)
{serv.to_markdown()}

---
*Relatório gerado automaticamente em {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""

    # Salvar em um arquivo
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Relatório gerado com sucesso em: {REPORT_PATH}")
    print("Você pode copiar o conteúdo do relatório e colar diretamente no seu email para a gerência!")

if __name__ == "__main__":
    main()
