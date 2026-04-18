numero = 0
def sequencia_fribonnaci(numero,numero_principal = 1,numero_secundario = 1): #função de fribonnci com zero não incluso
    if numero_principal >= numero:
        return 0
    numero_temporario = numero_principal
    print(numero_principal)    
    numero_principal += numero_secundario
    numero_secundario = numero_temporario
    sequencia_fribonnaci(numero,numero_principal,numero_secundario)

numero = int(input("digite a sequencia fribonnaci: "))
sequencia_fribonnaci(numero)

    
