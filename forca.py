palavra_secreta = 'casa'
letras_acertadas = ''
tentativas = 0

def forca(letra):
    while True:
        palavra_formada = ''       
        if letra in palavra_secreta:
            letras_acertadas += letra
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
        tentativas += 1
        print(f'Palavra formada: {palavra_formada}')
        if palavra_formada == palavra_secreta:
            print(f'Fim do Jogo!\nA palavra é {palavra_secreta}.\nVocê acertou na {tentativas}ª tentativa.')
            letras_acertadas = ''
            tentativas = 0

letra_digitada = input('Digite uma letra: ')
forca(letra_digitada)