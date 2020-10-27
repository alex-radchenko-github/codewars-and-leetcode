import random
import string
import time


def solution1(S):
    start_time = time.time()
    d = {'B': 0, 'A': 0, 'L': 0, 'O': 0, 'N': 0}  # словарь для подсчета букв. ключ и кол-во таких букв
    for x in d:  # заполняем словарь
        d[x] = S.count(x)
    key_min = min(d.keys(), key=(lambda k: d[k]))  # находим букву с минимальным количеством вхождений
    if (d['O'] / 2 > d[key_min]) and (d['L'] / 2 > d[key_min]):  # Если удвоенное кол-во О или L встречаeтся чаще чем
        # другая буква,
        return int(d[key_min]), "--- %s seconds ---" % (
                    time.time() - start_time)  # то возвращаем минимальное количество
    else:
        return min(int(d['O'] / 2), int(d['L'] / 2)), "--- %s seconds ---" % (
                    time.time() - start_time)  # иначе возвращаем минимальное количество из O или L (деленное на 2)


# def solution(str):
#    sw = True
#    str = list(str)
#    rez = 0
#    while sw:
#        try:
#            for i in list("BALLOON"):
#                str.remove(i)
#            rez += 1
#            sw = True
#        except ValueError:
#            return rez
#    return rez


def solution2(s):
    start_time = time.time()
    x1 = []
    for x in list("BANLO"):
        x1.append(s.count(x))
    if (min(x1[3:])) / 2 > min(x1[:3]):
        return int(min(x1[:3])), "--- %s seconds ---" % (time.time() - start_time)
    else:
        return int(min(x1[3:]) / 2), "--- %s seconds ---" % (time.time() - start_time)


def solution3(s):
    start_time = time.time()
    return int(min((s.count("B"), s.count("A"), s.count("N"), s.count("L")/2, s.count("O")/2,))), "--- %s seconds ---" % (time.time() - start_time)

def solution4(s):
    start_time = time.time()
    return int(min([s.count("B"), s.count("A"), s.count("N"), s.count("L")/2, s.count("O")/2])), "--- %s seconds ---" % (time.time() - start_time)

s = ''.join(random.choices(string.ascii_uppercase, k=10000000))

print(solution3('BAONXXOLL'))# 1 BAONXXOLL
print(solution3('BAOOLLNNOLOLGBAX'))  # 2 BAOOLLNNOLOLGBAX
print(solution3('BAAALLLLOOOOOOXXNNN')) #1
print(solution3('BALLOON')) #1
print(solution3('BALLOONXX')) #1
print(solution3('AAALLLLOOOOOOXXNNN')) #0
print(solution3('BALLON')) #0
print(solution1(s))  # 0
print(solution2(s))  # 0
print(solution3(s))  # 0
print(solution4(s))  # 0
