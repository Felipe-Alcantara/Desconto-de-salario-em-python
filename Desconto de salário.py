mensagem = 'olá mundo'
print(mensagem)

while True:
    try:
        salario_bruto = float(input('Digite seu salário: '))
        break
    except ValueError:
        print('Entrada inválida, digite um NÚMERO')

while True:
    try:
        descontos = float(input('Qual o valor de desconto em folha? '))
        break
    except ValueError:
        print('Entrada inválida, digite um NÚMERO')

while True:
    try:
        liquido = round(float(salario_bruto - descontos), 3)
        break
    except ValueError:
        print('Entrada inválida, digite um NÚMERO')

print('Descontando R${} do seu R${}, seu salário liquido será: R${}'.format(descontos, salario_bruto, liquido))
print('Obrigado')
print('By: Felixo')
