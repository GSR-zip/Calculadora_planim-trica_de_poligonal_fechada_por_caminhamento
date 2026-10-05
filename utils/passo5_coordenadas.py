import math

# coordenadas provisórias utilizadas para encontrar o erro de fechamento linear (referente as distâncias)
def coordenadas_provisorias(distancias, azimutes):

    delta_x_provisorio = []
    delta_y_provisorio = []

    for valor_n, (ditancia, azimute) in enumerate(zip(distancias, azimutes)):
        azimute_radianos = math.radians(azimute) 

        #∆x/∆y = distancia * sen/cos * azimute  
        variacao_de_x = ditancia * math.sin(azimute_radianos)
        variacao_de_y = ditancia * math.cos(azimute_radianos)

        print(f"∆X provisorio{valor_n}: {variacao_de_x}\n∆Y provisorio{valor_n}: {variacao_de_y}")
        delta_x_provisorio.append(variacao_de_x)
        delta_y_provisorio.append(variacao_de_y)


    return delta_x_provisorio, delta_y_provisorio

# soma as coordenadas provisórias, com elas é possivel observar o quanto o ponto final difere do inicial (o erro de fechamento)
def calculo_do_erro_linear(delta_x_provisorio, delta_y_provisorio):
    erro_linear_x = sum(delta_x_provisorio)
    erro_linear_y = sum(delta_y_provisorio)
    erro_linear_total = ((erro_linear_x) ** 2 + (erro_linear_y) ** 2) ** (1/2)

    return erro_linear_total, erro_linear_x, erro_linear_y


# atualiza a tabela das coordenadas provisórias corrigindo-as
def correcao_linear(distancias, perimetro, delta_x_provisorio, delta_y_provisorio, erro_linear_x, erro_linear_y):

    x_inicial = float(input("qual a coordenada X inicial?: "))
    y_inicial = float(input("qual a coordenada Y inicial?: "))

    x_partida = x_inicial
    y_partida = y_inicial

    coordenadas_finais_x = []
    coordenadas_finais_y = []

    for n, (ditancia) in enumerate(distancias):
        correcao_x = - (ditancia / perimetro) * (erro_linear_x)
        delta_x_provisorio[n] = delta_x_provisorio[n] + correcao_x

        correcao_y = - (ditancia / perimetro) * (erro_linear_y)
        delta_y_provisorio[n] = delta_y_provisorio[n] + correcao_y

    for x, y in zip(delta_x_provisorio, delta_y_provisorio):
        coordenada_x = x_partida + x
        coordenada_y = y_partida + y

        coordenadas_finais_x.append(coordenada_x)
        coordenadas_finais_y.append(coordenada_y)

        x_partida = coordenada_x
        y_partida = coordenada_y

    for i, (x, y) in enumerate(zip(coordenadas_finais_x, coordenadas_finais_y)):
        print(f"coordendas finais de x{i + 1}: {x:.3f}")
        print(f"coordendas finais de y{i + 1}: {y:.3f}")

    return coordenadas_finais_x, coordenadas_finais_y

