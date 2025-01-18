from itertools import accumulate, chain
import sys

def main(nums: list[int], queries):
  prefix_sum = list(accumulate(chain([0],nums)))
  res = []
  for l,r in queries:
    res.append(str(prefix_sum[r] - prefix_sum[l-1]))
  sys.stdout.write('\n'.join(res) + '\n')

if __name__ == "__main__":
  n,q = map(int, input().split())
  main((map(int, input().split())), (map(int, input().split()) for _ in range(q)))