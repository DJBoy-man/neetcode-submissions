class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        if not n:
            return 0
        
        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()
        
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)

            for nei in adj[i]:
                dfs(nei)
        
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)

        return count

        