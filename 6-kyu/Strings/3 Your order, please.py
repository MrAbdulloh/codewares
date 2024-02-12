def order(sentence):
    words = sentence.split()
    word_dict = {}

    for word in words:
        for char in word:
            if char.isdigit():
                word_dict[int(char)] = word

    sorted_words = [word_dict[i] for i in range(1, len(words) + 1)]

    return ' '.join(sorted_words)


print(order("is2 Thi1s T4est 3a"))
