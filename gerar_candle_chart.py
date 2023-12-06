import os
import pandas as pd
import mplfinance as mpf

def plot_chart(file_path, save_directory, image_name):
    # Criando o diretório se não existir
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Lendo os dados do arquivo
    df = pd.read_csv(file_path, decimal='.', sep=';')

    # Convertendo a coluna 'Date' para datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Definindo a coluna 'Date' como o índice do DataFrame
    df.set_index('Date', inplace=True)
    
    # Convertendo as colunas para float
    df['Open'] = df['Open'].astype(float)
    df['High'] = df['High'].astype(float)
    df['Low'] = df['Low'].astype(float)
    df['Close'] = df['Close'].astype(float)
    df['Volume'] = df['Volume'].astype(float)

    plot_style = {
        'title': image_name,
        'type': 'candle',  # Tipo de gráfico. Pode ser 'ohlc', 'candle', 'line', etc.
        'volume': True,   # Se deseja mostrar o volume
        'figratio': (16,9), # Aspecto da figura
        'figscale': 1.5   # Escala da figura
    }

    savefig_dict = {
        'fname': os.path.join(save_directory, image_name+'.png'),
        'dpi': 100  # Você pode ajustar a resolução (DPI) conforme necessário
    }

    # Plotando e salvando o gráfico
    mpf.plot(df, **plot_style, savefig=savefig_dict)
