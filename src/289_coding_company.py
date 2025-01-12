# TODO: TLE on 2 test cases!

from functools import cache
from typing import List

mod = 10**9 + 7

def main(n:int, k:int, nums: List[int]):
  nums.sort()
  @cache
  def solve(at, open, sum):
    if open < 0 or open > n - at or sum > k:
      return 0
    if at == n:
      return 1
    res = 0
    cur_sum = 0 if at == 0 else (nums[at]-nums[at-1])*open
    res = res + open * solve(at+1, open-1, sum + cur_sum)
    res = res + (open + 1) * solve(at+1, open, sum + cur_sum)
    res = res + solve(at+1, open+1, sum + cur_sum)
    return res % mod
  print(solve(0,0,0))

if __name__ == '__main__':
  n,k = map(int, input().split())
  nums = [int(x) for x in input().split()]
  main(n, k, nums)
