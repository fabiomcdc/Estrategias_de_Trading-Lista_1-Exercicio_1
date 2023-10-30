from funcao_time_bar import resumo_intervalo
from funcao_volume_bar import resumo_volume
from funcao_dolar_bar import resumo_valor

def parse_negociacao(linha):
    campos = linha.split(';')
    timestamp = campos[0]  # Data-Hora
    preco = float(campos[3].replace(',', '.'))  # Preço do Negócio
    volume = int(campos[4].replace(',', '.'))   # Quantidade Negociada
    valor_reais = preco*volume  # Valor em reais negociado
    return timestamp, preco, volume, valor_reais

def get_negociacoes():
    with open("dados.txt", "r") as file:
        linhas = file.readlines()[0:]
        return [parse_negociacao(linha) for linha in linhas]
            
def geracao_de_arquivo(lista, nome_do_arquivo):
    with open(f"resultados/{nome_do_arquivo}.txt", "w") as arquivo:
        for item in lista:
            line = ";".join(map(str, item))
            arquivo.write(line + "\n")
    return

def main():
    negociacoes = get_negociacoes()
    
    # Bloco de código para timebar
    delta_tempo_minutos = 120   # Input do tempo em minutos desejado
    delta_tempo_milissegundos = delta_tempo_minutos * 60 * 1000  # Transformando delta_tempo em milissegundos (3 minutos)
    dados_time_bar = resumo_intervalo(negociacoes, delta_tempo_milissegundos)
    geracao_de_arquivo(dados_time_bar, "arquivo_time_bar")

    # Bloco de código para volumebar
    delta_volume = 10000
    dados_volume_bar = resumo_volume(negociacoes, delta_volume)
    geracao_de_arquivo(dados_volume_bar, "arquivo_volume_bar")

    # Bloco de código para dolarbar
    delta_valor = 10000000
    dados_valor_bar = resumo_valor(negociacoes, delta_valor)
    geracao_de_arquivo(dados_valor_bar, "arquivo_dolar_bar")
main()