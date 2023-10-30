# Estrategia_de_Trading-Produzindo_Bars
Local onde serão colocados os programas relacionados a matéria do Mestrado de Economia da FGV
Esses programas visam produzir Timebars, Volumebars, e Dolarbars a partir de um arquivo chamado dados.txt localizado no folder raiz que contém as cotações de uma Ativo, “tic by tic”.

Para cada tipo de barra, foi usado um procedimento em separado:
- funcao_time_bar para Timebars
- funcao_volume_bar para Volumebars
- funcao_dolar_bar para Dolarbars

Essas funções são chamadas por um programa chamado gerar_arquivo_resultados que prepara a base através do comando negociacoes = get_negociacoes().

Em seguida, chama as funções de geração das barras.

Os parâmetros para as barras podem ser definidas pelas variáveis delta_tempo_minutos, delta_volume  e delta_valor. Os valores que estão programados inicialmente são 120 minutos, 10000 contratos e 10 milhões de valor.

Em todas as gerações das barras, tomei o cuidado para tratar o caso de a construção da barra ser interrompida pelo fim do dia. Caso isso aconteça, o intervalo que estava sendo gerado é descartado.

Os prints do console dão indicações do que está ocorrendo e os casos em que uma barra é descartada.

Outro cuidado que tomei foi quando o volume de uma barra atingia o valor do intervalo no meio de um “tic”. Quando isso acontecia, quebrava o “tic” até o volume ser atingido, guardando o saldo como se fosse um “tic” adicional.

No caso do Dolarbar, quando o volume do “tic” era tal que estouraria o valor do intervalor, quebrava o “tic” até o volume que não estourava o intervalo, guardando o saldo de volume e valor como se fosse um novo “tic” a ser considerado.

Em todos os cenários, foi feito um comparativo com uma versão resumida com 100 mil linhas em excel chamada “Planilha de Verificação” para verificar os valores encontrados. Foi ótimo fazer isso pois permitiu encontrar diversos problemas. Também ficou claro que fazer em excel foi mais difícil do que em Python.
