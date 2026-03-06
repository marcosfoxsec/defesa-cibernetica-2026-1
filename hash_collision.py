"""
Verifica colisão de hash MD5 entre dois ou mais arquivos.
Suporta qualquer tipo: .jpg, .jpeg, .png, .gif, .bmp, .webp, .bin, etc.

Uso:
  python3 hash_collision.py <arquivo1> <arquivo2> [arquivo3 ...]
"""

import hashlib
import sys
from pathlib import Path
from itertools import combinations

EXTENSOES_SUPORTADAS = {
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".tif",
    ".ico", ".svg", ".raw", ".bin", ".img", ".iso", ".dat", ".exe",
    ".pdf", ".zip", ".tar", ".gz", ".7z",
}


def md5_file(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def tamanho_legivel(n: int) -> str:
    for unidade in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unidade}"
        n /= 1024
    return f"{n:.1f} TB"


def main():
    if len(sys.argv) < 3:
        print("Uso: python3 hash_collision.py <arquivo1> <arquivo2> [arquivo3 ...]")
        sys.exit(1)

    arquivos = [Path(a) for a in sys.argv[1:]]

    # Valida existência e extensão
    erros = False
    for p in arquivos:
        if not p.exists():
            print(f"[ERRO] Arquivo não encontrado: {p}")
            erros = True
        elif p.suffix.lower() not in EXTENSOES_SUPORTADAS:
            print(f"[AVISO] Extensão não reconhecida: {p.suffix}  ({p.name}) — processando mesmo assim")
    if erros:
        sys.exit(1)

    # Calcula hashes
    print("\n{:<5} {:<40} {:>10}  {}".format("#", "Arquivo", "Tamanho", "MD5"))
    print("-" * 75)
    hashes = {}
    for i, p in enumerate(arquivos, 1):
        h = md5_file(p)
        size = tamanho_legivel(p.stat().st_size)
        print(f"{i:<5} {str(p):<40} {size:>10}  {h}")
        hashes[p] = h

    # Verifica colisões entre todos os pares
    print("\n" + "=" * 75)
    colisoes = []
    for p1, p2 in combinations(arquivos, 2):
        if hashes[p1] == hashes[p2]:
            if p1.resolve() == p2.resolve():
                print(f"[AVISO] Mesmo arquivo referenciado duas vezes: {p1}")
            else:
                colisoes.append((p1, p2, hashes[p1]))

    if colisoes:
        print(f"COLISÃO MD5 DETECTADA — {len(colisoes)} par(es) com hash idêntico:\n")
        for p1, p2, h in colisoes:
            print(f"  {p1.name}  ==  {p2.name}")
            print(f"  MD5: {h}\n")
    else:
        print("Sem colisões — todos os hashes são distintos.")

    print("=" * 75)


if __name__ == "__main__":
    main()
