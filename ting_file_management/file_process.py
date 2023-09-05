from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lines = txt_importer(path_file)

    if len(instance.data) > 0:
        for elements in instance.data:
            if elements["nome_do_arquivo"] == path_file:
                return None

    value = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(value)
    return print(value)


def remove(instance):
    if len(instance.data) == 0:
        return print("Não há elementos")

    path_file = instance.data[0]
    instance.dequeue()
    return print(
        f"Arquivo {path_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        return print(instance.search(position))
    except IndexError:
        return sys.stderr.write("Posição inválida")
