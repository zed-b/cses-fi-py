from typing import Optional


class Node:
  def __init__(self, val):
    self.val, self.cnt = val, 1
    self.adj = [None, None]

def cnt(node: Optional[Node]):
  return 0 if not node else node.cnt

class NumTree:
  def __init__(self, mx):
    self.end = Node(1e9)
    self.end.adj[0] = self.build(1, mx)

  def build(self, left, right):
    if (left > right):
      return None
    m = left + (right - left) // 2
    at = Node(m)
    at.adj[0:2] = self.build(left, m-1), self.build(m+1, right)
    at.cnt = 1 + cnt(at.adj[0]) + cnt(at.adj[1])
    return at

  def __len__(self):
    return cnt(self.end.adj[0])

  def pop(self, pos):
    par, dir, at = self.end, 0, self.end.adj[0]
    while True:
      at.cnt -= 1
      cnt_left = cnt(at.adj[0])
      if cnt_left == pos:
        break
      if cnt_left > pos:
        dir = 0
      else:
        dir, pos = 1, pos - cnt_left-1
      par, at = at, at.adj[dir]
    res = at.val
    # swap if needed
    if at.adj[0] and at.adj[1]:
      pred_par, pred_dir, pred = at, 0, at.adj[0]
      while pred.adj[1]:
        pred.cnt -=  1
        pred_par, pred_dir, pred = pred, 1, pred.adj[1]
      pred_par.adj[pred_dir] = pred.adj[0]
      at.val = pred.val
    # else it's easy
    elif par:
      if at.adj[0]:
        par.adj[dir] = at.adj[0]
      else:
        par.adj[dir] = at.adj[1]
    return res

def main(n,q):
  tree = NumTree(n)
  res = []
  at, hop = 0, q
  while n:
    at = (at + hop) % n
    res.append(tree.pop(at))
    n -= 1
  print(' '.join(map(str, res)))

if __name__ == "__main__":
  main(*map(int,input().split(' ')))