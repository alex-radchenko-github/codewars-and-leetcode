def leaderboard_sort(leaderboard, changes):
    tmp = []
    for i in changes:
        tmp.append(i.split(' '))
    for i in tmp:
        ind = leaderboard.index(i[0])
        leaderboard.pop(ind)
        leaderboard.insert(ind - int(i[1]), i[0])

    return leaderboard
print(leaderboard_sort(['John', 'Brian', 'Jim', 'Dave', 'Fred'], ['Dave +1', 'Fred +4', 'Brian -1']))#['Fred', 'John', 'Dave', 'Brian', 'Jim'])
#print(leaderboard_sort(['Bob', 'Larry', 'Kevin', 'Jack', 'Max'], ['Max +3', 'Kevin -1', 'Kevin +3']))#['Bob', 'Kevin', 'Max', 'Larry', 'Jack'])