import math
def propagar_azimutes(azimute_inicial_decimal, angulos_corrigidos):

    azimutes = []
    
    azimute_inicial = azimute_inicial_decimal
    azimutes.append(azimute_inicial)

    # Regras de ajuste dos angulos para mante-los dentro de 0° a 360°
    # Além de corrigir a orientação geométrica do angulo em relação à linha do norte
    for angulo in angulos_corrigidos:
        
        azimute_final_provisorio = (angulo + azimute_inicial)

        if azimute_final_provisorio < 180:
            azimute_final_definitivo = azimute_final_provisorio + 180
        else:
            azimute_final_definitivo = azimute_final_provisorio - 180

        azimute_final_definitivo = azimute_final_definitivo % 360

        azimutes.append(azimute_final_definitivo)

        azimute_inicial = azimute_final_definitivo

    if math.isclose(azimutes[-1], azimutes[0], abs_tol=1e-4):
        print("azimutes fechados com sucesso")
        azimutes.pop()
        return azimutes
    else:
        print("algo deu errado, os azimutes não fecharam")
        return

# A lista dos azimutes tem 1 termo a mais que a lista dos angulos, 
# isso ocorre pois o ultimo angulo é o fechamento.
# O ultimo azimute é exatamente igual ao de partida.
