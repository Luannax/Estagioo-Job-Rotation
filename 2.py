numero = int(input("Digite um número: "))

fibonacci = [0, 1]

while fibonacci[-1] < numero:
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)

if numero in fibonacci:
    print(f"O número {numero} pertence à sequência de Fibonacci!")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
