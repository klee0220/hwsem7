'''
Винни-Пух попросил Вас посмотреть,
есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто,
насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов,
то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
    **Вывод:** Парам пам-пам
'''


def check_rhythm(poem):
    phrases = poem.split(" ")
    syllables = []

    for phrase in phrases:
        words = phrase.split("-")
        phrase_syllables = sum([count_syllables(word) for word in words])
        syllables.append(phrase_syllables)

    if len(set(syllables)) == 1:
        return "Param pam-pam"  # Rhythm is okay
    else:
        return "Pam param"  # Rhythm is not okay


def count_syllables(word):
    vowels = "aeiou"
    count = 0

    for char in word:
        if char.lower() in vowels:
            count += 1

    return count


# Example usage
poem = input("Enter the poem: ")
result = check_rhythm(poem)
print(result)