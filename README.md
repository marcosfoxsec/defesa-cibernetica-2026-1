# Defesa Cibernética 2026.1

**Instituição:** Instituto Militar de Engenharia (IME)
**Disciplina:** Defesa Cibernética
**Professor:** Anderson Santos, DSc.
**Período:** 2026.1

---

## Sobre a disciplina

A disciplina de **Defesa Cibernética** do IME aborda os fundamentos teóricos e práticos da segurança da informação com ênfase na proteção de sistemas, redes e dados em ambientes computacionais modernos.

---

## Exercícios e implementações

Os códigos deste repositório são implementações práticas dos conceitos estudados em aula. O objetivo é consolidar o entendimento teórico por meio de demonstrações funcionais.

| Arquivo | Conceito | Descrição |
|---|---|---|
| `cifra_cesar.py` | Criptografia clássica | Implementação interativa da Cifra de César com cifragem e decifragem |
| `cifra_de_cesar_com_confidencialidade.py` | Confidencialidade | Extensão da Cifra de César com derivação de chave via SHA-256 e entrada de senha oculta (`getpass`) |
| `hash_collision.py` | Funções de hash | Verificação de colisão MD5 entre dois ou mais arquivos |
| `integrity_check.py` | Integridade | Verificação de integridade entre arquivos com MD5, SHA-256 e BLAKE2b — expõe colisões MD5 que passariam despercebidas em verificações de integridade |

---

## Estrutura do repositório

```
.
├── cifra_cesar.py                              # Cifra de César — criptografia por substituição
├── cifra_de_cesar_com_confidencialidade.py     # Cifra de César com KDF (SHA-256) e getpass
├── hash_collision.py                           # Detecção de colisão MD5 entre arquivos
├── integrity_check.py                          # Verificação de integridade: MD5 vs SHA-256 vs BLAKE2b
└── README.md
```

---

## Referências

- STALLINGS, W. *Cryptography and Network Security*. 8. ed. Pearson, 2022.
- FERGUSON, N.; SCHNEIER, B.; KOHNO, T. *Cryptography Engineering*. Wiley, 2010.
- NIST FIPS 180-4 — *Secure Hash Standard (SHS)*
- WANG, X. et al. *How to Break MD5 and Other Hash Functions*. Eurocrypt, 2005.
