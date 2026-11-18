from datetime import date
from time import sleep
while True:
 sleep(1.5)
 ano = int(input('Qual ano vc quer saber se é bissexto?'))
 sleep(1.5)
 if ano == 0:
    ano = date.today().year
 if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('Voce tem um ano bissexto')
 else:
    print ('Você nao tem um ano bissexto')
