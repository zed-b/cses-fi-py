class SegmentTree:
    class Node:
        def __init__(self, val):
            self.sum=val
            self.lazy=0
        def push(self, lazy):
            self.lazy+=lazy
    def __init__(self,values):
        pass
    def build(self):
        pass
            