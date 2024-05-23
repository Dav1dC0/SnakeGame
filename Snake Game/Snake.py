class Snake:
    def __init__(self, width, height, cell_size):
        self.body = [(width // 2, height // 2)]
        self.direction = (1, 0)
        self.grow = False
        self.alive = True
        self.cell_size = cell_size
        self.width = width
        self.height = height

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx * self.cell_size, head_y + dy * self.cell_size)

        if new_head in self.body or not (0 <= new_head[0] < self.width and 0 <= new_head[1] < self.height):
            self.alive = False
        else:
            self.body.insert(0, new_head)
            if not self.grow:
                self.body.pop()
            self.grow = False

    def change_direction(self, new_direction):
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
            self.direction = new_direction

    def eat(self):
        self.grow = True
