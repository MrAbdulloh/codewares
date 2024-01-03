def friend(x: list):
    friend_name = [name for name in x if len(name) == 4]
    return friend_name

print(friend(["Ryan", "Kieran", "Mark"]))
