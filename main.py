import pandas as pd
import os

def criar_pastas_excel(file_path):
    
    df = pd.read_excel(file_path)
    
    print("Nomes das colunas:", df.columns)


    
    # ler linhas do DataFrame
    for index, row in df.iterrows():
        nome_pasta = str(row['Digite a coluna/nome da pasta']) # nome_pasta = string
        status = row['pasta status/pasta a ser comparada']
        



        if pd.isna(status) or status.lower() != 'bloqueada':
            if not os.path.exists(nome_pasta):
                os.makedirs(nome_pasta)
                print(f'Pasta "{nome_pasta}" criada.')
            else:
                print(f'Pasta "{nome_pasta}" já existe.')
        else:
            print(f'Pasta "{nome_pasta}" Não foi criada. Status: "bloqueada".')

file_path = r'C:\Seu\Caminho\Para\O\Arquivo.xlsx'

criar_pastas_excel(file_path)

