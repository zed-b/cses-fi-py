# TODO: implement lazy propagation and solve the problem
class SegmentTree:
    class Node:
        def __init__(self, val=0):
            self.val=val
        def merge(self, l, r):
            if l and r: self.val = l.val + r.val
            else: self.val = l.val if l else r.val
            return self

    def __init__(self, n, values):
        self.n = n
        self.nodes = [None] * (4 * self.n)
        self.build(0, 0, self.n-1, values)

    def build(self, at, tl, tr, values):
        self.nodes[at] = SegmentTree.Node(next(values) if tl==tr else 0)
        if tl < tr:
            tm = tl + (tr-tl) // 2
            self.nodes[at].merge(self.build(at*2+1, tl, tm, values),
                self.build(at*2+2, tm+1, tr, values))
        return self.nodes[at]

    def _query(self, ql:int, qr:int, tat:int, tl:int, tr:int):
        if ql<=tl and tr<=qr:
            return self.nodes[tat]
        tm = tl + (tr-tl)//2
        l = self._query(ql,qr,tat*2+1,tl, tm) if ql <= tm else None
        r = self._query(ql,qr,tat*2+2,tm+1, tr) if tm +1 <= qr else None
        return SegmentTree.Node().merge(l,r)

    def query(self, l, r):
        return self._query(l, r, 0, 0, self.n-1)
      
    def _update(self, pos: int, val: int, tat: int, tl:int, tr:int):
      if tl == pos and tr == pos:
        self.nodes[tat].val = val
      else:
        tm = tl + (tr-tl)//2
        if pos <= tm:
          self._update(pos,val,tat*2+1, tl, tm)
        else:
          self._update(pos,val,tat*2+2, tm+1, tr)
        self.nodes[tat].merge(self.nodes[tat*2+1], self.nodes[tat*2+2])

    def update(self, pos, val):
        self._update(pos,val,0,0,self.n-1)
            
if __name__ == "__main__":
    a = [1,2,3,4,5,6,7]
    seg = SegmentTree(a)
    print(sum(a[0:3]), seg.query(0,2).val)
    print(sum(a[3:4]), seg.query(3,3).val)
    print(sum(a[1:7]), seg.query(1,6).val)