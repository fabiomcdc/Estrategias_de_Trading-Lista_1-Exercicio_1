def resumo_time(negociacoes, delta_tempo_milissegundos, campo_ativo):
    if not negociacoes:
        return []

    from datetime import datetime, timedelta
    formato = "%Y-%m-%d %H:%M:%S.%f"  # formato necessário para lidar com milissegundos
    inicio_intervalo = datetime.strptime(negociacoes[0][0], formato)
    final_intervalo = inicio_intervalo + timedelta(milliseconds=delta_tempo_milissegundos)

    resumos = []
    preco_abertura = negociacoes[0][1]
    preco_maximo = preco_abertura
    preco_minimo = preco_abertura
    volume_total = 0
    linha = 0
    num_dia_anterior = 0
    num_dia=0

    for negociacao in negociacoes:
        timestamp_str, ativo, preco, volume, valor = negociacao
        if ativo == campo_ativo:
            timestamp = datetime.strptime(timestamp_str, formato)
            num_dia_anterior = num_dia
            num_dia = timestamp.year + timestamp.month + timestamp.day
            linha=linha+1

            #  Se o dia termina antes do término do intervalo, intervalo é descartado

            if num_dia == num_dia_anterior:
                if timestamp < final_intervalo:
                    preco_maximo = max(preco_maximo, preco)
                    preco_minimo = min(preco_minimo, preco)
                    volume_total += volume
                else:
                    preco_fechamento = negociacoes[negociacoes.index(negociacao)-1][2]
                    formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
                    resumos.append((formatted_timestamp, preco_abertura,preco_maximo, preco_minimo, preco_fechamento, volume_total))
                    print("Gerando Timebar - nova barra finalizada em "+str(linha-1))
                    while timestamp >= final_intervalo:
                        inicio_intervalo += timedelta(milliseconds=delta_tempo_milissegundos)
                        final_intervalo += timedelta(milliseconds=delta_tempo_milissegundos)

                    preco_abertura = preco
                    preco_maximo = preco
                    preco_minimo = preco
                    volume_total = volume
            else:
                print("novo dia, barra descartada em " + str(linha-1)) # printa quando há troca de dia, antes do intervalo
                inicio_intervalo = timestamp
                final_intervalo = timestamp + timedelta(milliseconds=delta_tempo_milissegundos)
                preco_abertura = preco
                preco_maximo = preco
                preco_minimo = preco
                volume_total = volume

    preco_fechamento = negociacoes[-1][1]
    print("ultima barra")


    resumos.append(( ))

    return resumos