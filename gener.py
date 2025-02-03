import random


def gener_key(keys: int = 1, groups: int = 5, in_group: int = 5):
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    keylist = []
    for e in range(keys):
        key = ""
        for i in range(groups):
            if i != 0:
                key += "-"
            for q in range(in_group):
                ltype = random.randint(0, 1)
                if ltype:
                    key += random.choice(digits)
                else:
                    key += random.choice(letters)
        keylist.append(key)
    return keylist[0] if len(keylist) == 1 else keylist


keys = gener_key(12)
for i in range(len(keys)):
    print(keys[i])