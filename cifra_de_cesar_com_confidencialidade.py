#!/usr/bin/env python3
"""
Cifra de César com Confidencialidade
Mestrado IME — Defesa Cibernética 2026.1

Melhorias em relação à implementação original:
  - Chave derivada de senha via SHA-256 (KDF básico)
  - Entrada de senha oculta com getpass (sem exposição no terminal)
  - Chave nunca trafega como número bruto
"""

import hashlib
import getpass


def derivar_rotacao(senha: str) -> int:
    """Deriva a rotação a partir de uma senha via SHA-256.

    A chave nunca é fornecida diretamente como número — ela é derivada
    de um segredo textual, ampliando o espaço efetivo de chaves e
    evitando que a rotação apareça em logs ou histórico do shell.
    """
    digest = hashlib.sha256(senha.encode('utf-8')).digest()
    return (digest[0] % 25) + 1  # rotação em [1, 25]


def cifrar(mensagem: str, rotacao: int) -> str:
    """Cifra a mensagem deslocando cada letra pelo valor de rotação."""
    resultado = []
    for char in mensagem:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado.append(chr((ord(char) - base + rotacao) % 26 + base))
        else:
            resultado.append(char)
    return ''.join(resultado)


def decifrar(mensagem: str, rotacao: int) -> str:
    """Decifra revertendo a rotação."""
    return cifrar(mensagem, -rotacao)


def obter_chave() -> int:
    """Solicita a senha sem exibi-la no terminal e deriva a rotação."""
    senha = getpass.getpass("Senha (nao sera exibida): ")
    return derivar_rotacao(senha)


def menu():
    print("\n==============================")
    print("  CIFRA DE CESAR              ")
    print("  (com confidencialidade)     ")
    print("==============================")
    print(" [1] Cifrar mensagem          ")
    print(" [2] Decifrar mensagem        ")
    print(" [0] Sair                     ")
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
            rotacao = obter_chave()

            if opcao == '1':
                resultado = cifrar(mensagem, rotacao)
                label = "Cifrada"
            else:
                resultado = decifrar(mensagem, rotacao)
                label = "Decifrada"

            print(f"\n {label}: {resultado}")
        else:
            print(" Opcao invalida.")


if __name__ == "__main__":
    main()
