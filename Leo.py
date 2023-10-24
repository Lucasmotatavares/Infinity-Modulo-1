print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 1: Estrutura Repetitiva While")
print ("Há Diferença Entre If e While, Porém são Parecidas")
print ("Na Instrução If, Quando a Condição é Atendida as Instruções são Repetidas Apenas uma Vez")
print ("Na Instrução While, Enquanto a Condição é Atendida as Instruções são Repetidas")
print ("Tomar Cuidado com Código Resultando em Loop Infinito")
print ("[Number = Number + 1] é Igual a [Number += 1]")
print ("O Comando [while True:] é Loop Infinito Intencional, Precisa o Usuário Finalizar o Programa")
print ("O Comando [break] Encerra o Programa Intencionalmente Infinito, Relacionado à uma Condição")
print ("Uso Prático do Loop Infinito Intencional são Apps, Games e Etc.")
print ("------------------------------------------------------------------------------------------------------------------------------")



print ("-> 2: Exemplo")
Number = 0
while Number < 10:
    print (Number)
    Number = Number + 1



print ("------------------------------------------------------------------------------------------------------------------------------")



print ("-> 3: Exemplo")
Number = 0
while Number < 201:
    print (Number)
    Number += 1



print ("------------------------------------------------------------------------------------------------------------------------------")



print ("-> 4: Exemplo")
for Info in range (1, 201):
    print (Info)



print ("------------------------------------------------------------------------------------------------------------------------------")



print ("-> 5: Exemplo")
for Info in range (0, 101, 10):
    print (Info)



print ("------------------------------------------------------------------------------------------------------------------------------")



print ("-> 6: Exemplo")
Number = 0
while Number <= 100:
    print (Number)
    Number += 10



print ("------------------------------------------------------------------------------------------------------------------------------")



print ("-> 6: Exemplo")
Valor = 7
while Valor <= 100:
    if Valor % 10 == 0:
        print (Valor)
        Valor += 1



print ("------------------------------------------------------------------------------------------------------------------------------")



print ("-> 7: Exemplo")
while True:
    Number = int(input("Digite seu Número: "))
    if Number > 100:
        break
    else:
        print (Number)



print ("-> 50: Observações Importantes")
print ("O Comando [Ctrl + C] Encerra Loop Infinito Indesejado")



print ("------------------------------------------------------------------------------------------------------------------------------")