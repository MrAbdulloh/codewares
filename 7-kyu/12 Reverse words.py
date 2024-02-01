def reverse_words(text):
    words = text.split()
    result_words = [word[::-1] for word in words]
    return " ".join(result_words)


print(reverse_words("This is an example!"))
