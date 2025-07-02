import random

def imprime_mensagem_abertura():
    print("******************************")
    print("*      Jogo de Adivinha      *")
    print("******************************")

def escolher_nivel():
    while True:
        try:
            nivel = int(input("Escolha o nível (1 - Fácil | 2 - Médio | 3 - Difícil): "))
            if nivel == 1:
                return 6
            elif nivel == 2:
                return 4
            elif nivel == 3:
                return 2
            else:
                print("Digite um número válido entre 1 e 3.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

def jogar():
    imprime_mensagem_abertura()

    numero_secreto = random.randint(1, 100)
    total_tentativas = escolher_nivel()
    pontos = 100

    print(f"\n🎯 O jogo começou! Você tem {total_tentativas} tentativas.")

    for rodada in range(1, total_tentativas + 1):
        print(f"\nTentativa {rodada} de {total_tentativas}")
        try:
            chute = int(input("Digite um número entre 1 e 100: "))

            if chute < 1 or chute > 100:
                print("Digite um número entre 1 e 100.")
                continue

            if chute == numero_secreto:
                print(f"✅ Você acertou! Sua pontuação final foi {pontos} pontos.")
                break
            else:
                pontos_perdidos = abs(numero_secreto - chute)
                pontos -= pontos_perdidos

                if chute > numero_secreto:
                    print("🔻 Seu chute foi muito alto.")
                else:
                    print("🔺 Seu chute foi muito baixo.")
        except ValueError:
            print("⚠️ Por favor, insira um número inteiro.")

    else:
        print(f"\n💀 Fim de jogo! O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jogar()
