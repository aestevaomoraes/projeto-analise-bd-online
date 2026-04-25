import os
import glob
import markdown
import win32com.client as win32
from datetime import datetime

# Caminhos do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

def get_latest_report():
    # Encontra todos os arquivos .md na pasta reports
    list_of_files = glob.glob(os.path.join(REPORTS_DIR, '*.md'))
    if not list_of_files:
        return None
    # Pega o mais recente baseado na data de criacao
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def main():
    print("Iniciando automação de envio de e-mail...")
    
    latest_report = get_latest_report()
    if not latest_report:
        print("Erro: Nenhum relatório encontrado na pasta reports.")
        return

    print(f"Lendo o relatório: {os.path.basename(latest_report)}")
    
    # Ler o conteúdo Markdown
    with open(latest_report, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Converter Markdown para HTML, ativando a extensão de tabelas
    html_content = markdown.markdown(md_text, extensions=['tables'])

    # Aplicar CSS corporativo (Padrão limpo, com destaque verde e cinza)
    estilo_html = f"""
    <html>
    <head>
    <style>
        body {{
            font-family: 'Segoe UI', Calibri, Arial, sans-serif;
            color: #333333;
            line-height: 1.6;
            margin: 20px;
        }}
        h1, h2, h3 {{
            color: #4a4a4a; /* Cinza corporativo sobrio */
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 3px;
            margin-top: 20px;
            font-size: 16px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            max-width: 800px;
            margin: 15px 0;
            font-size: 11px; /* Diminuindo o tamanho */
        }}
        th {{
            background-color: #555555; /* Fundo cinza escuro */
            color: white;
            text-align: left;
            padding: 6px;
            border: 1px solid #ccc;
        }}
        td {{
            padding: 4px 6px;
            border: 1px solid #ccc;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        blockquote {{
            background-color: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 10px;
            margin: 20px 0;
            border-radius: 4px;
        }}
    </style>
    </head>
    <body>
        <p>Prezado Antonio,</p>
        <p>Segue abaixo o <b>Relatório Diário de Casos e SLA</b> automatizado para acompanhamento.</p>
        <hr>
        {html_content}
        <br>
        <hr>
        <p><i>Este é um e-mail gerado automaticamente via Python. Favor não responder.</i></p>
        <p>Atenciosamente,<br><b>Automação de Relatórios - Data Analytics</b></p>
    </body>
    </html>
    """

    # Integração com Outlook para envio
    try:
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)

        # Configurar destinatário para teste
        mail.To = 'antonio.neto@oi.net.br'
        mail.Subject = f'Relatório Diário de SLA Automatizado - {datetime.now().strftime("%d/%m/%Y")}'
        mail.HTMLBody = estilo_html

        mail.Send()
        print("Email enviado com sucesso via Outlook!")

    except Exception as e:
        print(f"Erro ao enviar email pelo Outlook: {e}")

if __name__ == "__main__":
    main()
