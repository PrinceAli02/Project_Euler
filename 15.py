size = 20
grid = [[0 for i in range (size+1)]for i in range(size+1)]

for i in range (size):
    grid[size][i] = 1
    grid[i][size] = 1


for i in range (size-1,-1,-1):
    for j in range (size-1,-1,-1):
        grid[i][j] = grid[i][j+1] + grid[i+1][j]

print (grid[0][0])