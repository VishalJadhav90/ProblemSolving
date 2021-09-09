class Solution:
    def __init__(self):
        pass

    def dfs(self, node):
        self.whites.remove(node)
        self.greys.add(node)
        for adjnode in self.adj[node]:
            if adjnode not in self.greys:
                return self.dfs(adjnode)
            else:
                return True
        self.greys.remove(node)
        self.blacks.add(node)
        return False

    def findCycle(self, adj):
        self.adj = adj
        self.whites = set([node for node in range(len(adj))]) #not explored
        self.greys = set() #in exploration
        self.blacks = set() #explored
        for node in range(len(adj)):
            try:
                if node in self.whites and node not in self.blacks:
                    result = self.dfs(node)
                    if result:
                        return 1
            except Exception as e:
                break
        return 0


sol = Solution()
adj = [[1, 2, 3],
       [4],
       [3],
       [4],
       [0]]

result = sol.findCycle(adj)
print("result", result)