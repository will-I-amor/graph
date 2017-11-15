class Graph:
    #graph is a dict
    def __init__(self,vertices):#vertices is int
        self.V = vertices
        self.graph = []#dict
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    #find set of an element i(path compression technique)
    def find(self,parent,i):
        if parent[i]==i:
            return i
        return self.find(parent,parent[i])
    #union of two sets of x and y
    def union(self,parent,rank,x,y):
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)
        #attach smaller rank tree under root of high rank tree(Union by rank)
        if rank[xroot]<rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        #if ranks are same, then make one as root and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    def KruskalMST(self):
        result = []#store the result MST
        i = 0 #index, for sorted edges
        e = 0 #index, for result[]
        #step 1: sort all edges(weight)
        self.graph = sorted(self.graph, key=lambda item:item[2])
        parent = [];rank = []
        #create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        #number of edges to be taken is equal to V-1
        while e<self.V-1:
            #step 2: Pick the smallest edge and + the index for next iteration
            u,v,w = self.graph[i]
            i = i+1
            x = self.find(parent,u)
            y = self.find(parent,v)
            #if include this edge doesn't cause cycle, include it
            #increment the index of result for next edge
            if x!=y:
                e = e + 1
                result.append([u,v,w])
                self.union(parent,rank,x,y)
        print("Following are the edges in the constructed MST")
        for u,v,weight in result:
            print("%d -- %d == %d" % (u,v,weight))
g = Graph(4)
g.addEdge(0,1,10)
