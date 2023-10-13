print ("-> Questão 1:")
Número_1 = int(input("Número 1: "))
Número_2 = int(input("Número 2: "))
print ("Bem Vindo!")
if Número_1 == Número_2:
    print ("São Iguais")
elif Número_1 > Número_2:
    print (f"{Número_1} é Maior que {Número_2}")
else:
    print (f"{Número_1} é Menor que {Número_2}")
print ("Tchau!")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 2:")
Number = int(input("Your Number: "))
if Number > 0:
    print ("Your Number is Positive")
elif Number < 0:
    print ("Your Number is Negative")
else:
    print ("Your Number is Neutral")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 3:")
Sexo = str(input("Digite a Letra do seu Sexo: ")).upper()
if Sexo in "FM":
    if Sexo == "F":
        print ("Seu Gênero é Feminino")
    else:
        print ("Seu Gênero é Masculino")
else:
    print ("Erro! Verifique a Informação Inserida. Caso seu Gênero não Esteja Cadastrado Entre em Contato com o Suporte.")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 4:")
Letra = str(input("Digite a Letra: ")).lower()
if len(Letra) == 1:
    if Letra in "aeiou":
        print ("Sua Letra é uma Vogal")
    else:
        print ("Sua Letra é uma Consoante")
else:
    print ("Digite Apenas Uma Letra, Por Gentileza.")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 5:")
Nota_1 = float(input("Nota 1: "))
Nota_2 = float(input("Nota 2: "))
Média = (Nota_1 + Nota_2)/2
if Média >= 7 and Média < 10:
    print ("Aluno Aprovado.")
elif Média < 7 or Média == 0:
    print ("Aluno Reprovado.")
elif Média == 10:
    print ("Aluno Aprovado com Honras.")
else:
    print ("Nota Inválida.")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 6:")
Number_1 = float(input("Número 1: "))
Number_2 = float(input("Número 2: "))
Number_3 = float(input("Número 3: "))
if Number_1 > Number_2 and Number_1 > Number_3:
    print (f"{Number_1} é o Maior Entre Todos.")
elif Number_2 > Number_1 and Number_2 > Number_3:
    print (f"{Number_2} é o Maior Entre Todos.")
elif Number_3 > Number_1 and Number_3 > Number_2:
    print (f"{Number_3} é o Maior Entre Todos.")
else:
    print ("Erro. Números Inválidos ou Números Iguais.")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 7:")
Number_1 = int(input("Número 1: "))
Number_2 = int(input("Número 2: "))
Number_3 = int(input("Número 3: "))
if Number_1 < Number_2 and Number_1 < Number_3:
    Menor = Number_1
elif Number_2 < Number_1 and Number_2 < Number_3:
    Menor = Number_2
elif Number_3 < Number_1 and Number_3 < Number_2:
    Menor = Number_3
print (f"O Menor Número é {Menor}")
if Number_1 > Number_2 and Number_1 > Number_3:
    Maior = Number_1
elif Number_2 > Number_1 and Number_2 > Number_3:
    Maior = Number_2
elif Number_3 > Number_1 and Number_3 > Number_2:
    Maior = Number_3
print (f"O Maior Número é {Maior}")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 8:")
Produto_1 = float(input("Qual o Preço do Produto 1? "))
Produto_2 = float(input("Qual o Preço do Produto 2? "))
Produto_3 = float(input("Qual o Preço do Produto 3? "))
if Produto_1 < Produto_2 and Produto_1 < Produto_3:
    Barato = Produto_1
    print (f"O Preço Mais Barato é {Barato}, Então Compre o Produto 1")
elif Produto_2 < Produto_1 and Produto_2 < Produto_3:
    Barato = Produto_2
    print (f"O Preço Mais Barato é {Barato}, Então Compre o Produto 2")
elif Produto_3 < Produto_1 and Produto_3 < Produto_2:
    Barato = Produto_3
    print (f"O Preço Mais Barato é {Barato}, Então Compre o Produto 3")
else:
    print ("Existem Preços Iguais, Tente Novamente")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 9:")
Aa = int(input("Digite o Número 1: "))
Bb = int(input("Digite o Número 2: "))
Cc = int(input("Digite o Número 3: "))
if Aa >= Bb and Aa >= Cc and Bb >= Cc:
    print (f"Aa Sequência Decrescente é: [{Aa}, {Bb}, {Cc}]")
elif Aa >= Bb and Aa >= Cc and Cc >= Bb:
    print (f"Aa Sequência Decrescente é: [{Aa}, {Cc}, {Bb}]")
elif Bb >= Aa and Bb >= Cc and Aa >= Cc:
    print (f"Aa Sequência Decrescente é: [{Bb}, {Aa}, {Cc}]")
elif Bb >= Aa and Bb >= Cc and Cc >= Aa:
    print (f"Aa Sequência Decrescente é: [{Bb}, {Cc}, {Aa}]")
elif Cc >= Aa and Cc >= Bb and Aa >= Bb:
    print (f"Aa Sequência Decrescente é: [{Cc}, {Aa}, {Bb}]")
elif Cc >= Aa and Cc >= Bb and Bb >= Aa:
    print (f"Aa Sequência Decrescente é: [{Cc}, {Bb}, {Aa}]")
else:
    print ("Error")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> Questão 10:")
Turno = str(input("Qual seu Turno? [M/V/N]: "))
if len(Turno) == 1:
    if Turno == "M" or "m" or "V" or "v" or "T" or "t" or "N" or "n":
        if Turno in "Mm":
            print ("Bom Dia!")
        elif Turno in "Vv" or "Tt":
            print ("Boa Tarde!")
        elif Turno in "Nn":
            print ("Boa Noite!")
        else:
            print ("Turno Inválido")
    else:
        print ("Turno Inválido")
else:
    print ("Turno Inválido")
print ("------------------------------------------------------------------------------------------------------------------------------")