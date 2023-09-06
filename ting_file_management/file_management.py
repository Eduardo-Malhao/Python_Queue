def txt_importer(path_file):
    doc = path_file.endswith(".txt")
    try:
        if not doc:
            raise ValueError("Formato inválido")
        with open(path_file, "r") as doc:
            lines = doc.read().split("\n")
            return lines
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo {path_file} não encontrado")
