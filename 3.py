import json

# Abre o arquivo faturamento.json e carrega os dados
with open('dados/faturamento.json', 'r') as file:
    faturamento = json.load(file)

# Extrai os dados do mês de janeiro
faturamento_janeiro = faturamento['Janeiro']

# Inicializa as variáveis com valores iniciais
menor_valor = float('inf')
maior_valor = float('-inf')
soma_valores = 0
dias_acima_media = 0

# Percorre os dados de faturamento
for dia in faturamento_janeiro:
    valor = dia['faturamento']

    # Atualiza o menor valor
    if valor < menor_valor:
        menor_valor = valor

    # Atualiza o maior valor
    if valor > maior_valor:
        maior_valor = valor

    # Soma o valor para o cálculo da média
    soma_valores += valor

# Calcula a média
media = soma_valores / len(faturamento_janeiro)

# Percorre novamente os dados de faturamento
for dia in faturamento_janeiro:
    valor = dia['faturamento']

    # Verifica se o valor é superior à média e não é igual a zero
    if valor > media and valor != 0:
        dias_acima_media += 1

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
