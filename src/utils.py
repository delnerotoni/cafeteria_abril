import pandas as pd

def carregar_dados(caminho, encoding='utf-8'):
    """
    Carrega um CSV em um DataFrame pandas.
    """
    return pd.read_csv(caminho, encoding=encoding)
