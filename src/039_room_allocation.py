#TODO: TLE

from collections import deque
from typing import Iterable, List

def main(arr: Iterable[List[int]]):
  events = []
  for i, [l,r] in enumerate(arr):
    events.append((l,'b',i))
    events.append((r,'e',i))

  results = [0] * (len(events) // 2)
  taken, free = 0, deque()

  events.sort()
  for at, ev, i in events:
    if ev == 'b':
      if not len(free):
        free.append(taken+1)
      results[i] = free.popleft()
      taken += 1
    else:
      taken -= 1
      free.append(results[i])
  
  print(len(free))
  print(' '.join(map(str,results)))

if __name__ == "__main__":
  n = int(input())
  main((map(int, input().split()) for _ in range(n)))
