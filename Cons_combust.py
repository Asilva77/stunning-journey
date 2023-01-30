def calcula_consumo(distancia, combustivel):
    consumo = round (distancia / (combustivel*1), 3)
    
    return consumo

distancia_percorrida = float(input("Informe a distância percorrida (em km): "))
combustivel_usado = float(input("Informe a quantidade de combustível usado (em litros): "))

consumo = calcula_consumo(distancia_percorrida, combustivel_usado)
print("O consumo de combustível é de", consumo, "km/l")