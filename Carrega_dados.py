#Ler CSV Base_Varejo

import pandas as pd

CAMINHO_CSV = "Base_Varejo.csv"

def carregar_dados():
    try:
        df = pd.read_csv(CAMINHO_CSV, sep=';', encoding='latin-1'  )
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo {CAMINHO_CSV} não foi encontrado.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo {CAMINHO_CSV} está vazio.")
        return None
    except pd.errors.ParserError:
        print(f"Erro: O arquivo {CAMINHO_CSV} não pôde ser analisado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

if __name__ == "__main__":
    df = carregar_dados()
    if df is not None:
        print("Dados carregados com sucesso!")
        print(df.head())
    else:
        print("Falha ao carregar os dados.")
    