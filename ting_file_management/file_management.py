import sys


def txt_importer(path_file):
    doc = path_file.endswith(".txt")
    try:
        if not doc:
            return sys.stderr.write("Formato inválido")
        with open(path_file, "r") as file:
            lines = file.read().split("\n")
            return lines
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
