from collections import defaultdict

def main(a: int):
  word_dict = defaultdict(int)
  for char in a:
    word_dict[char] += 1
  left, middle = [], ''
  for char, cnt in word_dict.items():
    if cnt % 2 == 1:
      if middle:
        print("NO SOLUTION")
        return
      else:
        middle = char
    for _ in range(cnt //2):
      left.append(char)
  print(''.join(left + [middle] + list(reversed(left))))

if __name__ == '__main__':
  main(input())
