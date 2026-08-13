class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        def addSpace(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit or 
                grid[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addSpace(r + 1, c)
                addSpace(r - 1, c)
                addSpace(r, c + 1)
                addSpace(r, c - 1)

            dist += 1
