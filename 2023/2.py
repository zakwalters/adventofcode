import re
from utils import *

def part_one():
  lines = get_input(2)
  max_allowed = { "red": 12, "green": 13, "blue": 14 }
  possible = []
  for i, line in enumerate(lines):
    _game, *draws = re.split(r'[:;,] ', line)
    for draw in draws:
      n, colour = draw.split()
      if int(n) > max_allowed[colour]:
        break
    else:
      possible.append(i + 1) # Game number is 1-indexed so add 1
  return sum(possible)

def part_two():
  lines = get_input(2)
  total_power = 0
  for line in lines:
    max_seen = { "red": 0, "green": 0, "blue": 0 }
    _game, *groups = re.split(r'[:;] ', line)
    for group in groups:
      draws = group.split(', ')
      for draw in draws:
        n, colour = draw.split()
        max_seen[colour] = max(max_seen[colour], int(n))
    total_power += max_seen["red"] * max_seen["green"] * max_seen["blue"]
  return total_power

print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
