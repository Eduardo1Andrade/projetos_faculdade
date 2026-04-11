numero = 0
def e_par(novo_numero):# define se par = True ou impar = False
    if novo_numero % 2 == 0:
        return True
    else:
        return False
    
numero = int(input("Digite um número: "))
print(e_par(numero))
