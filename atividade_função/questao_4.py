notas = []
nota = 0
status_aluno = ""
for i in range(3): #recebe as 3 notas
    nota = int(input(f"digite a nota{i+1}: "))
    notas.append(nota)

def situacao_aluno(nota1,nota2,nota3): #faz o calculo da média
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
status_aluno = situacao_aluno(notas[0],notas[1],notas[2]) #chama a função
print(status_aluno) #saida