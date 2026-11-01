#Limpeza de dados

import pandas as pd

from Carrega_dados import CAMINHO_CSV_ORIGINAL, CAMINHO_CSV_LIMPA

class LimpezaDados:
    def __init__(self, df):
        self.df = df.copy()
        self.registros_iniciais = len(df)

    def remover_colunas_vazias(self):
        self.df.dropna(axis=1, how='all')
        return self

    def remover_nulos(self):
        self.df.dropna()
        return self

    def remover_duplicados(self):
        self.df.drop_duplicates().reset_index(drop=True)
        return self

    def executar(self):       
        self.remover_colunas_vazias().remover_nulos().remover_duplicados()
        return self.df

    def mostrar_relatorio(self):
        registros_finais = len(self.df)
        registros_removidos = self.registros_iniciais - registros_finais
        print(f"Registros iniciais: {self.registros_iniciais}")
        print(f"Registros finais: {registros_finais}")
        print(f"Registros removidos: {registros_removidos}")
        return self

    def salvar_csv(self, CAMINHO_CSV_LIMPA):
        self.df.to_csv(CAMINHO_CSV_LIMPA, sep=';')
        print(f"Arquivo CSV salvo em: {CAMINHO_CSV_LIMPA}")
        return self

if __name__ == "__main__":
    from Carrega_dados import CAMINHO_CSV_LIMPA, CAMINHO_CSV_ORIGINAL

    limpeza = LimpezaDados(pd.read_csv(CAMINHO_CSV_ORIGINAL, sep=';'))

    limpeza.executar()

    limpeza.mostrar_relatorio()

    limpeza.salvar_csv(CAMINHO_CSV_LIMPA)
    print(f"Limpeza de dados concluída e salva em: {CAMINHO_CSV_LIMPA}")