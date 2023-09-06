def exists_word(word, instance):
    array = []
    for item in range(0, len(instance)):
        files = instance.search(item)
        found = []
        for item, lines in enumerate(files["linhas_do_arquivo"]):
            if word.lower() in lines.lower():
                found.append({"linha": item + 1})
        if found:
            array.append({
                "palavra": word,
                "arquivo": files["nome_do_arquivo"],
                "ocorrencias": found
            })
    return array


def search_by_word(word, instance):
    array = []
    for item in range(0, len(instance)):
        files = instance.search(item)
        found = []
        for item, line in enumerate(files["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                found.append({"linha": item + 1, "conteudo": line})
        if found:
            array.append(
                {
                    "palavra": word,
                    "arquivo": files["nome_do_arquivo"],
                    "ocorrencias": found,
                }
            )
    return array
