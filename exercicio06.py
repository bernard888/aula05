pin = 1234
tentativa = 0
mensagem = "acesso negado"
while tentativa <+ 3:
    senha = int(input("Qual a sua senha: "))
    if senha == pin:
        mensagem = "Acesso liberado"
        break
    tentativa += 1
print(mensagem)