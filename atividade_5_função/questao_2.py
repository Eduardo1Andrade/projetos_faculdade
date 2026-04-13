numero = 0
numero_inverso = 0
def numero_reverso(numero): #fiz uma leve bruxaria mas ele faz o for normal e pega o numero de -1 até o ultimo iteravel do numero
    str_numero = str(numero)
    str_numero_inverso = ""
    for i in range(0,len(str_numero)):
        str_numero_inverso  = str_numero_inverso + str_numero[-i - 1]
    return int(str_numero_inverso)
numero = int(input("digite um numero: "))
numero_inverso = numero_reverso(numero)
print(f"o inverso desse numero é = {numero_inverso}")