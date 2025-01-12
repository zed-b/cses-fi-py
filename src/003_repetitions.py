def main(dna: str):
  cur, cnt, res = 'z', 0, 0
  for c in dna:
    if c == cur: cnt = cnt + 1
    else: res, cur, cnt = max(res, cnt), c, 1
  print(max(res, cnt))

if __name__ == '__main__':
  main(input())
