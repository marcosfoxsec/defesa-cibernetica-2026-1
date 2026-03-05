#!/usr/bin/env python3
"""
Cifra de César — Implementação Interativa
Mestrado IME — Defesa Cibernética 2026.1
"""


def cifrar(mensagem: str, rotacao: int) -> str:
    resultado = []
    for char in mensagem:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado.append(chr((ord(char) - base + rotacao) % 26 + base))
        else:
            resultado.append(char)
    return ''.join(resultado)


def decifrar(mensagem: str, rotacao: int) -> str:
    return cifrar(mensagem, -rotacao)


def obter_rotacao() -> int:
    while True:
        try:
            r = int(input("Rotacao (1-25): "))
            if 1 <= r <= 25:
                return r
            print("  Digite um valor entre 1 e 25.")
        except ValueError:
            print("  Entrada invalida. Digite um numero inteiro.")


def menu():
    print("\n==============================")
    print("       CIFRA DE CESAR         ")
    print("==============================")
    print("  [1] Cifrar mensagem         ")
    print("  [2] Decifrar mensagem       ")
    print("  [0] Sair                    ")
    print("==============================")


def main():
    while True:
        menu()
        opcao = input("\nEscolha uma opcao: ").strip()

        if opcao == '0':
            print("Encerrando...")
            break
        elif opcao in ('1', '2'):
            mensagem = input("Mensagem: ")
            rotacao = obter_rotacao()

            if opcao == '1':
                resultado = cifrar(mensagem, rotacao)
                label = "Cifrada"
            else:
                resultado = decifrar(mensagem, rotacao)
                label = "Decifrada"

            print(f"\n  {label}: {resultado}")
        else:
            print("  Opcao invalida.")


if __name__ == "__main__":
    main()
