
from utils.passo1_conversao_de_medidas import gms_para_decimal, decimal_para_gms
from utils.passo2_obtencao_de_dados import escolher_opcao, importar_dados, tolerancia_linear
from utils.passo3_tratamento_dos_angulos import calculo_erro_angular, tolerancia_angular, compensacao_angular
from utils.passo4_azimutes import propagar_azimutes
from utils.passo5_coordenadas import coordenadas_provisorias, calculo_do_erro_linear, correcao_linear
from utils.passo6_calculadora_de_area import calculo_da_area

#================================================>>>>>>>>>> φ <<<<<<<<<<================================================
#================================================== Obtenção de dados: =================================================
def fornecer_dados():
    opcao = escolher_opcao()
    resultado = importar_dados(opcao)

    if not resultado or not resultado [0]:
        print("os dados não foram inseridos corretamente ")
        return None
    
    lista_dos_angulos, lista_das_distancias, numero_de_estacoes = resultado
    
    tol_aparelho = gms_para_decimal(input( "antes de tudo qual a tolerânca do aparelho?\nsiga a ordem gg.mm.ss: " ))

    print(f"Ângulos: {lista_dos_angulos}\n distâncias: {lista_das_distancias}\n estações: {numero_de_estacoes}")
    print(tol_aparelho) 
   
    return lista_dos_angulos, lista_das_distancias, numero_de_estacoes, tol_aparelho

#================================================ Tratamento dos ângulos ===============================================
def verificar_tolerancia_angular(lista_dos_angulos, numero_de_estacoes):
    erro_de_fechamento_angular = calculo_erro_angular(lista_dos_angulos, numero_de_estacoes)

    return erro_de_fechamento_angular

def corrigir_angulos(erro_de_fechamento_angular, estacoes, lista_dos_angulos):
    angulos_corrigidos = compensacao_angular(erro_de_fechamento_angular, estacoes, lista_dos_angulos)

    return angulos_corrigidos

#======================================================= Azimutes ======================================================

def tratamento_dos_azimutes(azimute_inicial_fornecido, angulos_corrigidos):
    azimutes = propagar_azimutes(azimute_inicial_fornecido, angulos_corrigidos)

    return azimutes

#===================================================== Coordenadas =====================================================
def x_y_provisorios(distancias, azimutes):
    delta_x_provisorio, delta_y_provisorio = coordenadas_provisorias(distancias, azimutes)

    return delta_x_provisorio, delta_y_provisorio

def erro_linear(delta_x_provisorio, delta_y_provisorio):

    return calculo_do_erro_linear (delta_x_provisorio, delta_y_provisorio)
     
def tol_linear(erro_linear_total, tol_linear_medicao):

    if erro_linear_total <= tol_linear_medicao:
        print ("erro dentro da tolerância")
        return True
    else:
        print("erro fora da tolerancia")
        return False

def coordenadas_finais(
        distancias,
        perimetro, 
        delta_x_provisorio, 
        delta_y_provisorio, 
        erro_linear_x, 
        erro_linear_y
    ):
    coordenadas_finais_x, coordenadas_finais_y = correcao_linear(
        distancias,
        perimetro, 
        delta_x_provisorio, 
        delta_y_provisorio, 
        erro_linear_x, 
        erro_linear_y
    )
    return coordenadas_finais_x, coordenadas_finais_y


#======================================== FUNÇÃO PRINCIPAL DA POLIGONAL FECHADA ========================================

def main():

    # --------------------------->>>>>> fornece as informações iniciais para o cálculo <<<<<<---------------------------
    dados= fornecer_dados() 

    if dados is None:
        return 

    angulos, distancias, estacoes, tol_aparelho = dados
    erro_de_fechamento_angular = verificar_tolerancia_angular(angulos, estacoes)
    perimetro = sum(distancias)
    azimute_inicial_fornecido = gms_para_decimal(input("qual o azimute inicial? (em gg.mm.ss): "))
    tol_linear_medicao = tolerancia_linear(perimetro)

    # ------------------>>>>>> Apenas para fornecer o erro em números hexadecimais (xx°xx'xx'') <<<<<<------------------
    erro_de_fechamento_angular_gms = decimal_para_gms(erro_de_fechamento_angular) 
    print(erro_de_fechamento_angular_gms)

    # ------------------------>>>>>> Verifica se o erro de fechamento angular é tolerável <<<<<<------------------------
    dentro_da_tol_angular = tolerancia_angular(estacoes, tol_aparelho, erro_de_fechamento_angular)
    if not dentro_da_tol_angular:
        return 
    
    print(dentro_da_tol_angular)
  
    # ---------------->>>>>> Corrige o erro de fechamento angular e retorna os angulos corrigidos <<<<<<----------------
    angulos_corrigidos = corrigir_angulos(erro_de_fechamento_angular, estacoes, angulos) 
    for n_angulo, angulo in enumerate(angulos_corrigidos):
        angulo_correto_gms = decimal_para_gms(angulo)
        print (f"angulo {n_angulo} corrigido: {angulo_correto_gms}")

    # ------------------------------->>>>>> Propaga o azimute pelos demais ângulos <<<<<<-------------------------------
    azimutes = tratamento_dos_azimutes(azimute_inicial_fornecido ,angulos_corrigidos)
    for n_azimute, azimute in enumerate(azimutes):
        azimute_gms = decimal_para_gms(azimute)
        print (f"azimute {n_azimute}: {azimute_gms}")

    # ------------------------->>>>>> Calcula as coordenadas provisórias e o erro angular <<<<<<------------------------
    delta_x_provisorio, delta_y_provisorio = x_y_provisorios(distancias, azimutes)

    erro_linear_total, erro_linear_x, erro_linear_y = erro_linear(delta_x_provisorio, delta_y_provisorio)
    dentro_da_tol_linear = tol_linear(erro_linear_total, tol_linear_medicao)
    if not dentro_da_tol_linear:
        return

    coordenadas_finais_x, coordenadas_finais_y = coordenadas_finais(
        distancias,
        perimetro, 
        delta_x_provisorio, 
        delta_y_provisorio, 
        erro_linear_x, 
        erro_linear_y
    )

    for i, (x, y) in enumerate(zip(coordenadas_finais_x, coordenadas_finais_y)):
        print(f"coordendas finais de x{i + 1}: {x:.3f}")
        print(f"coordendas finais de y{i + 1}: {y:.3f}")

    coordenadas = list(zip(coordenadas_finais_x, coordenadas_finais_y))
    area = calculo_da_area(coordenadas)
    print (f"area = {area}")


if __name__ == "__main__":
    main()