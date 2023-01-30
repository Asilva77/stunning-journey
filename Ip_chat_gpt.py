def calcula_imc(peso, altura):
    imc = round(peso / (altura ** 2), 3)
    return imc

peso = float(input("Insira o seu peso em kg: "))
altura = float(input("Insira sua altura em metros: "))

resultado = calcula_imc(peso, altura)
if resultado >= 30:
    print("Seu IMC é: ", resultado," VOCÊ ESTÁ GORDO!")
else:
    print("Seu IMC é: ", resultado," VOCÊ ESTÁ EM FORMA!")