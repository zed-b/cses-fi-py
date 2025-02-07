from typing import List

def main(arr: List[int]):
  print(max(2*max(arr), sum(arr)))   

if __name__ == "__main__":
  n = int(input())
  main(list(map(int, input().split(' '))))
