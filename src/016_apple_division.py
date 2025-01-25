from typing import List

def main(nums: List[int]):
  n = len(nums)
  partial = [0] * (1<<n)
  sum = 0
  for i in range(n):
    partial[1<<i] = nums[i]
    sum += nums[i]

  best = sum
  for i in range(1, 1<<n):
    lsb = i & -i
    cur = partial[lsb] + partial[i ^ lsb]
    diff = abs(sum - cur * 2)
    if diff < best:
      best = diff
    partial[i] = cur

  print(best)

if __name__ == "__main__":
  input()
  main(list(map(int, input().split())))
