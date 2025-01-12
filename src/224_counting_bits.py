def main(a: int):
  res = 0
  step = 2
  while True:
    add = a // step * (step // 2)
    if a % step >= step // 2:
      add += a % step - step // 2 + 1
    if add == 0:
      break
    res += add
    step *= 2
  print(res)

if __name__ == '__main__':
  main(int(input()))