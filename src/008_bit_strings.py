mod = 10**9 + 7

def main(n: int):
  res, base = 1, 2
  while n:
    if n % 2:
      res = (res * base) % mod
    base = (base * base) % mod
    n //= 2
  print(res)

if __name__ == "__main__":
  main(int(input()))