def resumo_volume(negociacoes, volume_intervalo, campo_ativo):
    if not negociacoes:
        return []

    from datetime import datetime, timedelta
    formato = "%Y-%m-%d %H:%M:%S.%f"  # formato necessário para lidar com milissegundos

    resumos = []
    preco_abertura = negociacoes[0][2]
    preco_maximo = preco_abertura
    preco_minimo = preco_abertura
    volume_acumulado = 0
    linha = 0
    num_dia_anterior = 0
    num_dia=0
    
    for negociacao in negociacoes:
        timestamp_str, ativo, preco, volume, valor = negociacao
        if ativo == campo_ativo:
            timestamp = datetime.strptime(timestamp_str, formato)
            preco_maximo = max(preco_maximo, preco)
            preco_minimo = min(preco_minimo, preco)
            volume_acumulado += volume
            num_dia_anterior = num_dia
            num_dia = timestamp.year + timestamp.month + timestamp.day
            linha=linha+1

            #  Se o dia termina antes do término do intervalo, intervalo é descartado

            if num_dia == num_dia_anterior:
                barras_por_linha = 0
                while volume_acumulado >= volume_intervalo:
                    preco_fechamento = preco
                    formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
                    resumos.append((formatted_timestamp, preco_abertura, preco_maximo, preco_minimo, preco_fechamento, volume_intervalo))
                    indcador_barras_por_linha = "-"+str(barras_por_linha)
                    print("Gerando Volumebar - nova barra finalizada em " + str(linha-1) + indcador_barras_por_linha) # printa quando há uma barra finalizada
                    # Reinicializa as variáveis para o novo intervalo
                    barras_por_linha+=1
                    preco_abertura = preco
                    preco_maximo = preco
                    preco_minimo = preco
                    volume_acumulado = volume_acumulado - volume_intervalo
            else:
                print("novo dia, barra descartada em " + str(linha-1)) # printa quando há troca de dia, antes do intervalo
                volume_acumulado = volume
                preco_abertura = preco
                preco_maximo = preco
                preco_minimo = preco
    return resumos