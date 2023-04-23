# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется
# более 1 раза, к нему добавляется количество повторений.

strin = input("Введите строку: ")


def rle(strin):
    temp = strin[0]
    count = 1
    str_final = ""
    for i in range(1, len(strin)):
        if temp == strin[i]:
            count += 1
        else:
            str_final += strin[i - 1]
            if count > 1:
                str_final += str(count)
            temp = strin[i]
            count = 1
        if i + 1 == len(strin):
            str_final += strin[i]
            if count > 1:
                str_final += str(count)
    return str_final


print(rle(strin))