import math

#função para converter angulos do sistema sexagonal para decimal

def GMS_P_decimal(texto):
    part = texto.split(".")          

    graus = int(part[0]) 
    minutos = int(part[1])
    segundos = int(part[2])

    return graus + minutos / 60 + segundos / 3600

#obtenção de dados: ângulos e distâncias

print("este programa calcula a correção de ângulos de uma poligonal fechada")
K = GMS_P_decimal(input( "antes de tudo qual a tolerânca do aparelho?\nsiga a ordem gg.mm.ss: " ))

#escolha do modo de operação
while True:

    opcao = input("certo, gostaria de importar dos dados ou escreve-lo no terminal?\n1 = importar\n2 = digitar manualmente\nescolha: ")
    
    if opcao == "1":
        print("voce escolheu importar!\ninforme os ângulos dentro desta estrutura -> gg.mm.ss;dist respeitando os caracteres ")
        break
    elif opcao == "2":
        print("você escolheu digitar no terminal!\ninforme os ângulos dentro desta estrutura -> gg.mm.ss e na sequência as distâncias")
        break
    else:
        print("opção não identificada")

#tabelas
tabela_ang = []
tabela_dist = []
dados = []

#obtenção dos dados por copia e cola
if opcao == "1":
    #obtenção dos dados 
    while True:
        importacao = input("cole as informações de ângulos e distâncias na mesma linha: ")  #cria a string importacao com toda a informação bagunçada
        if importacao == "":
            break                                       #sai do loop pois o usuário digitou certo

        dados.extend(importacao.split())                # procura espaços dentro da string importação, os separa por split (criando uma nova lista) e adiciona os itens dessa lista para dentro da lista "dados"

    #conversão de cada um para a sua devida lista
    for n in dados:                                     # faz a varredura na lista dados 
        if ";" in n:                                    # procura ";" na lista dados      
            parte = n.split(";")                       # separa os itens da lista dados em duas partes antes de ";" e depois
            angulo = GMS_P_decimal(parte[0])         # lê a primeira parte e aplica a função grua minutos e segundos para decimal e chama de angulo
            distancia = float(parte[1])                 # lê a segunda parte e chama de distância 

            tabela_ang.append(angulo)                       # adiciona o que foi chamado de angulo na lista "tabela_ang"
            tabela_dist.append(distancia)                   # adiciona o que foi distância de angulo na lista "tabela_dist"

# obtenção dos dados manualmente
elif opcao == "2":
    #obtenção de dados
    while True:
        ang_txt = input(f"angulo {len(tabela_ang) + 1 }: ")
        if ang_txt == "":
            break

        angulo = GMS_P_decimal(ang_txt)
        distancia = float(input(f"distância {len(tabela_ang) + 1 }: "))
        
        tabela_ang.append(angulo)
        tabela_dist.append(distancia)

    print(f"foram inseridas {len(tabela_ang)} estações")

if len(tabela_ang) < 3:                                 #verifica se é uma polional válida
    quit("falta dados para formar uma poligonal")



#soma dos angulos 
somatorio_angs = sum(tabela_ang)

#calculo do erro (teórico - calculado) * 180

while True:
    opcao2 = input("os angulos medidos são internos ou externos?\n1 = externos\n2 = interno\nescolha: ")

    if opcao2 == "1":
        externa = (len(tabela_ang) + 2) * 180
        erro_ang = somatorio_angs - externa
        break
    elif opcao2 == "2":
        interna = (len(tabela_ang) - 2) * 180
        erro_ang = somatorio_angs - interna 
        break
    else:
        print("nenhuma opção valida encontrada")

#tolerância
T = K * len(tabela_ang) ** (1/2)
if abs(erro_ang) <= T:
    print("erro dentro da tolerância")
else:
    print("erro fora de tolerância")
    quit("retorne ao campo e tire as medidas novamente")

correcao = - (erro_ang / len(tabela_ang))

tabela_ang_corrigida = []

for angulo in tabela_ang:
    c = correcao + angulo

    tabela_ang_corrigida.append(c)

print(tabela_ang_corrigida)

azimutes = []

azz = (input("qual o azimute inicial? (em gg.mm.ss): "))
azi = GMS_P_decimal(azz)
azimutes.append(azi)

for x in tabela_ang_corrigida:
    
    azf = (x + azi)

    if azf < 180:
        azfc = azf + 180
    else:
        azfc = azf - 180
    if azfc >= 360:
        azfc -= 360

    azimutes.append(azfc)

    azi = azfc

print(azimutes)


tol_lin = input("qual a tolerancia linear da medição? x/xxx: ")
ç = tol_lin.split("/")
num = int(ç[0]) 
deno = int(ç[1])
TL = num / deno

Xi = float(input("qual a coordenada X inicial?: "))
Yi = float(input("qual a coordenada Y inicial?: "))

X_partida = Xi
Y_partida = Yi

Delta_X = []
Delta_Y = []

coordenadas_x = []
coordenadas_y = []

P = sum(tabela_dist)

for d, az in zip(tabela_dist, azimutes):
    az_rad = math.radians(az)
    Δx = d * math.sin(az_rad) 
    Δy = d * math.cos(az_rad) 

    Delta_X.append(Δx)
    Delta_Y.append(Δy)

erro_x = sum(Delta_X)
erro_y = sum(Delta_Y)

for c, (d, Δx, Δy) in enumerate(zip(tabela_dist, Delta_X, Delta_Y)):
    correcao_x = - (d/P) * (erro_x)
    Delta_X[c] = Delta_X[c] + correcao_x

    correcao_y = - (d/P) * (erro_y)
    Delta_Y[c] = Delta_Y[c] + correcao_y

for x, y in zip(Delta_X, Delta_Y):
    CFx = X_partida + x
    CFy = Y_partida + y

    coordenadas_x.append(CFx)
    coordenadas_y.append(CFy)

    X_partida = CFx
    Y_partida = CFy

for i, (x, y) in enumerate(zip(coordenadas_x, coordenadas_y)):
    print(f"coordendas finais de x{i + 1}: {x:.3f}")
    print(f"coordendas finais de y{i + 1}: {y:.3f}")






'''
print("Número de estações:", len(tabela_ang))
print("Soma observada:", somatorio_angs)
print("Soma teórica:", externa)
print("Soma teórica:", interna)
print("Erro angular:", erro_ang)
print("Tolerância:", T)

215.32.00;56.57 288.54.00;60.83 287.06.00;60.75 142.07.00;44.72 326.19.00;51.01


301.29.03;100.18 246.47.25;115.80 261.29.34;116.68 301.45.11;91.65 148.28.31;89.06 
'''