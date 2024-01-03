def shortest_word(s: str):
    return min(len(word) for word in s.split())


print(shortest_word('bitcoin take over the world maybe who knows perhaps'))
