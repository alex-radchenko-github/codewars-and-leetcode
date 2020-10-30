def highFive(items):
    a = sum(list(map(lambda x: x[1], list(filter(lambda x: x[0] == 1, items))))) / len(
        list(map(lambda x: x[1], list(filter(lambda x: x[0] == 1, items)))))
    b = sum(list(map(lambda x: x[1], list(filter(lambda x: x[0] == 2, items))))) / len(
        list(map(lambda x: x[1], list(filter(lambda x: x[0] == 2, items)))))
    return [[1, int(a)], [2, int(b)]], (lambda x: x[1], list(filter(lambda x: x[0] == 1, items)))


print(highFive([[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))
