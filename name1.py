# Mudando para letras maiúsculas e minúsculas em uma string
# usando métodos

nome = "maria clara"
letra_maiuscula = nome.title()
print(letra_maiuscula)

# Saída:
# Maria Clara

# Outro exemplo diferente:
nome = "joão pedro"
print(nome.title())

# Saída:
# João Pedro

# title() --> exibe cada palavra com uma letra maiúscula no início.

nome1 = "paulo sebastião"
print(nome1.upper()) # Upper() deixa todas as letras maiúsculas
# Saída = PAULO SEBASTIAO

nome2 = "PAULO SEBASTIÃO"
print(nome2.lower()) # lower() deixa todas as letras minúsculas
# Saída = paulo sebastião

# Exemplo diferente:
nome3 = "rogério andrade"
nome_maiusculo1 = nome3.upper()
print(nome_maiusculo1)
# Saída = ROGÉRIO ANDRADE

nome4 = "ROGÉRIO ANDRADE"
nome_minusculo = nome4.lower()
print(nome_minusculo)
# Saída = rogério andrade

# combinando métodos também da certo:
nome5 = "ROGÉRIO ANDRADE"
nome_titulo = nome5.lower().title()
print(nome_titulo)
# Saída = Rogério Andrade