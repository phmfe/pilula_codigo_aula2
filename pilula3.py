import datetime
#entra
dadata_compra = input('Digite a data da compra d/m/aaaa: ')
meses = int(input('Prazo de garantia: '))
#processamento
data_inicial = datetime.datetime.strptime(data_compra, '%d/%m/%Y')
data_final = data_inicial + datetime.timedelta(days=meses * 30)
print(f'Garantia valida ate {data_final.strftime('%d/%m/%Y')}')
print(f'Dia da semana: {data_final.strftime('%A')}')