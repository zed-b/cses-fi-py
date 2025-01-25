from typing import List

class RMQ:
    def __init__(self, vals: List[int]):
      span, n = 1, len(vals)
      self.values = [vals]
      while True:
        nxt_span = span * 2
        if nxt_span > n:
          break
        m = n - nxt_span + 1
        nxt = [0] * m
        for i in range(m):
          nxt[i] = min(self.values[-1][i], self.values[-1][i + span])
        self.values.append(nxt)
        span = nxt_span

    def query(self, l:int, r:int):
      delta, p2 = r - l, 0
      while 1 << (p2 + 1) <= delta: p2 += 1
      return min(self.values[p2][l], self.values[p2][r - (1 << p2)])

def main(n, nums, queries):
  rmq = RMQ(nums)
  res = []
  for l,r in queries:
    res.append(rmq.query(l-1,r))
  print('\n'.join(map(str, res)))

if __name__ == "__main__":
  n,q = map(int, input().split())
  main(n, list(map(int, input().split(' '))), (map(int, input().split()) for _ in range(q)))
  