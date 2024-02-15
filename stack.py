class Stack():
    def __init__(self):
        self.blocks = []
    
    def push(self, item):
        self.blocks.append(item)
    
    def pop(self):
        del self.blocks[-1]



