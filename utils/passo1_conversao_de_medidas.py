def gms_para_decimal(texto):
    parte = texto.split(".")          

    graus = int(parte[0]) 
    minutos = int(parte[1])
    segundos = int(parte[2])

    return graus + minutos / 60 + segundos / 3600


def decimal_para_gms(graus_decimais):

    graus = int(graus_decimais)                             #gg.xxxx = gg = graus

    minutos_decimais = (graus_decimais - graus) * 60   #gg.xxxx - gg = 00.xxxx * 60x.yyy

    minutos = int(minutos_decimais)                         # 60.yyyy = 60x = min
    segundos = (minutos_decimais - minutos) * 60       # 60x.yyyy - 60x = 00.yyyy * 60 = seg

    return f"{graus}°{minutos}'{segundos:.2f}''"