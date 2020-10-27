def mirror(list):
    return sorted(list)[:-1] + sorted(list)[::-1]

print(mirror([2, 1]))