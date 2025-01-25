from typing import Iterable, List

class Fenwick:
  def __init__(self, n, vals: Iterable[int]):
    self.n = n + 1
    self.vals = [0] * self.n
    for index, val in enumerate(vals):
      cur = index + 1
      self.vals[cur] ^= val
      nxt = cur + (cur & (-cur))
      if (nxt < self.n):
        self.vals[nxt] ^= self.vals[cur]

  def prefix_sum(self, at):
    res = 0
    while at > 0:
      res ^= self.vals[at]
      at -= at & (-at)
    return res

def main(n, nums, queries):
  bit = Fenwick(n, nums)
  res = []
  for l,r in queries:
    res.append(bit.prefix_sum(l-1) ^ bit.prefix_sum(r))
  print('\n'.join(map(str, res)))

if __name__ == "__main__":
  n,q = map(int, input().split())
  main(n, map(int, input().split(' ')), (map(int, input().split()) for _ in range(q)))