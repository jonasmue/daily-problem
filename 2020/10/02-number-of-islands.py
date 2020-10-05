class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def dfs(self, grid, x, y):
        if not self.inRange(grid, y, x):
            return
        if not grid[y][x]:
            return

        grid[y][x] = 0
        for delta in [-1, 1]:
            self.dfs(grid, x + delta, y)
            self.dfs(grid, x, y + delta)

    def numIslands(self, grid):
        num_islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if not grid[y][x]:
                    continue
                num_islands += 1
                self.dfs(grid, x, y)

        return num_islands


grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(Solution().numIslands(grid))
# 3
