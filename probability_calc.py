import copy
import random
class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for x in kwargs:
            for i in range(kwargs[x]):
                self.contents.append(x)
    def draw(self, num):
        draws = []
        if num > len(self.contents):
            return self.contents
        for x in range(num):
            rand = random.randrange(len(self.contents))
            draws.append(self.contents[rand])
            self.contents.pop(rand)
        return draws

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected = []
  #creates a list of all the balls that should be drawn
  for i, j in expected_balls.items():
    for k in range(j):
      expected.append(i)
  match = 0
  backup = copy.deepcopy(hat.contents)
  #start the experiments
  for i in range(num_experiments):
    sample = hat.draw(num_balls_drawn)
    hat.contents = copy.deepcopy(backup)
    count = 0
    #checks for balls that match within the expected and the sample lists
    for i in expected:
      for j in sample:
        if i == j:
          count += 1
          sample.pop(sample.index(j))
          break
      #checks if enough balls matched
      if count == len(expected):
        match += 1
  return match/num_experiments
