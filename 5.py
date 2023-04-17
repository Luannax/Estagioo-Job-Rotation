# Recebe uma string do usuário
string = input("Digite uma string: ") 

# Variável para armazenar a string invertida
inverted_string = "" 

# Percorre a string de trás para frente e adiciona cada caractere na variável inverted_string
for i in range(len(string)-1, -1, -1):
    inverted_string += string[i]

print("String invertida: ", inverted_string)
