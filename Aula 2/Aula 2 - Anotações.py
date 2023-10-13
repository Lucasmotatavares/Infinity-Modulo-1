print ("-> 1: Estruturas Condicionais")
print ("Fazer que o Programa Tome Decisões de Acordo com o Cumprimento das Regras Impostas ou Não dos Dados Apresentados pelo Usuário ")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 2: Condicional If")
print ("If = Significa Se")
print ("Geralmente Usa-se em Operações Comparativas")
print ("Será o Começo da Cadeia e Caso de Condições Múltiplas")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 3: Exemplo")
Número_1 = 8
Número_2 = 6
print ("Bem Vindo!")
if Número_1 == Número_2:
    print ("São Iguais")
if Número_1 != Número_2:
    print ("São Diferentes")
print ("Tchau!")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 4: Condicional Else")
print ("Usado em Situações onde tem Apenas 2 Opções")
print ("Tecnicamente é o Fim do If")
print ("É Mais Prático que Usar 2 If's")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 5: Exemplo")
Número_1 = int(input("Número 1: "))
Número_2 = int(input("Número 2: "))
print ("Bem Vindo!")
if Número_1 == Número_2:
    print ("São Iguais!")
else:
    print ("Não São Iguais!")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 6: Exemplo")
print ("Bem Vindo!")
Idade = int(input("Idade: "))
if Idade >= 18:
    print ("Individuo Possui Maioridade!")
else:
    print ("Indivíduo Não Possui Maioridade!")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 7: Condicional Elif")
print ("Utilizado em Multiplas Condicições")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 8: Exemplo")
Number = int(input("Your Number: "))
if Number > 0:
    print ("Your Number is Positive")
elif Number < 0:
    print ("Your Number is Negative")
else:
    print ("Your Number is Neutral")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 9: Exemplo")
Color = str(input("Your Color [Green / Yellow / Red]: ")).capitalize().strip()
if Color == str("Green"):
    print ("Go On")
elif Color == str("Yellow"):
    print ("Take Caution")
elif Color == str("Red"):
    print ("Stop")
else:
    print ("Invalid Color, Try Again")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 10: Operadores Lógicos")
print ("And = Quando 2 Condições Precisam ser Atendidas")
print ("Or = Quando 1 das 2 Condições Precisa ser Atendida")
print ("Not = Quando 1 Condição é o Oposto da Outra, Sempre")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 11: Exemplo")
Grade = int(input("Your Grade: "))
if Grade >= 0 and Grade <= 10:
    print (f"Your Grade is {Grade}. ")
else:
    print ("Invalid Grade")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 12: Exemplo")
Alternativa = str(input("Você Deseja Sair? S/N")).lower()
if Alternativa == "s" or "n":
    print ("Alternativa Válida")
    if Alternativa == "s":
        print ("Ok, Cuidado.")
    else:
        print ("Sem Problemas.")
else:
    print ("alternativa Inválida")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 13: Condicional Match")
print ("Caso seja Necessário Verificar Várias Escolhas de uma Mesma Variável")
print ("Refinar Códigos que seriam Usados Vários Elif, Repetindo a Variável em Cada Elif")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 14: Exemplo")
Cor = str(input("Digite sua Cor: ")).capitalize()
match Cor:
    case "Vermelho":
        print ("Pare!")
    case "Amarelo":
        print ("Atenção")
    case "Verde":
        print ("Siga em Frente")
    case _:
        print ("Cor Inválida")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 15: Exemplo Especial")
Letra = str(input("Digite sua Letra: ")).lower()
if Letra in "aeiou":
    print ("True")
else:
    print ("False")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 16: Observações Importantes")
print ("Caso o Sistema Necessite Identificar/Alinhar Linhas str para Maiúsculo ou Minúsculo todas as Letras, Usar .upper() ou .lower()")
print ("Caso seja Necessário Refinar Apenas a Primeira Letra da Palavra, Usar .capitalize() ")
print ("Caso seja Necesário Refinar Apenas a Primira Letra de todas as Palavras, Usar .title() ")
print ("Retirar Espaços Indesejados pelo Usuário na Inserção de Dados, no Antes e Depois, Usar .strip() ")
print ("O Conceito de If, Else e Elif pode ser Usado Dentro Deles Mesmos, como If dentro de If, If Dentro de Else, Else Dentro de If")
print ("Shift + Tab = Recua Linhas Adiantadas")
print ("Utilizar if len(?) == 1, Demilitar Número de Caracteres Inseridos pelo Usuário")