class Graph:
    total_nodes = None

    def __init__(self, n):
        self.mat = []
        self.total_nodes = n
        for i in range(n):
            self.mat.append([0 for i in range(n)])

    def addEdge(self, u, v):
        self.mat[u][v] = 1
        self.mat[v][u] = 1

    def printMatrix(self):
        for i in range(self.total_nodes):
            print(self.mat[i])

    def addEdgeByFile(self):
        fo = open("edge.txt", "r")
        edge_list = []
        edge_list = fo.read()
        edge_list = edge_list.split(" ")
        for i in range(0, len(edge_list), 2):
            self.addEdge(int(edge_list[i]), int(edge_list[i + 1]))
        fo.close()

    def deleteEdge(self, u, v):
        self.mat[u][v] = 0
        self.mat[v][u] = 0

    def deleteEdgeByFile(self):
        fo = open("delete_edge.txt", "r")
        edge_list = []
        edge_list = fo.read()
        edge_list = edge_list.split(" ")
        for i in range(0, len(edge_list), 2):
            self.deleteEdge(int(edge_list[i]), int(edge_list[i + 1]))
        fo.close()


g = Graph(4)
g.printMatrix()
print()
g.addEdgeByFile()
g.printMatrix()
print()
g.deleteEdgeByFile()
g.printMatrix()
