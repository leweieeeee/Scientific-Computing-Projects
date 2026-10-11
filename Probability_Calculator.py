import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for color, count in kwargs.items():
            for i in range (count):
                self.contents.append(color)

    def draw(self,count):
        if count > len(self.contents):
            sample = self.contents
            self.contents = []
            return sample
        else:
            sample = random.sample(self.contents,count)
            for ball in sample:
                self.contents.remove(ball)
            return sample


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):   
    success = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        print(draw)
        if all(
            draw.count(color) >= amount
            for color, amount in expected_balls.items()
        ):
            success += 1
    print(success)
    return (success/num_experiments)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=100)
print(probability)