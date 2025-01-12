from typing import List

def main(nums: List[int]):
  res, mx = 0, nums[0]
  for a in nums[1:]:
    mx = max(mx, a)
    res += max(0, mx - a)
  print(res)

if __name__ == '__main__':
  input()
  main([int(x) for x in  input().split(' ')])
