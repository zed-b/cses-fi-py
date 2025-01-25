
from typing import Iterable

# It can only decrease in size compared to initial vals: List
class RingQueue:
  def __init__(self, vals: Iterable[int]):
    self.vals = list(vals)
    self.head = 0
    self.n = len(vals)
  def __len__(self):
    return self.n
  def pop(self):
    res = self.vals[self.head]
    self.head = (self.head + 1) % len(self.vals)
    self.n = self.n - 1
    return res
  def push(self, val):
    self.vals[(self.head + self.n) % len(self.vals)] = val
    self.n += 1

def main(n):
  rq = RingQueue(range(1, n+1))
  res = []
  while len(rq):
    rq.push(rq.pop())
    res.append(rq.pop())
  print(' '.join(map(str, res)))

if __name__ == "__main__":
  main(int(input()))
  
