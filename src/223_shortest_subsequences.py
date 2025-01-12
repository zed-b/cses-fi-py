def main(sub: str):
  res, s, alpha = [], set(), 'ACGT'
  for c in sub:
    s.add(c)
    if len(s) == len(alpha):
      res.append(c)
      s.clear()
  res.append(next(c for c in alpha if c not in s))
  print(''.join(res))

if __name__ == '__main__':
  main(input())