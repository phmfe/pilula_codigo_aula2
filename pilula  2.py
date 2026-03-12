import random
#entradas
cotacao = float(input('Cotaçao atual do dolar: '))
#processamento
variacão = random.uniform(-0.015, 0.015)
nova_cotacao = cotaçao * (1 + variacao)
print(f'Variação simulada: {variacao: .3%}')
print(f'Nova cotação>: R$ {nova_cotacao:.4f}')
