idade = 0
dias = 0
def dias_de_vida (qtr_ano): #calcula a quantidade de dias
    global dias
    dias = qtr_ano * 365
    return dias
idade = int(input("digite quantos anos possui: "))
dias_de_vida(idade) #chama a função
print(dias) #mostra a quandidade de dias
