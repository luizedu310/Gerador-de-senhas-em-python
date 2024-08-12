
chave = input("Digite a base da sua senha:")

#Foi seguido uma sequencia de letras só até certo ponto, o resto são algumas letras recorrente 
#Exemplo de nomes para teste do código: Security = %1/u#ity // Sergio29 = %1#giokjkgh

senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "§"
    elif letra in "Bb": senha = senha + "+"
    elif letra in "Cc": senha = senha + "/"
    elif letra in "Dd": senha = senha + "("
    elif letra in "Ee": senha = senha + "1"
    elif letra in "Ff": senha = senha + "5"
    elif letra in "Rr": senha = senha + "#"
    elif letra in "Ss": senha = senha + "%"
    elif letra in "Mm": senha = senha + "$"
    elif letra in "2": senha = senha + "kjk"
    elif letra in "9": senha = senha + "gh"
    else: senha = senha + letra 
print("Sua senha:" + senha)
