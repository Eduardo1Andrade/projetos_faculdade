lista_mes = ("Janeiro", "Fevereiro", "Março", "Abril",
"Maio", "Junho", "Julho", "Agosto","Setembro", 
"Outubro", "Novembro", "Dezembro")
data = ""
dia_valor = 0
mes_valor = 0
ano_valor = 0

def mes_por_extenso(mes_numero): #retorna o mês por extenso
    global lista_mes
    return str(lista_mes[mes_numero - 1])
dia_valor = int(input("Digite o numero do dia: ")) 
mes_valor = int(input("Digite o número do mês: ")) 
ano_valor = int(input("Digite o número do ano: "))
data = str(dia_valor) + "/" + mes_por_extenso(mes_valor) + "/" + str(ano_valor)
print(data)