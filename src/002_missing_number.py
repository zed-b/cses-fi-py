from typing import List

def main(n: int, a: List[int]):
  x = 0
  for i in range(n + 1):
    x ^= i
  for num in a:
    x ^= num
  print(x)

if __name__ == '__main__':
  main(int(input()), [int(x) for x in input().split(' ')])
