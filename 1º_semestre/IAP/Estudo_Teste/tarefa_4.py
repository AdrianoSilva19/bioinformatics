'''Numa empresa, os funcionários são pagos a 250$00 à hora. Pretende-se que, a partir do
número de horas de laboração de um empregado em cada um dos 5 dias da semana, e
tendo em conta que os descontos para segurança social e IRS representam 20% do
vencimento bruto, calcular o valor a receber pelo empregado na referida semana.'''

def vencimento(s : int):
    '''Recebe um valor de vencimento, pede as horas que o trabalhador fez por dia e dá
    o return do valor do salario liquido nessa semana'''
    salario=s
    dias = ['segunda','terça','quarta','quinta','sexta']
    total = 0
    for n in range(len(dias)):
        horas = int(input(f'quantas horas trabalhou na {dias[n]}? \n'))
        total += horas
    bruto = total * salario
    liquido = 0.8*bruto
    return f'{liquido}$'

print(vencimento(250))