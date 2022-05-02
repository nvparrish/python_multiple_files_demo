import os
class OutClass:
    def __init__(self, debug=False):
        self.filename = "file1.txt"
        self.debug = debug
    def display(self):
        if self.debug:
            print(os.getcwd()) # Print the current working directory
        with open(self.filename) as f:
            for line in f:
                print(line)

