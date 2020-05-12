def storst(tall1, tall2):
    if (tall1 > tall2):
        return tall1
    return tall2

print(storst(10, 1))
print(storst(1, 10))
print(storst(10.1, 10.2))
print(storst(10, 10))