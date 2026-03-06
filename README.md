# Defesa Cibernética 2026.1

**Instituição:** Instituto Militar de Engenharia (IME)
**Disciplina:** Defesa Cibernética
**Professor:** Anderson Santos, DSc.
**Período:** 2026.1

---

## Cifra de César — Implementação Interativa

Script Python que implementa a **Cifra de César**, uma das técnicas de criptografia mais antigas, baseada na substituição de cada letra da mensagem por outra deslocada um número fixo de posições no alfabeto.

### Como funciona

Dado um texto e uma rotação `n`, cada letra é deslocada `n` posições:

```
Mensagem:  ATAQUE AO AMANHECER
Rotação:   3
Cifrada:   DWDTXH DR DPDQKHFHU
```

Para decifrar, aplica-se a rotação inversa (`-n`).

### Funcionalidades

- Cifrar mensagem com rotação definida pelo usuário (1–25)
- Decifrar mensagem com rotação conhecida
- Preserva maiúsculas, minúsculas e caracteres especiais (espaços, pontuação)
- Validação de entrada com tratamento de erros
- Interface interativa via terminal

### Execução

```bash
python3 cifra_cesar.py
```

```
==============================
       CIFRA DE CESAR
==============================
  [1] Cifrar mensagem
  [2] Decifrar mensagem
  [0] Sair
==============================
```

### Requisitos

- Python 3.6+
- Sem dependências externas

---

## Estrutura do Repositório

```
.
├── cifra_cesar.py   # Implementação da Cifra de César
└── README.md        # Documentação
```
