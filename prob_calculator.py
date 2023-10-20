import copy
import random
# Consider using the modules imported above.

'''
class Hat:
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    def draw(self, n):
        n = min(n, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments
'''




class Hat:
    def __init__(self, **kwargs):
        self.contents = [color for color, count in kwargs.items() for _ in range(count)]

    def draw(self, n):
        n = min(n, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    hat_copy = copy.copy(hat)  # Создаем копию шляпы перед экспериментами
    for _ in range(num_experiments):
        another_hat = copy.copy(hat_copy)  # Создаем копию шляпы для каждого эксперимента
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum(1 for color, count in expected_balls.items() if balls_drawn.count(color) >= count)
        m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments

# Ваш код инициализации шляпы и проведения эксперимента остается без изменений
'''
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2, "red": 1},
    num_balls_drawn=4,
    num_experiments=3000
)
print("Probability:", probability)
'''