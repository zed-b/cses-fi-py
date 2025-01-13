def main(n: int):
  res = 0
  while n:
    many = n // 5
    res, n = res + many, many
  print(res)

if __name__ == "__main__":
  main(int(input()))

