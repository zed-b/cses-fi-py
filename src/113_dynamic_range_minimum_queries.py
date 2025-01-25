# TODO: TLE

MX = 10**10
class SegmentTree:
    class Node:
        def __init__(self, val=0):
            self.val=val
        def merge(self, l, r):
            if l and r: self.val = min(l.val,r.val)
            else: self.val = l.val if l else r.val
            return self

    def __init__(self, n, values):
        self.n = n
        self.nodes = [None] * (4 * self.n)
        self.build(0, 0, self.n-1, values)

    def build(self, at, tl, tr, values):
        if tl == tr:
          self.nodes[at] = SegmentTree.Node(next(values))
        else:
            tm = tl + (tr-tl) // 2
            self.nodes[at] = SegmentTree.Node().merge(self.build(at*2+1, tl, tm, values),
                self.build(at*2+2, tm+1, tr, values))
        return self.nodes[at]

    def _query(self, ql:int, qr:int, tat:int, tl:int, tr:int):
        if ql<=tl and tr<=qr:
            return self.nodes[tat].val
        tm = tl + (tr-tl)//2
        l = self._query(ql,qr,tat*2+1,tl, tm) if ql <= tm else MX
        r = self._query(ql,qr,tat*2+2,tm+1, tr) if tm + 1 <= qr else MX
        return min(l, r)

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
    
def main(n, nums, queries):
  seg_tree = SegmentTree(n, nums)
  res = []
  for k,l,r in queries:
    if k == 1:
      seg_tree.update(l-1, r)
    else:
      res.append(seg_tree.query(l-1, r-1))
  out_string = '\n'.join(map(str, res))
  print(out_string)

if __name__ == "__main__":
  n,q = map(int, input().split())
  main(n, map(int, input().split(' ')), (map(int, input().split()) for _ in range(q)))