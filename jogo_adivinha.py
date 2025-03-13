import random

def jogar_adivinha():
    # Gerar número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas_maximas = 7
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhar o Número!")
    print("----------------------------------------")
    print(f"\nTenho um número secreto entre 1 e 100.")
    print(f"Você tem {tentativas_maximas} tentativas para adivinhar.")

    while tentativas < tentativas_maximas:
        # Calcular tentativas restantes
        tentativas_restantes = tentativas_maximas - tentativas
        
        # Solicitar palpite do usuário
        try:
            print(f"\nTentativas restantes: {tentativas_restantes}")
            palpite = int(input("Digite seu palpite (ou 0 para sair): "))
            
            # Verificar se usuário quer sair
            if palpite == 0:
                print(f"\nJogo encerrado. O número secreto era {numero_secreto}.")
                return

            # Incrementar contador de tentativas
            tentativas += 1

            # Verificar palpite
            if palpite == numero_secreto:
                print(f"\nParabéns! Você acertou em {tentativas} tentativas!")
                print("O número secreto era", numero_secreto)
                return
            elif palpite < numero_secreto:
                print("Dica: O número secreto é MAIOR que seu palpite.")
            else:
                print("Dica: O número secreto é MENOR que seu palpite.")

        except ValueError:
            print("Por favor, digite apenas números!")
            continue

    # Se acabaram as tentativas
    print("\nGame Over! Suas tentativas acabaram.")
    print(f"O número secreto era {numero_secreto}.")

# Iniciar o jogo
if __name__ == "__main__":
    jogar_adivinha()
