def calculo_erro_angular(lista_dos_angulos, numero_de_estacoes):

    somatorio_dos_angulos_medidos = sum(lista_dos_angulos)

    # Calculo do erro = (teórico - medido)
    # Teórico = (número de estações +- 2) * 180

    while True:
        opcao = input("os angulos medidos são internos ou externos?\n1 = externos\n2 = interno\nescolha: ")

        if opcao == "1":
            medicao_por_angulos_externos = (numero_de_estacoes + 2) * 180
            erro_angular = somatorio_dos_angulos_medidos - medicao_por_angulos_externos
            return erro_angular
        elif opcao == "2":
            medicao_por_angulos_internos = (numero_de_estacoes - 2) * 180
            erro_angular = somatorio_dos_angulos_medidos - medicao_por_angulos_internos 
            return erro_angular
        else:
            print("nenhuma opção valida encontrada")
            
    

def tolerancia_angular(estacoes, tol_aparelho,  erro_de_fechamento_angular):

    #tolerancia angular = tolerancia do aparelho * √ numero de estações
    tol_angular = tol_aparelho * (estacoes ** (1/2))

    if abs( erro_de_fechamento_angular) <= tol_angular:
        print ("erro dentro da tolerância")
        return True
    else:
        print("erro fora de tolerância")
        return False

def compensacao_angular(erro_de_fechamento_angular, estacoes, lista_dos_angulos):
    correcao = - ( erro_de_fechamento_angular / estacoes)

    angulos_corrigidos = []

    for angulo in lista_dos_angulos:
        c = correcao + angulo

        angulos_corrigidos.append(c)

    return angulos_corrigidos