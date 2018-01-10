# Reza, TUM Informatics
# MST, Prims Algorithm

# Critical Input : You must consider the existing cables whether they produce more costly result than the MST edge list cost. 
# An intuitive way could be assigning the existing cable cost between vertices (if any) to 0.0 
# so that, that particular edge must be in the final MST edge list.

import sys
import math

class PrimsAlgo:
    
    def __init__(self):
        self.file = open("output.txt", "w")
        self.INFINITY = 100000000
        self.get_input()
    
    def reset(self):
        self.graph = {}
        self.coordinates = []
        self.visited = []
        self.cheapest_cost = []
        self.root = []
        self.mst_edge_list = {}
        self.existing_eddge_list = {}
    
    def coordinate_distance_calc(self, x1, y1, x2, y2, u, v):
        data =  math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2)*(y1 - y2))
        self.graph[u,v] = data
        self.graph[v,u] = data
    

    def minimum_weight_vertex(self, total_vertices):
        min = sys.maxsize
        min_vertex = -1
        for i in range(total_vertices):
            if((self.visited[i] == False) and (self.cheapest_cost[i] < min)):
                min = self.cheapest_cost[i]
                min_vertex = i

        return min_vertex
    
    def print_minimum_spanning_tree(self, total_vertices):
        i = 1
        cost = 0.0
        while(i < total_vertices):
            v = self.root[i]
            if(((i,v) not in self.existing_eddge_list) or ((v,i) not in self.existing_eddge_list)):
                self.mst_edge_list[i,v] = self.graph[i,v]
                cost += self.graph[i,v]
            i += 1
        #print(self.mst_edge_list)
        #self.file.write("%.2f\n" % round(cost,2))
        print('{0:.2f}'.format(cost))
          
    def prims_algorithm(self, total_vertices):
         # Let's Node 0 as the source 
         self.cheapest_cost[0] = 0
         self.root[0] = -1 # Node 0 is the root of the MST
         i = 0
         while(i < total_vertices):
             # Pick the minimum weight-edge and transfer it to the Tree
             u = self.minimum_weight_vertex(total_vertices)
             self.visited[u] = True # Mark the vertex as visited, means it is included in the MST

             # Update cheapest cost and the root of adjacent vertices
             for v in range(total_vertices):
                 if((u,v) in self.graph):
                     if((self.visited[v] == False) and (self.graph[u,v] < self.cheapest_cost[v])):
                         self.root[v] = u
                         self.cheapest_cost[v] = self.graph[u,v]
             i += 1
         self.print_minimum_spanning_tree(total_vertices)
         
    def get_input(self):
        
        for line in sys.stdin:
            self.reset()
            if(line == '\n'):
                continue

            num_buildings = int(line)
            #print(num_buildings)
            for i in range(num_buildings):
                x_cord, y_cord = map(int, input().split())
                self.visited.append(False)
                self.cheapest_cost.append(self.INFINITY)
                self.root.append(self.INFINITY)
                self.coordinates.append((x_cord, y_cord))
            i=0
            while(i < num_buildings):
                j = i + 1
                while(j < num_buildings):
                    x1, y1 = self.coordinates[i]
                    x2, y2 = self.coordinates[j]
                    self.coordinate_distance_calc(x1, y1, x2, y2, i, j)
                    j += 1
                i += 1

            # Existing connection cables Input
            exs_cable_connec = int(input())
            for i in range(exs_cable_connec):
                u, v = map(int, input().split())
                self.graph[v-1,u-1] = self.graph[u-1,v-1] = 0.0
                self.existing_eddge_list[(u-1,v-1)] = True
                self.existing_eddge_list[(v-1,u-1)] = True
                
            for key, value in self.graph:
                 self.file.write('%s %s'.format(key, value))
            #print(self.coordinates)
            #print(self.graph)
            #self.prims_algorithm(num_buildings)
        
if __name__ == '__main__':
    obj = PrimsAlgo()
