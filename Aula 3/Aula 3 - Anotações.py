print ("-> 1: Estruturas Repetitivas")
print ("Há 2 Types de Estruturas Repetitivas: For e While")
print ("For de Iteração irá Executar Repetição nos Elementos Dentro da Variável")
print ("Variáveis Booleanas Podem Controlar os Outcomes do For")
print ("Múltiplas Variáveis no For ou If São Utilizadas para Controle dos Outcomes do For")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 2: Exemplo")
Name = "Maria"
for Letra in Name:
    print (Letra)
    print ("Any Text")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 3: Exemplo")
Name = str(input("Insert Your Name: ")).upper
Have_A = False
for Letra in Name:
    if Letra == "A":
        Have_A = True
if Have_A == True:
    print ("Your Word Does Have A")
else:
    print ("Your Word Doesn't Have A")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 4: Exemplo")
Name = str(input("Insert Your Name: ")).upper
Have_A = False
Quantity = 0
for Letra in Name:
    if Letra == "A":
        Have_A = True
        Quantity = Quantity + 1
if Have_A == True:
    print (f"Your Word Does Have {Quantity} A")
else:
    print ("Your Word Doesn't Have A")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 5: Exemplo")
Alfabeto = "ABCDEFGHIJKLMNOPQRSTUVXYWZ"
Vogais = "AEIOU"
for Letra in Alfabeto:
    if Letra not in Vogais:
        print (Letra)
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 6: Exemplo")
Frase = str(input("Digite sua Frase: "))
Número = ("0123456789")
Tem_Número = 0
Lista = []
for Caracter in Frase:
    if Caracter in ("0123456789"):
        Tem_Número += 1
        Lista.append(Caracter)
print (f"A Quantidade de Números é: {Tem_Número}")
print (f"Os Números Encontrados Foram {Lista}")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 7: Utilização de Range no For")
print ("Quando Tem Apenas 1 Argumento vai de 0 a X")
print ("Quando Tem 2 Argumentos vai de X a Anterior ao Y")
print ("Quando Tem 3 Argumentos vai de X a Anterior ao Y e Pulará Z Casas por Contagem")
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 8: Exemplo")
for Número in range(10):
    print (Número)
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 9: Exemplo")
for Número in range(5, 10):
    print (Número)
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 10: Exemplo")
for Número in range(2, 200, 2):
    print (Número)
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("-> 20: Observações Importantes")
print ("Por Convenção Intuitiva, Escrevemos as Variáveis de Acordo com a Informaçõa que Será Inserida")
print ("Após o In Pode Ser Usado Tanto a Variável Quanto a Informação nela Contida")