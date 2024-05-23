import random

class Food:
    def __init__(self, snake):
        self.snake = snake
        self.position = self.place_food()

    def place_food(self):
        while True:
            position = (random.randint(0, (self.snake.width - self.snake.cell_size) // self.snake.cell_size) * self.snake.cell_size,
                        random.randint(0, (self.snake.height - self.snake.cell_size) // self.snake.cell_size) * self.snake.cell_size)
            if position not in self.snake.body:
                return position
