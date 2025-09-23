#Conteúdo inicial dos arquivos
import pandas as pd

def limpar_valores(df, coluna):
    """
    Converte coluna de valores monetários para float.
    Exemplo: '27,77' -> 27.77
    """
    df[coluna] = df[coluna].str.replace(',', '.').astype(float)
    return df

def padronizar_categorias(df, coluna, mapa):
    """
    Padroniza categorias de uma coluna com base em um dicionário de mapeamento.
    Exemplo: {'Cartão crédito': 'Crédito'}
    """
    df[coluna] = df[coluna].replace(mapa)
    return df
