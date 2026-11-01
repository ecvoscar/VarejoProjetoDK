#Ler CSV Base_Varejo

import os
import pandas as pd

PASTA = os.path.dirname(os.path.abspath(__file__))
CAMINHO_CSV_ORIGINAL = os.path.join(PASTA,'Base_Varejo_Original.csv')
CAMINHO_CSV_LIMPA = os.path.join(PASTA,'Base_Varejo_Limpa.csv')

def carregar_dados():
    
        df = pd.read_csv(CAMINHO_CSV_LIMPA, sep=';')
        return df

if __name__ == "__main__":
    df = carregar_dados()
    if df is not None:
        print("Dados carregados com sucesso!")
        print(df.head())
    else:
        print("Falha ao carregar os dados.")
