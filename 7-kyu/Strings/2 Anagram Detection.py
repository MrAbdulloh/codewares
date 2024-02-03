def is_anagram(test: str, original: str) -> bool:
    return sorted(test.lower()) == sorted(original.lower())


print(is_anagram("foefet", "toffee"))