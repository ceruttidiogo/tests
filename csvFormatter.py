import os
import pandas as pd

def replace_text(content):
    # Substituições sensíveis a diacríticos
    content = content.replace("\n", "<br>")
    content = content.replace(';', '.,')  # Manter a substituição necessária
    return content

def process_csv(file_path):
    # Ler a planilha CSV com delimitador ';'
    df = pd.read_csv(file_path, delimiter=';', dtype=str)  # Garantir que todo o conteúdo seja tratado como string

    # Criar um DataFrame vazio para armazenar os dados tratados
    df_processed = pd.DataFrame()

    # Aplicar substituições em cada coluna
    for col in df.columns:
        df_processed[col] = df[col].apply(lambda x: replace_text(str(x)))

    # Salvar a planilha processada como CSV com delimitador ';'
    processed_csv_path = file_path.replace('.csv', '_processed.csv')
    df_processed.to_csv(processed_csv_path, sep=';', index=False)
    print(f"Planilha processada e salva como: {processed_csv_path}")

def process_xlsx(file_path):
    # Ler a planilha XLSX
    df = pd.read_excel(file_path, sheet_name=None, dtype=str)

    for sheet_name, data in df.items():
        # Criar uma cópia do DataFrame para aplicar as substituições
        df_processed = data.copy()

        # Aplicar substituições em cada célula
        for col in df_processed.columns:
            df_processed[col] = df_processed[col].apply(lambda x: replace_text(str(x)))

        # Salvar a aba como CSV com delimitador ';'
        csv_path = file_path.replace('.xlsx', f'_{sheet_name}_processed.csv')
        df_processed.to_csv(csv_path, sep=';', index=False)
        print(f"Aba '{sheet_name}' processada e salva como: {csv_path}")

def process_all_files(folder_path, input_format):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(f'.{input_format}'):
                file_path = os.path.join(root, file)
                print(f"Processando arquivo: {file_path}")
                if input_format == 'csv':
                    process_csv(file_path)
                elif input_format == 'xlsx':
                    process_xlsx(file_path)

# Defina o caminho para a pasta contendo os arquivos
folder_path = 'C:/Users/Diogo/Desktop/Planilhas'

# Menu para escolher o formato de entrada
print("Escolha o formato de entrada:")
print("1. CSV")
print("2. XLSX")
choice = input("Digite o número correspondente à sua escolha: ")

if choice == '1':
    input_format = 'csv'
elif choice == '2':
    input_format = 'xlsx'
else:
    print("Escolha inválida. Saindo...")
    exit()

process_all_files(folder_path, input_format)
