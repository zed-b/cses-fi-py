def main(num: int):
  if 1 < num and num < 4:
    print("NO SOLUTION")
  else:
    for i in range(2, num+1, 2):
      print(i, end=" ")
    for i in range(1, num+1, 2):
      print(i, end=" ")
    print()

if __name__ == '__main__':
  main(int(input()))
