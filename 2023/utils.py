def get_input(day, split=True):
  f = open(f'./input/{day}.txt')
  return f.read().splitlines() if split else f.read()
