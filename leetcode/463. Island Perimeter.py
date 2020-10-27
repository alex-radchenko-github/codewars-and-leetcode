def islandPerimeter(grid):
    rez = 0
    for i in range(len(grid)):
        for i1 in range(len(grid[0])):
            if grid[i][i1] == 1:
                rez += 4
                print(i, i1, "+4")
                if i1 > 0 and grid[i][i1 - 1] == 1:
                    rez -= 2
                if i > 0 and grid[i - 1][i1] == 1:
                    rez -= 2

    return rez


print(islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))  # 16
print(islandPerimeter([[1]]))  # 4

# [0,1,0,0]
# [1,1,1,0]
# [0,1,0,0]
# [1,1,0,0]

# 0-0 0-1 0-2 0-3
# 1-0 1-1 1-2 1-3
# 2-0 2-1 2-2 2-3
# 3-0 3-1 3-2 3-3
