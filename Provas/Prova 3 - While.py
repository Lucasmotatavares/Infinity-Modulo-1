Soma = 0
Quantidade = 0
Média = 0

while True:
    Number = int(input('Digite seus Números: '))
    
    if Number == 0:
        break
    
    Soma = Soma + Number
    Quantidade = Quantidade + 1
    Média = Soma / Quantidade

print (Soma)
print (Quantidade)
print (Média)

    

    
