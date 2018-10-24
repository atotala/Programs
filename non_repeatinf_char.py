x = input()
char  = {}
for i in x:

    val = char.get(i)
    if val is None:
        val = 0
    val = val + 1
    char[i] = val

for key, values in char.items():
        if values == 1:
                non_repeat = key
                break
print(non_repeat)

