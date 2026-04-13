numero = 0
qtr_digitos = 0
def quantidade_digito(numero): # calcula a quantidade de digito sem usar string :D
    qtr_digito = 0
    while numero > 1:
        if numero % 10 == 0:
            numero = (numero + 1)/10
        else:
            numero = numero/10
        qtr_digito += 1
    return qtr_digito
numero = int(input("digite um numero: "))
qtr_digitos = quantidade_digito(numero)
print(f"Quantidade de números é : {qtr_digitos}")