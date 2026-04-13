pedidos = []
action = 0
posicao = 0
def cadastrar_pedido():
    pedido = {
        "nome" : input("digite o nome: "),
        "item" : input("digite o nome do item: "),
        "quantidade" : int(input("digite a quantidade: ")),
        "preco_unid" : float(input("digite o preço unitario: "))
    }
    return pedido

def listar_pedidos(pedidos):
    for item in pedidos:
        print(f"item = {item['item']}")
        print(f"quantidade = {item['quantidade']}")
        print(f"preço unitario = {item['preco_unid']}")
        print(f"preço_total = {item['preco_unid'] * item['quantidade']}")

def editar_pedido(pedido):
    pedido['nome'] = input("digite o novo nome: "),
    pedido['item'] = input("digite o nome do item: "),
    pedido['quantidade'] = int(input("digite a quantidade: ")),
    pedido['preco_unid'] = float(input("digite o preço unitario: "))
    return pedido

def remover_pedido(pedidos,posicao):
    pedidos.pop(posicao)

while True:
    action = int(input("Menu:\n 1 - Cadastrar pedido\n2 - Listar pedidos\n3 - Atualizar pedido\n4 - Remover pedido\n5 - Sair\n: "))
    if action == 1:
        pedidos.append(cadastrar_pedido())
        print(pedidos)
    if action == 2:
        listar_pedidos(pedidos)
    if action == 3:
        posicao = int(input("Digite a posição do pedido: "))
        pedidos[posicao] = editar_pedido(pedidos[posicao])
    if action == 4:
        posicao = int(input("digite a posição do pedido: "))
        remover_pedido(pedidos,posicao)
    if action == 5:
        break