from funcao_time_bar import resumo_time
from funcao_volume_bar import resumo_volume
from funcao_dolar_bar import resumo_dolar
from gerar_candle_chart import  plot_chart

def parse_negociacao(linha):
    campos = linha.split(';')
    timestamp = campos[0]  # Data-Hora
    ativo = campos[1]  # Data-Hora   
    preco = float(campos[3].replace(',', '.'))  # Preço do Negócio
    volume = int(campos[4].replace(',', '.'))   # Quantidade Negociada
    valor_reais = preco*volume  # Valor em reais negociado
    return timestamp, ativo, preco, volume, valor_reais

def get_negociacoes(arquivo):
    with open(arquivo, "r") as file:
        linhas = file.readlines()[0:]
        return [parse_negociacao(linha) for linha in linhas]
            
def geracao_de_arquivo(lista, nome_do_arquivo):
    with open(f"{nome_do_arquivo}.txt", "w") as arquivo:
        line = "Date;Open;High;Low;Close;Volume"
        arquivo.write(line + "\n")
        for item in lista:
            line = ";".join(map(str, item))
            arquivo.write(line + "\n")
    return

def main():
    
    ###################################################
    # fazendo as barras para os dados de dolar DOLG19 #
    ###################################################
    negociacoes = get_negociacoes("Dados Entrada/dados_dolar.txt")
    
    # Bloco de código para timebar
    delta_tempo_minutos = 120   # Input do tempo em minutos desejado
    delta_tempo_milissegundos = delta_tempo_minutos * 60 * 1000  # Transformando delta_tempo em milissegundos (3 minutos)
    campo_ativo = "DOLG19"
    dados_time_bar = resumo_time(negociacoes, delta_tempo_milissegundos, campo_ativo)
    geracao_de_arquivo(dados_time_bar, "resultados_dolar/arquivo_time_bar")
    plot_chart("resultados_dolar/arquivo_time_bar.txt", 'resultados_dolar','Chart Time Bar')

    # Bloco de código para volumebar
    delta_volume = 100000
    dados_volume_bar = resumo_volume(negociacoes, delta_volume, campo_ativo)
    geracao_de_arquivo(dados_volume_bar, "resultados_dolar/arquivo_volume_bar")
    plot_chart("resultados_dolar/arquivo_volume_bar.txt", 'resultados_dolar','Chart Volume Bar')

    # Bloco de código para dolarbar
    delta_valor = 300000000
    dados_valor_bar = resumo_dolar(negociacoes, delta_valor, campo_ativo)
    geracao_de_arquivo(dados_valor_bar, "resultados_dolar/arquivo_dolar_bar")
    plot_chart("resultados_dolar/arquivo_dolar_bar.txt", 'resultados_dolar','Chart Dolar Bar')
    
    ####################################################
    # fazendo as barras para os dados de índice INDV18 #
    ####################################################

    negociacoes = get_negociacoes("Dados Entrada/dados_indice.txt")
    
    # Bloco de código para timebar
    delta_tempo_minutos = 60   # Input do tempo em minutos desejado
    delta_tempo_milissegundos = delta_tempo_minutos * 60 * 1000  # Transformando delta_tempo em milissegundos (3 minutos)
    campo_ativo = "INDV18"
    dados_time_bar = resumo_time(negociacoes, delta_tempo_milissegundos, campo_ativo)
    geracao_de_arquivo(dados_time_bar, "resultados_indice/arquivo_time_bar")
    plot_chart("resultados_indice/arquivo_time_bar.txt", 'resultados_indice','Chart Time Bar')

    # Bloco de código para volumebar
    delta_volume = 10000
    dados_volume_bar = resumo_volume(negociacoes, delta_volume, campo_ativo)
    geracao_de_arquivo(dados_volume_bar, "resultados_indice/arquivo_volume_bar")
    plot_chart("resultados_indice/arquivo_volume_bar.txt", 'resultados_indice','Chart Volume Bar')

    # Bloco de código para dolarbar
    delta_valor = 1000000000
    dados_valor_bar = resumo_dolar(negociacoes, delta_valor, campo_ativo)
    geracao_de_arquivo(dados_valor_bar, "resultados_indice/arquivo_dolar_bar")
    plot_chart("resultados_indice/arquivo_dolar_bar.txt", 'resultados_indice','Chart Dolar Bar')

main()