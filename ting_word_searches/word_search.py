def exists_word(word, instance):
    for item in instance.data:
        found = search_by_word(word, instance["linhas_do_arquivo"])
        if found == word:
            response = {
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorências": len(search_by_word(word, instance["linhas_do_arquivo"])),
            }
    return response


def search_by_word(word, instance):
    array = []
    for item in range(0, len(instance)):
        file = instance.search(item)
        foundTimes = []
        for element, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                foundTimes.append({"linha": element + 1})

        if len(foundTimes) > 0:
            array.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorências": len(foundTimes),
                }
            )
    return array

