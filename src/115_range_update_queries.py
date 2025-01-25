from typing import List

class Fenwick:
  def __init__(self, n):
    self.n = n + 1
    self.vals = [0] * self.n

  def add(self, at, val):
    while at < self.n:
      self.vals[at] += val
      at += at & (-at)

  def prefix_sum(self, at):
    res = 0
    while at > 0:
      res += self.vals[at]
      at -= at & (-at)
    return res

def main(n, nums, queries: List[List[int]]):
  bit = Fenwick(n)
  res = []
  for q in queries:
    if q[0] == 1:
      bit.add(q[1], q[3])
      bit.add(q[2]+1, -q[3])
    else:
      res.append(bit.prefix_sum(q[1]) + nums[q[1]-1])
  print('\n'.join(map(str, res)))

if __name__ == "__main__":
  n,q = map(int, input().split())
  main(n, list(map(int, input().split(' '))), [list(map(int, input().split())) for _ in range(q)])