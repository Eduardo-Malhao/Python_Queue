from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lines = txt_importer(path_file)

    value = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    if len(instance.queue) > 0:
        for elements in instance.queue:
            if elements["nome_do_arquivo"] == path_file:
                return None

    instance.enqueue(value)
    print(value)


def remove(instance):
    if len(instance.queue) == 0:
        print("Não há elementos")
    else:
        path_file = instance.queue[0]
        instance.dequeue()
        print(f"Arquivo {path_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        return sys.stderr.write("Posição inválida")
