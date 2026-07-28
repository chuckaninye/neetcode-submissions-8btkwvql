class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = defaultdict(list)
        visited = set()

        for pre, crs in prerequisites:
            adjList[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False
            if adjList[crs] == []:
                return True

            visited.add(crs)
            for c in adjList[crs]:
                if not dfs(c): return False
            
            visited.remove(crs)
            adjList[crs] = []
            
            return True
        
        for pre, crs in prerequisites:
            if not dfs(crs): return False
        
        return True
