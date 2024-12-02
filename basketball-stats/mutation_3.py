def bball_stats(twos: int, threes: int, shotsTaken: int):
  '''
    Forgotten Floor
  '''
    import math 
    points = (twos * 2) + (threes * 3)
    FG = str(((twos + threes) / shotsTaken) * 100) + "%"
    return [points, FG]
bball_stats
