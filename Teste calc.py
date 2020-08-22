o = input('Qual operação você quer fazer (+ - * /):')
n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
if o == '+':
    t1 = n1 + n2
    print(f'{n1} + {n2} é {t1}')
elif o == '-':
    t2 = n1 - n2
    print(f'{n1} - {n2} é {t2}')
elif o == '*':
    t3 = n1 * n2
    print(f'{n1} x {n2} é {t3}')
elif o == '/':
    t4 = n1 / n2
    print(f'{n1} / {n2} é {t4:.2f}')
