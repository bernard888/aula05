n1 = float(input("digite o primeiro valor: "))
n2 = float(input("digite o segundo valor: "))
while n2 <= 0:
    n2 = float(input("digite outro valor que não seja zero: "))
divisao = n1/n2
print(divisao)