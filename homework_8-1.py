"""
1. Определение количества различных подстрок с использованием хэш-функции.
   Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
   Требуется найти количество различных подстрок в этой строке.
"""


from hashlib import sha1


def sub_str_count(string: str):
    str_length = len(string)

    is_counted = [
        string
    ]
    substrings = {}

    # формируем подстроки
    for pos in range(str_length):
        for width in range(pos + 1, str_length + 1):
            subs = string[pos:width]
            if subs not in is_counted and subs not in substrings:
                substrings[subs] = 0

    for patt in substrings:
        patt_length = len(patt)
        patt_hash = sha1(patt.encode("utf-8")).hexdigest()
        for i in range(str_length - patt_length + 1):
            subs_hash = sha1(string[i:i + patt_length].encode("utf-8")).hexdigest()
            if subs_hash == patt_hash:
                substrings[patt] += 1

    return substrings


text = input("Введите строку латинских букв: ").lower()

result = sub_str_count(text)
print(result)
print(f"Количество подстрок {sum(x for x in result.values())}")
