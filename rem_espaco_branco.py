# Removendo espaços em branco 
# Removendo espaços do lado direito --> rstrip()
# Removendo espaços do lado esquerdo --> lstrip()
# Removendo espaços dos dois lados --> strip()
# Exemplo:
frase = "   Olá, Mundo!   "
print(frase.rstrip()) # Remove espaços à direita
print(frase.lstrip()) # Remove espaços à esquerda
print(frase.strip())  # Remove espaços dos dois lados
# Saída:
# "   Olá, Mundo!"
# "Olá, Mundo!   "
# "Olá, Mundo!"
# Note que os espaços dentro da frase não são removidos.
# Se quiser remover todos os espaços, incluindo os internos, use replace():
frase_sem_espacos = frase.replace(" ", "")
print(frase_sem_espacos) # "Olá,Mundo!"
# Saída: "Olá,Mundo!"

linguagem = "   Python   "
print(linguagem.strip())  # Remove espaços dos dois lados
# Saída: "Python"
# Removendo todos os espaços, incluindo os internos
linguagem_sem_espacos = linguagem.replace(" ", "")
print(linguagem_sem_espacos)  # "Python"
# Saída: "Python"
# Removendo espaços em branco de uma lista de strings
frases = ["   Olá   ", "   Mundo   ", "   Python   "]
frases_sem_espacos = [frase.strip() for frase in frases]
print(frases_sem_espacos)  # ['Olá', 'Mundo', 'Python']
# Saída: ['Olá', 'Mundo', 'Python']