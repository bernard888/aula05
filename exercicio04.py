qnotas = 0
notaf = 0
nalunos = int(input("digite o número de alunos: "))
print(" ")
while qnotas < nalunos:
    nota = float(input(f"Digite a nota do {qnotas+1}º aluno: "))
    notaf += nota
    qnotas += 1
media = notaf/ nalunos
print(" ")
print(f"A média da classe é: {media:.2f}")