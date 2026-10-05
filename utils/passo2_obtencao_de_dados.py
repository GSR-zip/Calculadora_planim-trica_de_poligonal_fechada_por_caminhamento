from utils.passo1_conversao_de_medidas import gms_para_decimal

#obtenção de dados: ângulos, distâncias e tolerancias

#--------------------------------- Escolha do modo de operação --------------------------------
def escolher_opcao():
    while True:

        opcao = input("1 = importar\n2 = digitar manualmente\nescolha: ")
    
        if opcao == "1":
            print("voce escolheu importar!\ninforme os ângulos e distâncias dentro desta estrutura -> gg°mm'ss''; distância respeitando os caracteres ")
            break
        elif opcao == "2":
            print("você escolheu digitar no terminal!\ninforme os ângulos dentro desta estrutura -> gg.mm.ss e na sequência as distâncias")
            break
        else:
            print("opção não identificada")
    
    return opcao


#--------------------------------------- Obtenção dos dados ------------------------------------
def importar_dados(opcao):

    tabela_de_angulos = []
    tabela_de_distancias = []
    dados = []

    def salvar_angulos_e_distancias(angulo,distancia):
        tabela_de_angulos.append(angulo)
        tabela_de_distancias.append(distancia)

    #---------------------------- Obtenção dos dados por copia e cola --------------------------

    if opcao == "1":

        importacao = input("cole as informações de ângulos e distâncias na mesma linha: ")
        dados.extend(importacao.split())

        #conversão de cada termo (angulo e distância) para a sua devida lista
        for n in dados:
            if ";" in n:
                try:
                    parte = n.split(";")
                    angulo = gms_para_decimal(parte[0])
                    distancia = float(parte[1])

                    salvar_angulos_e_distancias(angulo, distancia)
                except:
                    print(f"erro no valor do dado {n}, verifique a digitação do mesmo ")

    #----------------------------- Obtenção dos dados manualmente ------------------------------
    elif opcao == "2":

        while True:
            angulo_informado_manualmente = input(f"angulo {len(tabela_de_angulos) + 1 }: ")
            if angulo_informado_manualmente == "":
                break

            angulo = gms_para_decimal(angulo_informado_manualmente)
            distancia = float(input(f"distância {len(tabela_de_angulos) + 1 }: "))

            salvar_angulos_e_distancias(angulo, distancia) 

        print(f"foram inseridas {len(tabela_de_angulos)} estações")

    if len(tabela_de_angulos) < 3:
        print("falta dados para formar uma poligonal")
        return [], []

    numero_de_estacoes = len(tabela_de_angulos)

    return tabela_de_angulos, tabela_de_distancias, numero_de_estacoes

def tolerancia_linear(perimetro):

    entrada = input("qual a tolerancia linear da medição?\nx/xxx: ")
    parte = entrada.split("/")
    numerador = int(parte[0]) 
    denominador = int(parte[1])
    tol_linear = (numerador / denominador) * perimetro
    
    return tol_linear