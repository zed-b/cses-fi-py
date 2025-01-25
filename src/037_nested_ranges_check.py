
# TODO: todo, either compress coords and use fenwick or code an AVL tree

from typing import Iterable

def main(ranges: Iterable[tuple[int, int]]):
  events = []
  for l, r in ranges:
    events.append((l, 's'))
    events.append((r, 'e'))
  events.sort()
