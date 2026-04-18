linha = 0
coluna = 0
def desenhar_retangulo(linha = 5,coluna = 20): #faz o retangulo 
    i = 0
    str_coluna = "+"  #adiciona os valores inicias
    str_linha = "|"
    for i in range(coluna): #monta a string da base do retangulo
        str_coluna += "-"
    str_coluna += "+"
    for i in range(coluna): #monta a string da altura do retangulo
        str_linha += " "
    str_linha +="|"
    
    print(str_coluna) #mostra o retangulo
    for i in range(linha):
        print(str_linha)
    print(str_coluna)

    return 0
desenhar_retangulo()