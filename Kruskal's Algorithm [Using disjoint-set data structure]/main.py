import sys
from operator import itemgetter
from operator import attrgetter

__author__ = "Reza, Technical University of Munich"
__email__ = "rakib08cse@gmail.com"

class KruskalAlgo:

    def __init__(self):
        #self.file = open("output.txt", "w")
        self.first = False
        self.get_input()

    # Inner class having the information of an egde of the Graph
    class Edge():
        def __init__(self, u, v, w):
            self.node_u = u
            self.node_v = v
            self.weight = w

        '''def __repr__(self):
             return repr((self.node_u, self.node_v, self.weight))'''

        # __getitem__ is needed because, class attributes with operator.itemgetter can't access
        # directly without implementing a __getitem__ method, as classes are basically dictionaries 
        # If not implemented, "object does not support indexing" Error occured
        def __getitem__(self, index): 
            return self.weight # Always sort against the weight attribute


    def reset(self, nodes):
        self.graph = [] # value will be the list of edges
        self.min_spanning_tree_set = []
        self.parent = [i for i in range(nodes)]
        self.node_id = {}
        self.mst_cost = 0

    def find_parent(self, node):
        if(node != self.parent[node]):
            self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def get_input(self):
        test_case = int(input())
        #input() # Blank Line before each Data Set
        #print(test_case)

        for i in range(test_case):
            input() # Blank Line before each Data Set
            vertices = int(input())
            num_of_edges = int(input())
            self.reset(vertices)
            id = 0
            for j in range(num_of_edges):
                u, v, w = map(str, sys.stdin.readline().split())
                w = int(w)
                if(u not in self.node_id):
                    self.node_id[u] = id
                    id+=1
                if(v not in self.node_id):
                    self.node_id[v] = id
                    id+=1
                edge_obj = self.Edge(self.node_id[u],self.node_id[v],w)
                self.graph.append(edge_obj)

            self.graph = sorted(self.graph, key=itemgetter(2))
            #print(self.graph)

            for obj in self.graph:
                #print(obj.node_u, obj.node_v, obj.weight)
                parent_u = self.find_parent(obj.node_u)
                parent_v = self.find_parent(obj.node_v)

                if(parent_u != parent_v):
                    self.min_spanning_tree_set.append(obj)
                    self.mst_cost+=obj.weight
                    self.parent[parent_u] = self.parent[parent_v] # Union by updating parent
               
            if(self.first == False):
                self.first = True
            else:
                print("")
                #self.file.write("\n")

            #self.file.write("%d\n" % self.mst_cost)
            print(self.mst_cost)


if __name__ == '__main__':
    obj = KruskalAlgo()