print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 1:")
while True:
    Nota = float(input("Insira a Nota: "))
    if Nota >= 0 and Nota <= 10:
        print (f"Sua Nota é {Nota}")
        break
    else:
        print ("Insira uma Nota Válida")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 2:")
while True:
    Usuário = str(input("Insira seu Usuário: "))
    Senha = input("Insira sua Senha: ")
    if Usuário != Senha:
        print (f"Sua Conta foi Criada com Sucesso")
        break
    else:
        print ("Usuário não Pode ser Igual à Senha, Insira Dados Válidos")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 3:")
while True:
    Nome = str(input("Digite seu Nome:"))
    if len(Nome) > 3:
        break
    else:
        print("Digite um nome com no mínimo 3 caracteres")

while True:
    idade = int(input("Digite a sua idade: "))
    if idade >= 0 and idade <=150:
        break
    else:
        print("Digite uma idade entre 0 e 150")

while True:
    salario = float(input("Digite seu salário: "))
    if salario > 0:
        break
    else:
        print("Digite um salário maior que 0")

while True:
    sexo = str(input("Digite seu sexo: [M | F]")).upper()

    if len(sexo) == 1:
        if sexo == "M" or sexo == "F":
            break
        else:
            print("Digite um sexo válido ou M ou F")
    else:
        print("Digite apenas uma letra")

while True:
    estado_civil = str(input("Digite seu estado civil: [S | C | V | D]")).upper()

    if len(estado_civil) == 1:
        if estado_civil == "C" or estado_civil == "S" or estado_civil == "V" or estado_civil == "D":
            break
        else:
            print("Digite um estado civil correto.")
    else:
        print("Digite apenas uma letra")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 4:")
População_A = 80000
População_B = 200000
Tempo = 0
while População_A < População_B:
    População_A = População_A * 1.03
    População_B = População_B * 1.015
    Tempo = Tempo + 1
print (População_A, População_B, Tempo)
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 5:")
População_A = int(input('Digite a Densidade Populacional da Cidade A: '))
População_B = int(input('Digite a Densidade Populacional da Cidade B: '))
Taxa_Crescimento_A = float(input('Digite a Taxa de Crescimento Populacional da Cidade A (Número Sem Porcentagem): '))
Taxa_Crescimento_B = float(input('Digite a Taxa de Crescimento Populacional da Cidade B (Número Sem Porcentagem): '))
Tempo = 0
while População_A < População_B:
    População_A = População_A * Taxa_Crescimento_A
    População_B = População_B * Taxa_Crescimento_B
    Tempo = Tempo + 1
print (População_A, População_B, Tempo)
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 6:")
Number = 0
while Number < 21:
    print (Number)
    Number += 1
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 7:")
Bigger = 0
for Number in range(4):
    Number = float(input('Digite Aqui: '))
    if Number >= Bigger:
        Bigger = Number
    else:
        print ('Digite um Número Maior que 0')
print (Bigger)
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 8:")
Soma = 0
for Any in range(1, 6):
    Number = float(input(f'Digite o {Any}º Número: '))
    Soma += Number
print (f'Soma é {Soma}')
Média = Soma / 5
print (f'Média é {Média}')
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 9:")
for Number in range(1, 51):
    if (Number % 2) != 0:
        print (Number)
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 10:")
Número_Inicial = int(input('Digite o 1º Número: '))
Número_Final = int(input('Digite o 2º Número: '))
Intervalo = int(input('Digite o Intervalo: '))
for Number in range(Número_Inicial, Número_Final, Intervalo):
    print (Number)