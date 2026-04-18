hora = 0
minuto = 0 #to considerando que o tapado do usuario não vai digitar 48 por exemplo
hora_convertida = ""
action = 0
def conversor_hora(hora): #converte as horas de 23 para 12
    if hora == 24:
        hora = 0
        return hora
    elif hora > 12 :
        hora -= 12
        return hora
    elif hora == 24:
        hora = 0
        return hora
    else: 
        return hora
def divisor_ciclo(hora): #diz se é A.M ou P.M
    if hora > 12:
        return "P"
    else:
        return "A"
while True: 
    hora = int(input("digite a hora: "))
    minuto = int(input("digite o valor de minutos: "))
    if hora < 0 or hora > 24 or minuto < 0 or minuto > 60: # garante que o enzo não vai digitar 120 minutos
        print("hora ou minuto invalida")
        continue
    if minuto > 10:
        hora_convertida = str(conversor_hora(hora)) + ":" + str(minuto) + " " + divisor_ciclo(hora) + ".M"
    else: 
        hora_convertida = str(conversor_hora(hora)) + ":0" + str(minuto)+ " " + divisor_ciclo(hora) + ".M"
    print(f"hora convertida = {hora_convertida}")
    action = int(input("Deseja Sair?:[1]"))
    if action == 1:
        break