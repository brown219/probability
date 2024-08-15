import random
from typing import Dict, List

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, num in kwargs.items():
            self.contents.extend([color] * num)

    def draw(self, num_balls: int) -> List[str]:
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

def experiment(hat: Hat, expected_balls: Dict[str, int], num_balls_drawn: int, num_experiments: int) -> float:
    success_count = 0

    for _ in range(num_experiments):
        # Create a copy of the hat for each experiment
        hat_copy = Hat(**{color: hat.contents.count(color) for color in hat.contents})
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count the occurrences of each color in the drawn balls
        drawn_ball_counts = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        
        # Check if the drawn balls match the expected criteria
        if all(drawn_ball_counts.get(color, 0) >= count for color, count in expected_balls.items()):
            success_count += 1

    return success_count / num_experiments
# Example test
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(f'Probability: {probability:.3f}')
