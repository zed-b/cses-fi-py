#TODO: TLE

from array import array


class Fenwick:
  def __init__(self, n):
    self.n = n + 1
    self.vals = array('l', (0 for _ in range(self.n)))
    self.sz = 0

  def add(self, at, val):
    self.sz += val
    while at < self.n:
      self.vals[at] += val
      at += at & (-at)

  def prefix_sum(self, at):
    res = 0
    while at > 0:
      res += self.vals[at]
      at -= at & (-at)
    return res

def solve(arr):
  n = len(arr)
  coords_set = set()
  for l,r in arr:
    coords_set.add(l)
    coords_set.add(r)
  decomp = sorted(coords_set)
  comp = {v: k for k, v in enumerate(decomp)}

  events = []
  for i,[l,r] in enumerate(arr):
    events.append((l,i,'b'))
    events.append((r,i,'e'))

  events.sort()

  over = array('l', (0 for _ in range(n)))
  under = array('l', (0 for _ in range(n)))

  cur,passed, l = Fenwick(len(comp)), Fenwick(len(comp)), 0

  for r in range(n*2+1):
    while r < n*2 and events[l][0] < events[r][0] or r == n*2 and l < r:
      [lpos, lindex, levent] = events[l]
      if levent == 'e':
        lbegin = comp[arr[lindex][0]]
        cur.add(lbegin + 1, -1)
        over[lindex] = 1 if passed.sz - passed.prefix_sum(lbegin) - 1 > 0 else 0
      l += 1
    if r == n * 2: break
    [rpos, rindex, revent] = events[r]
    if revent == 'b':
      cur.add(comp[rpos]+1, 1)
    elif revent == 'e':
      rbegin = comp[arr[rindex][0]]
      under[rindex] = 1 if cur.prefix_sum(rbegin+1) - 1 > 0 else 0
      passed.add(rbegin+1, 1)

  print(' '.join(map(str,over)))
  print(' '.join(map(str,under)))


if __name__ == "__main__":
  n = int(input())
  arr = [list(map(int, input().split())) for _ in range(n)]
  solve(arr)

