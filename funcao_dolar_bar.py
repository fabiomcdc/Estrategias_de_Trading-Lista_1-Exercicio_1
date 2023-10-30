def resumo_valor(negociacoes, valor_intervalo):
    if not negociacoes:
        return []

    from datetime import datetime, timedelta
    formato = "%Y-%m-%d %H:%M:%S.%f"  # formato necessário para lidar com milissegundos

    resumos = []
    preco_abertura = negociacoes[0][1]
    preco_maximo = preco_abertura
    preco_minimo = preco_abertura
    volume_acumulado = 0
    valor_acumulado = 0
    linha = 0
    num_dia_anterior = 0
    num_dia=0
    
    for negociacao in negociacoes:
        timestamp_str, preco, volume, valor = negociacao
        timestamp = datetime.strptime(timestamp_str, formato)
        preco_maximo = max(preco_maximo, preco)
        preco_minimo = min(preco_minimo, preco)
        valor_acumulado += valor
        volume_acumulado+=volume
        num_dia_anterior = num_dia
        num_dia = timestamp.year + timestamp.month + timestamp.day
        linha=linha+1

        #  Se o dia termina antes do término do intervalo, intervalo é descartado

        if num_dia == num_dia_anterior:
            barras_por_linha = 0
            volume_acumulado_anterior = volume_acumulado - volume
            valor_acumulado_anterior = valor_acumulado - valor
            while valor_acumulado >= valor_intervalo:
                preco_fechamento = preco
                valor_extra = valor_intervalo - valor_acumulado_anterior
                volume_extra = float(int(valor_extra/preco))
                valor_extra = volume_extra*preco
                valor_a_registrar = float(int((valor_acumulado_anterior + valor_extra)*100))/100
                volume_a_registrar = volume_acumulado_anterior + volume_extra
                resumos.append((preco_abertura, preco_minimo, preco_maximo, preco_fechamento, volume_a_registrar, valor_a_registrar))
                indicador_barras_por_linha = "-"+str(barras_por_linha)
                print("Gerando Dolarbar - nova barra finalizada em " + str(linha-1) + indicador_barras_por_linha) # printa quando há uma barra finalizada                
                valor_acumulado = valor_acumulado - valor_a_registrar
                valor_acumulado_anterior = 0
                volume_acumulado = volume_acumulado - volume_a_registrar
                volume_acumulado_anterior = 0
                # Reinicializa as variáveis para o novo intervalo
                barras_por_linha+=1
                preco_abertura = preco
                preco_maximo = preco
                preco_minimo = preco
        else:
            print("novo dia, barra descartada em " + str(linha-1)) # printa quando há troca de dia, antes do intervalo
            valor_acumulado = valor
            volume_acumulado = volume
            preco_abertura = preco
            preco_maximo = preco
            preco_minimo = preco
    return resumos
