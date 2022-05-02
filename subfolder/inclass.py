import os
#import neighbor as nb
import subfolder.neighbor as nb

class InClass:
    def __init__(self, debug=False):
        self.filename = "file1.txt"
        self.debug = debug
    def display(self):
        if self.debug:
            print(os.getcwd())
        with open(self.filename) as f:
            for line in f:
                print(line)
    def greet_neighbor(self):
        neighbor = nb.Neighbor()
        neighbor.display() 

