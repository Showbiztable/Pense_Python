"""
    Escreva um script que leia a hora atual e a converta em um tempo em horas, minutos e segundos, mais o número de dias
    desde a época.
"""

import time


hora_atual = time.time()
hora = int(hora_atual)
minutos = (hora_atual - hora) * 60
segundos = (minutos - int(minutos)) * 60
dias = hora / 24

print('Horas : ', hora)
print('Minutos : ', int(minutos))
print('Segundos : ', int(segundos))
print('Já se passaram :', int(dias), 'dias')
