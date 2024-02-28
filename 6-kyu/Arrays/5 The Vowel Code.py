def encode(st):
    vowels = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    encoded_string = ""
    for char in st:
        if char in vowels:
            encoded_string += vowels[char]
        else:
            encoded_string += char
    return encoded_string


def decode(st):
    numbers_to_vowels = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    decoded_string = ""
    for char in st:
        if char in numbers_to_vowels:
            decoded_string += numbers_to_vowels[char]
        else:
            decoded_string += char
    return decoded_string

# 2 method

# def encode(s, t=str.maketrans("aeiou", "12345")):
#     return s.translate(t)
#
#
# def decode(s, t=str.maketrans("12345", "aeiou")):
#     return s.translate(t)


encoded_string = encode("hello")
print(encoded_string)  # Выведет: h2ll4
