import seaborn as sns
import matplotlib.pyplot as plt

def plot_ticket_por_categoria(df, coluna, valor='Valor_da_compra_R$'):
    """
    Plota o ticket médio por categoria de uma coluna.
    """
    sns.barplot(x=coluna, y=valor, data=df)
    plt.title(f"Ticket Médio por {coluna}")
    plt.show()

def plot_distribuicao_valores(df, coluna='Valor_da_compra_R$'):
    """
    Plota a distribuição dos valores de compra.
    """
    sns.histplot(df[coluna], bins=20, kde=True)
    plt.title("Distribuição do Valor das Compras")
    plt.show()
