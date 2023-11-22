print ("-> Questão 1:")
for Número in range (1, 11):
    print (Número)
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 2:")
Lista = []
for Número in range (1, 21):
    if Número % 2 == 0:
        Lista.append(Número)
print (f"Os Números Encontrados Foram {Lista}")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 3:")
Lista = []
for Número in range(1, 20):
    if Número % 2 != 0:
        Lista.append(Número)
print (f"Os Números Encontrados Foram {Lista}")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 4:")
Soma = 0
for Número in range(1, 101):
    Soma += Número
print (f"A Soma dos Números é {Soma}")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 5:")
Soma = 0
for Info in range(1, 11):
    Número = float(input(f"Insira o {Info}º Número: "))
    Soma += Número
    Média = Soma / 10
print (f"A Média dos Números é {Média}")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 6:")
print ("Professor Mandou Passar")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 7:")
Nome = "Lucas"
for Letra in Nome:
    print (Letra)
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 8:")
Texto = str(input("Digite sua Palavra: ")).lower()
Quantidade = 0
Vogais = "aeiou"
for Letra in Texto:
    if Letra in Vogais:
        Quantidade += 1
        print (f"Sua Palavra tem {Quantidade} Vogais")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 9:")
Palavra = str(input("Digite uma Palavra: ")).lower()
Contador = 0

for Letra in Palavra:
    if Letra in "bcdfghjklmnpqrstvxywz":
        Contador += 1

print(f"A palavra {Palavra} possui {Contador} consoantes")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 10:")
Palavra = str(input("Digite uma palavra: ")).strip()

Invertida = Palavra[::-1]

if Palavra == Invertida:
    print(f"{Palavra} é um Palindromo")
else:
    print(f"{Palavra} Não é um Palindromo")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 11:")

print ("------------------------------------------------------------------------------------------------------------------------------")

# Faça um Programa que Pede pro Usuário Digitar uma Senha e Verificar se é uma Senha Forte. 
# Regras: 
# Uma Senha Forte Tem que Contar no Mínimo: 
# 1 Letra Maiuscula
# 1 Letra Minuscula
# 1 Caracter Especial
# 1 Número
# 8 Digitos