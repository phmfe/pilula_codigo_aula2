import math
assinate = int(input('Assinates atuais:'))
mensalidade = float(input('valor da mensalidade: '))
taxa = float(input('taxa de crescimento mensal:(%)'))/100
#processamento
assinantes_finais = assinantes * math.pow((1+taxa),meses)
receita_final = assinates_finais * mensalidade 
#saida
print(f'Assinates estimados: {assinates_finais:.0f}')
print(f'Receita mwnsal estimada R$:{receita_final:.2f}')
