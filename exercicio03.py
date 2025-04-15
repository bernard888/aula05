qnota = 0
soma = 0
while qnota < 3:
    nota = float(input(f"digite {qnota+1}º um valor: "))
    soma += nota
    qnota += 1

print(f"{soma/3}")
