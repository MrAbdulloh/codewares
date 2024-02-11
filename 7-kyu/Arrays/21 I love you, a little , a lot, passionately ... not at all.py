# def how_much_i_love_you(nb_petals):
#     if nb_petals == 1 or nb_petals % 6 == 1:
#         return "I love you"
#     elif nb_petals == 2 or nb_petals % 6 == 2:
#         return "a little"
#     elif nb_petals == 3 or nb_petals % 2 == 3:
#         return "a lot"
#     elif nb_petals == 4 or nb_petals % 2 == 4:
#         return "passionately"
#     elif nb_petals == 5 or nb_petals % 2 == 5:
#         return "madly"
#     elif nb_petals == 6 or nb_petals % 2 == 6:
#         return "not at all"

def how_much_i_love_you(nb_petals):
    if nb_petals % 6 == 1:
        return "I love you"
    elif nb_petals % 6 == 2:
        return "a little"
    elif nb_petals % 6 == 3:
        return "a lot"
    elif nb_petals % 6 == 4:
        return "passionately"
    elif nb_petals % 6 == 5:
        return "madly"
    elif nb_petals % 6 == 0:
        return "not at all"

print(how_much_i_love_you(5))  # Output: "I love you"

