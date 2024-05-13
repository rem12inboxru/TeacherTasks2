from typing import List, LiteralString

sid = input('Введите фразу для шифрования: ')
print(sid)


def shifr(phrase):
    phrase1 = phrase.split()
    print(phrase1)
    phrase2 = []
    for i in range(len(phrase1)):
        ph3 = list(phrase1[i])
        for j in range(0, len(phrase1[i])):
            if (65 <= ord(phrase1[i][j]) <= 90) or (
                    97 <= ord(phrase1[i][j]) <= 122):
                ph3[j] = chr(ord(phrase1[i][j]) + len(phrase1[i]))
        phrase2.append(''.join(ph3))
    #phrase1.append(phrase2)
    print(' '.join(phrase2))


shifr(sid)
