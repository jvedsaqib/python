class graphTrav:
    g = dict()

    def __init__(self, g):
        self.g = g

    def bfs(self, node):
        visited = [False] * (len(self.g))
        queue = []

        visited.append(node)
        queue.append(node)

        while queue:
            v = queue.pop(0)
            print(v, end=" ")
            for neigh in self.g[v]:
                if neigh not in visited:
                    visited.append(neigh)
                    queue.append(neigh)

    def dfs(self, visited, g, node):
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neigh in g[node]:
                self.dfs(visited, g, neigh)


if __name__ == '__main__':
    g = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }
    ob = graphTrav(g)
    ob.bfs('A')
    print()
    ob.dfs(set(), g, 'A')
