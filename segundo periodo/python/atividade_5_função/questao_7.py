numero = 0
def numero_perfeito(numero): #define se um numero é perfeito
    numero_acumulador = 0
    for i in range(1,numero + 1):
        #print(f"entrou no for {i}")
        if numero % i == 0 and i < numero:
            #print(f"foi {i}")
            numero_acumulador += i
    if numero_acumulador == numero:
        return print(f"{numero} é perfeito!!")
    else:
        return 0
def lista_numeros_pefeitos(numero): #lista n numeros perfeitos
    for i in range(numero):
        numero_perfeito(i)

numero = int(input("digite um numero para testar: "))
numero_perfeito(numero)
lista_numeros_pefeitos(numero)    