from typing import List

def main(nums: List[List[int]]):
  for a,b in nums:
    print("YES" if min(a,b) * 2 >= max(a,b) and (a+b) % 3 == 0 else "NO")

if __name__ == "__main__":
  n = int(input())
  main([[int(x) for x in input().split()] for _ in range(n)])