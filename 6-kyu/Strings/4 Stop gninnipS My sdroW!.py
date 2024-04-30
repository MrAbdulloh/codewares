def spin_words(sentence):
    ## 1 method

    sentence_split = sentence.split()
    ans = []

    for i in sentence_split:
        if len(i) > 5:
            ans.append(i[::-1])
        else:
            ans.append(i)
    # return ans

    ## 2 method

    words = [word[::-1] if len(word) >= 5 else word for word in sentence_split]
    return ' '.join(words)


print(spin_words("This is another test"))
