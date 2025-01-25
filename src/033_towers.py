
from bisect import bisect
from typing import Iterable

def main(nums: Iterable[int]):
  towers = []
  for a in nums:
    base = bisect(towers, a) 
    # this trick also would do an append if at end
    towers[base: base+1] = a,
  print(len(towers))

if __name__ == "__main__":
  input()
  main(map(int, input().split()))
