def main(n: int):
  digits = ['0', '1']
  buf = [0]*n
  for i in range(1 << n):
    gray = i ^ (i >> 1)
    for at in range(n):
      buf[n-at-1] = digits[(gray >> at) & 1]
    print(''.join(buf))

if __name__ == "__main__":
  main(int(input()))
