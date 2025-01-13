def main(n: int):
  if 0 < n % 4 and n % 4 < 3:
    print("NO")
    return
  s1, s2 = [], []
  start = 1
  if n % 4 == 3:
    s1 = [1,2]
    s2 = [3]
    start = 4
  for i in range(start, n+1, 4):
    s1.append(i)
    s1.append(i+3)
    s2.append(i+1)
    s2.append(i+2)
  print("YES")
  print(len(s1))
  print(*s1)
  print(len(s2))
  print(*s2)

if __name__ == "__main__":
  main(int(input()))