preco = 0
desconto = 0 # em %
def aplicar_desconto(valor_produto,valor_desconto):#calcula o desconto
    novo_preco = valor_produto - ((valor_produto * valor_desconto)/100)
    return novo_preco
preco = int(input("digite o preço do protudo: "))
desconto = int(input("digite o desconto do protudo: "))
preco = aplicar_desconto(preco,desconto)#chama a função
print(preco) #exibe o novo preço