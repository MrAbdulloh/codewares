def duplicate_count(text):
    counts = dict()
    duplicates = 0
    for word in text.lower():
        counts[word] = counts.get(word, 0) + 1

    for values in counts.values():
        if values > 1:
            duplicates += 1
    return duplicates

# ikkita usul

    # count = {}
    # duplicates = 0
    # for word in text.lower():
    #     if word in count:
    #         count[word] += 1
    #     else:
    #         count[word] = 1
    #
    # for key in count.values():
    #     if key > 1:
    #         duplicates += 1
    # return duplicates


# print(duplicate_count("abcde"))  # 0
# print(duplicate_count("a"))  # 2
print(duplicate_count("aabBcde"))  # 2
# print(duplicate_count("indivisibility"))  # 1
# print(duplicate_count("Indivisibilities"))  # 2
# print(duplicate_count("aA11"))  # 2
# print(duplicate_count("ABBA"))  # 2
