"""
integrity_check.py — Verificação de integridade entre arquivos

Evolução do hash_collision.py: em vez de usar apenas MD5 (quebrado),
compara arquivos com múltiplos algoritmos e expõe quando MD5 afirma
igualdade mas SHA-256 não — situação em que a integridade NÃO é garantida.

Uso:
  python3 integrity_check.py <arquivo1> <arquivo2> [arquivo3 ...]
"""

import hashlib
import sys
from itertools import combinations
from pathlib import Path


ALGOS = {
    "MD5":    (hashlib.md5,    False),   # inseguro — colisões conhecidas
    "SHA-256":(hashlib.sha256, True),
    "BLAKE2b":(hashlib.blake2b,True),
}


def hash_file(path: Path, algo_fn) -> str:
    h = algo_fn()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def tamanho_legivel(n: int) -> str:
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {u}"
        n /= 1024
    return f"{n:.1f} TB"


def main():
    if len(sys.argv) < 3:
        print("Uso: python3 integrity_check.py <arquivo1> <arquivo2> [arquivo3 ...]")
        sys.exit(1)

    arquivos = [Path(a) for a in sys.argv[1:]]

    for p in arquivos:
        if not p.exists():
            print(f"[ERRO] Arquivo não encontrado: {p}")
            sys.exit(1)

    # ── Tabela de hashes ──────────────────────────────────────────────────
    col_arquivo = max(len(str(p)) for p in arquivos) + 2
    print(f"\n{'#':<4} {'Arquivo':<{col_arquivo}} {'Tamanho':>8}  {'MD5 (inseguro)':>32}  {'SHA-256':>64}  {'BLAKE2b':>64}")
    print("-" * (4 + col_arquivo + 8 + 32 + 64 + 64 + 10))

    hashes = {nome: {} for nome in ALGOS}

    for i, p in enumerate(arquivos, 1):
        row_hashes = {nome: hash_file(p, fn) for nome, (fn, _) in ALGOS.items()}
        for nome, val in row_hashes.items():
            hashes[nome][p] = val
        size = tamanho_legivel(p.stat().st_size)
        print(f"{i:<4} {str(p):<{col_arquivo}} {size:>8}  "
              f"{row_hashes['MD5']:>32}  "
              f"{row_hashes['SHA-256']:>64}  "
              f"{row_hashes['BLAKE2b']:>64}")

    # ── Comparação por pares ──────────────────────────────────────────────
    print(f"\n{'='*80}")
    print("  COMPARAÇÃO DE INTEGRIDADE POR PAR DE ARQUIVOS")
    print(f"{'='*80}")

    encontrou_problema = False

    for p1, p2 in combinations(arquivos, 2):
        mesmo_arquivo = p1.resolve() == p2.resolve()

        iguais_por_algo = {
            nome: hashes[nome][p1] == hashes[nome][p2]
            for nome in ALGOS
        }

        md5_igual    = iguais_por_algo["MD5"]
        sha256_igual = iguais_por_algo["SHA-256"]
        blake2_igual = iguais_por_algo["BLAKE2b"]

        print(f"\n  {p1.name}  ↔  {p2.name}")
        print(f"  {'Algoritmo':<12} {'Resultado':<30} {'Seguro?':>8}")
        print(f"  {'-'*55}")

        for nome, (_, seguro) in ALGOS.items():
            igual = iguais_por_algo[nome]
            if igual:
                resultado = "IGUAL"
            else:
                resultado = "diferente"
            seguro_str = "✔ sim" if seguro else "✘ não"
            print(f"  {nome:<12} {resultado:<30} {seguro_str:>8}")

        # Casos relevantes para integridade
        if mesmo_arquivo:
            print(f"\n  ⚠  Mesmo arquivo referenciado duas vezes.")

        elif md5_igual and not sha256_igual:
            encontrou_problema = True
            print(f"""
  ┌─────────────────────────────────────────────────────────────────┐
  │  COLISÃO MD5 — INTEGRIDADE NÃO GARANTIDA                        │
  │                                                                 │
  │  MD5 reporta os arquivos como IGUAIS, mas SHA-256 os distingue. │
  │  Um atacante pode ter substituído um arquivo por outro com o    │
  │  mesmo MD5 — a verificação por MD5 seria enganada.              │
  │                                                                 │
  │  Use SHA-256 ou BLAKE2b para garantir integridade real.         │
  └─────────────────────────────────────────────────────────────────┘""")

        elif sha256_igual and blake2_igual:
            print(f"\n  ✔  Integridade confirmada: SHA-256 e BLAKE2b são idênticos.")

        elif not sha256_igual:
            print(f"\n  ✔  Arquivos distintos — sem colisão nos algoritmos seguros.")

    # ── Resumo final ──────────────────────────────────────────────────────
    print(f"\n{'='*80}")
    if encontrou_problema:
        print("  RESULTADO: COLISÃO MD5 DETECTADA — integridade NÃO garantida por MD5.")
        print("  Troque MD5 por SHA-256 ou BLAKE2b em qualquer verificação de integridade.")
    else:
        print("  RESULTADO: Sem colisões nos algoritmos seguros — integridade garantida.")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
