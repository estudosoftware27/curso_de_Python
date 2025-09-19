# Combinando ou concatenando strings
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)  # Saída: João Silva

# python usa o operador + para concatenar strings
# compor mensagens completas
mensagem = "Olá, " + nome + " " + sobrenome + "! Bem-vindo ao curso."
print(mensagem)  # Saída: Olá, João Silva! Bem-vindo ao curso.
# criar identificadores únicos
identificador = nome + "_" + sobrenome
print(identificador)  # Saída: João_Silva
# formatar dados para exibição
data = "2024"
print("Ano:", data)  # Saída: Ano: 2024

first_name = "maria"
last_name = "oliveira"
full_name = first_name + " " + last_name
print("hello, " + full_name.title() + "!")  # Saída: hello, Maria Oliveira!
print("hello, " + full_name.upper() + "!")  # Saída: hello, MARIA OLIVEIRA!
print("hello, " + full_name.lower() + "!")  # Saída: hello, maria oliveira!