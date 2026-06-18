def group_anagrams(words: list[str]) -> list[list[str]]:
    anagrams = {}

    for word in words:
        chave =''.join(sorted(word))

        if chave not in anagrams:
            anagrams[chave] = []

        anagrams[chave].append(word)

    return list(anagrams.values())
