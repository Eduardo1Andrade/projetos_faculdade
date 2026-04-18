numero_temperatura = 0 #vontade grande de escrever celsius_portiolli

action = 0
# C/ 5 = f-32/9

def converter_para_celsius(farenheit): #converte de farenheit para celsius portiolli
    celsius = 5 *((farenheit - 32) /9)
    celsius = round(celsius)
    return celsius #portiolli

def converter_para_farenheit(celsius):# converte de celsius para farenheit
    farenheit = 9 *((celsius + 32) /5)
    farenheit = round(farenheit)
    return farenheit 
def menu():
    action = int(input("Digite sua opção de conversão:\n 1-Celsius para Farenheit\n 2- Farenheit para celsius \n:"))
    if action == 1:
        numero_temperatura = int(input("digite o valor em celsius: "))
        print(converter_para_farenheit(numero_temperatura))
    if action == 2:
        numero_temperatura = int(input("digite o valor em farenheit: "))
        print(converter_para_celsius(numero_temperatura))
menu()