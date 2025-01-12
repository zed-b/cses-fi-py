def main(n: int):
  for i in range(1, n+1):
    print(((i**2)*(i**2-1) - 8*(i-1)*(i-2)) // 2)

if __name__ == '__main__':
  main(int(input()))
