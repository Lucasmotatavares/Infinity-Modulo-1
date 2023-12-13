Car_Speed = int(input('Insira a Velocidade do Carro em Km: '))
Max_Speed = 80
Valor_Multa = 20
Multa = (Car_Speed - Max_Speed) * Valor_Multa

if Car_Speed > 80:
    print (f'Você Ultrapassou o Limite de Velocidade, a Multa Aplicada será de R$ {Multa}')
else:
    print ('Prossiga')