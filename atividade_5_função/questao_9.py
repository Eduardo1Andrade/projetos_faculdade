prestacao = []
valor_parcela = 1
dia_atraso = 0
def valor_pagemento(valor_parcela,dia_atraso):
    if dia_atraso > 0:
        valor_parcela += ((valor_parcela * 3)/100) + ((valor_parcela /1000) * dia_atraso)
    return valor_parcela
while valor_parcela > 0:
    valor_parcela = float(input("digite o valor atual da parcela: "))
    dia_atraso = int(input("Informe os dias de atraso das parcelas: "))
    if valor_parcela != 0:
        prestacao.append(valor_pagemento(valor_parcela,dia_atraso))
print("prestações pagas:")
for i in range(len(prestacao)):
    print(prestacao[i])