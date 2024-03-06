print('Digite "Sim" ou "Não" para as perguntas.')

p1 = str(input('Telefonou para a vítima? ')).strip().upper()
p2 = str(input('Esteve no local do crime? ')).strip().upper()
p3 = str(input('Mora perto da vítima? ')).strip().upper()
p4 = str(input('Devia para a vítima? ')).strip().upper()
p5 = str(input('Já trabalhou com a vítma? ')).strip().upper()

resposta = [p1, p2, p3, p4, p5]
respostaresultado = resposta.count('SIM')

if respostaresultado < 2:
    print('Inocente.')
elif respostaresultado == 2:
    print('Suspeito.')
elif 2 < respostaresultado <= 4:
    print('Cúmplice.')
else:
    print('Assassino.')