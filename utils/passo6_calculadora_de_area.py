
def calculo_da_area(coordenadas):

    n = len(coordenadas)
    soma = 0

    for i in range(len(coordenadas)):
        X1, Y1 = coordenadas[i]
        X2, Y2 = coordenadas [(i + 1) % n] 

        soma += (X1 * Y2 - X2 * Y1)

    area = abs(soma) / 2
    return area

# metodo de gauss A = |(X1Y2 + X2Y3 + Xn Yn+1)| / 2