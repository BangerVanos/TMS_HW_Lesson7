def is_polyndrom(word: str) -> bool:
    backw_word = ""
    for i in range(len(word)-1, -1, -1):
        backw_word += word[i]
    if backw_word == word:
        return True
    else:
        return False


word_list = tuple(input("Введите список слов: ").split())
filtered = tuple(filter(is_polyndrom, word_list))
print(f"Первоначальный список слов: {word_list}")
print(f"Палиндромы: {filtered}")
