nome = ""
sobrenome = ""
email = ""
def gerar_email(valor_nome,valor_sobrenome): #gera o email e o torna minusuculo
    novo_email = valor_nome + "." + valor_sobrenome + "@escola.com"
    novo_email = novo_email.lower()
    return novo_email
nome = input("Digite seu nome: ")
sobrenome = input("digite seu sobrenome: ")
email = gerar_email(nome,sobrenome) #chama a função
print(email)