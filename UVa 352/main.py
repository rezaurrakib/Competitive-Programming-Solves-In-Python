# Reza, TUM Informatics
# UVa_352 
# Category : Flood Fill (Graph)

import sys

class FloodFill:

    def __init__(self):
        #self.file = open("output.txt", "w")
        self.dx = [1,-1,0,0,-1,1,1,-1] # Direction Arrays/Lists
        self.dy = [1,-1,1,-1,0,0,-1,1]   
        self.test_case = 1 # Trace the number of test_cases
        self.get_input() 

    def reset(self):
        self.num_distict_group = 0
        self.pixel_matrix = {} # A dictionary as a 2D Pixel Matrix having <key, value> as <pixel_matrix(i,j), cell_Value>
        self.visited = {}
        self.num_of_connected_cmpnt = 0

    def dfs(self, x, y):
        #print("Now visited cell(",x,y,")")

        if(self.visited[x,y] == True):
            return 0

        self.visited[x,y] = True # Mark as visited

        for i in range(8):
            new_x = self.dx[i] + x
            new_y = self.dy[i] + y
            tup = (new_x, new_y)
            if(tup in self.pixel_matrix): # Check if key/cell(i,j) exist in dictionary
               if(self.pixel_matrix[new_x, new_y] == 1 and self.visited[new_x, new_y] == False):
                   self.dfs(new_x, new_y)

    def get_input(self):
        for dimension in sys.stdin: # Take the input from the console till EOF
            self.reset()
            dimension = int(dimension)

            #create and fill the Pixel Matrix as a 2D Grid having Square Dimension 
            for i in range(dimension):
                row_data = input()
                for j in range(dimension):
                    self.pixel_matrix[i,j] = ord(row_data[j]) - 48 
                    self.visited[i,j] = False # Initially all nodes are unvisited
            
            # Run dfs() to find the connected components
            for key, value in self.pixel_matrix.items():
                if(value == 1):
                    tup = key
                    if(self.visited[tup[0], tup[1]] == False):
                        self.num_of_connected_cmpnt +=1 
                        self.dfs(tup[0],tup[1])
            #self.file.write("Image number %d contains %d war eagles.\n" % (self.test_case, self.num_of_connected_cmpnt))
            print("Image number", self.test_case, "contains", self.num_of_connected_cmpnt, "war eagles.")  
            self.test_case += 1

if __name__ == '__main__':
    obj = FloodFill()