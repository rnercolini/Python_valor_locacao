# Calcula o valor da locação de um veículo com base nos quilômetros rodados e dias de locação
km = float(input("Digite quantos quilômetros o veículo percorreu: "))
dia = int(input("Digite quantos dias de aluguel do veículo: "))
ckm = km * 0.15
cdia = dia * 60
total = ckm + cdia
print('=' * 50)
print('Km percorrido {0}.\nValor do Km R${1:.2f}.\nDias de locação {2:.0f}.\nValor da locação R${3:.2f}.'
      '\nValor total R${4:.2f}'.format(km, ckm, dia, cdia, total))
