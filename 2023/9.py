from itertools import pairwise
from utils import *

def predict(ns):
  return 0 if all(n == 0 for n in ns) else ns[-1] + predict([b - a for (a, b) in pairwise(ns)])

def part_one():
  lines = get_input(9)
  return sum(predict(list(map(lambda n: int(n), line.split()))) for line in lines)

def part_two():
  lines = get_input(9)
  return sum(predict(list(map(lambda n: int(n), reversed(line.split())))) for line in lines)

print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
