import math
from utils import *

example = """Time:      7  15   30
Distance:  9  40  200"""

def quadratic(a, b, c):
  rt = math.sqrt(b**2 - 4 * a * c)
  return (
    (-b + rt) / (2 * a),
    (-b - rt) / (2 * a)
  )

def part_one():
  lines = get_input(6)
  races = list((int(t), int(d)) for t, d in zip(lines[0].split()[1:], lines[1].split()[1:]))

  """
  T is the total time allowed
  D is the distance to reach
  x is the number of ms holding the button
  x * (T - x) > D
  -x^2 + Tx > D
  -x^2 + Tx - D > 0
  """

  margin = 1
  for time, distance in races:
    lowest, highest = sorted(quadratic(-1, time, -distance))
    solutions = list(range(
      int(lowest) + 1 if lowest.is_integer() else math.ceil(lowest),
      int(highest) if highest.is_integer() else math.floor(highest) + 1
    ))
    margin *= len(solutions)
  return margin

def part_two():
  lines = get_input(6)
  time, distance = map(lambda l: int(l.replace(' ', '').split(':')[1]), lines)
  lowest, highest = sorted(quadratic(-1, time, -distance))
  return len(range(
    int(lowest) + 1 if lowest.is_integer() else math.ceil(lowest),
    int(highest) if highest.is_integer() else math.floor(highest) + 1
  ))

print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
