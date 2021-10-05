class graph:
    def __init__(self,vertices):
        self.V= vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    def print_graph(self):
        for i in range(self.V):
            print(self.graph[i])
    def add_edge(self,u,v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def dfs(self,s):
        visited = [False]*(self.V)
        self.dfs_util(s,visited)
    def dfs_util(self,s,visited):
        visited[s] = True
        print(s,end=' ')
        for i in range(self.V):
            if self.graph[s][i] == 1 and visited[i] == False:
                self.dfs_util(i,visited)
    
    def bfs(self,s):
        visited = [False]*(self.V)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s,end=' ')
            for i in range(self.V):
                if self.graph[s][i] == 1 and visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == '__main__':
    g = graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.dfs(2)
    g.bfs(2)