import os
class InClass:
    def __init__(self, debug=False):
        self.filename = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "file1.txt"
            )
        self.debug = debug
    def display(self):
        if self.debug:
            print(os.getcwd())
        with open(self.filename) as f:
            for line in f:
                print(line)

