print("*********************************")
print("Bem Vindo ao jogo de Adivinhação")
print("*********************************")

numero_secreto = 42

chute_strg = input("Digite o seu numero: ")


print("Você Digitou: ", chute_strg)

chute = int (chute_strg)


acertou = numero_secreto == chute
maior   = chute > numero_secreto
menor   = chute < numero_secreto


if(acertou):
    print("Você acertou")
else:
    if(maior):
        print("Você errou! O Seu chute foi maior que o numero secreto. ")
    elif(menor):
        print("Você errou! O seu chute foi menor do que o numero secreto. ")

print("Final de Jogo")

