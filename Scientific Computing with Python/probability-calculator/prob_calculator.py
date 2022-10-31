import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kw):
        self.contents = [k for k,v in kw.items() for i in range(v)]

    def draw(self,number):
        if number>len(self.contents):
            temp = self.contents
            self.contents = []
            return temp
        else:
            samples = random.sample(self.contents,number)
            for i in samples:
                self.contents.remove(i)
            return samples

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls = [k for k,v in expected_balls.items() for i in range(v)]
    success = 0
    for i in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        temp_expected_balls = copy.copy(expected_balls)
        samples = temp_hat.draw(num_balls_drawn)
        for j in temp_expected_balls:
            if j in samples:
                samples.remove(j)
            else:
                break
        else:
            success += 1
    return success/num_experiments