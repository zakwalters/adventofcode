import math
import re
from itertools import cycle
from utils import *

def build_graph(points):
  ps = [re.findall(r'\w{3}', point) for point in points]
  graph = { curr: { "L": l, "R": r } for (curr, l, r) in ps }
  return graph

def part_one():
  directions, points = get_input(8, False).split('\n\n')
  graph = build_graph(points.splitlines())
  pos = 'AAA'
  for i, turn in enumerate(cycle(directions), 1):
    pos = graph[pos][turn]
    if pos == 'ZZZ':
      return i

def part_two():
  directions, points = get_input(8, False).split('\n\n')
  graph = build_graph(points.splitlines())
  positions = list(filter(lambda p: p[-1] == 'A', graph.keys()))
  steps_taken = []
  for start in positions:
    pos = start
    for i, turn in enumerate(cycle(directions), 1):
      pos = graph[pos][turn]
      if pos[-1] == 'Z':
        steps_taken.append(i)
        break
  return math.lcm(*steps_taken)

print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
