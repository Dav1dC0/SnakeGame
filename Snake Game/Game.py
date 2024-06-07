import pygame
import sys
import tkinter as tk

from Food import Food
from GameGUI import GameGUI
from MongoDB import MongoDB
from Snake import Snake


class Game:
    def __init__(self):
        self.uri = "mongodb+srv://s26816:xui228@snake.ovqb4xa.mongodb.net/?retryWrites=true&w=majority&appName=Snake"
        self.db_name = "Snake"
        self.collection_name = "scores"
        self.db = MongoDB(self.uri, self.db_name, self.collection_name)

    def get_nickname_and_board_size(self):
        root = tk.Tk()
        root.title("Game Setup")
        root.geometry("300x200")

        nickname = tk.StringVar()
        board_size = tk.IntVar(value=20)

        tk.Label(root, text="Enter your nickname:").pack(pady=5)
        tk.Entry(root, textvariable=nickname).pack(pady=5)

        tk.Label(root, text="Enter board size (5-25):").pack(pady=5)
        tk.Spinbox(root, from_=5, to=25, textvariable=board_size).pack(pady=5)

        def submit():
            root.quit()

        tk.Button(root, text="Submit", command=submit).pack(pady=10)
        root.mainloop()

        return nickname.get(), board_size.get()

    def run(self):
        while True:
            nickname, board_size = self.get_nickname_and_board_size()
            width, height = board_size * 32, board_size * 24

            gui = GameGUI(width, height)
            snake = Snake(width, height, 20)
            food = Food(snake)
            score = 0

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            snake.change_direction((0, -1))
                        elif event.key == pygame.K_DOWN:
                            snake.change_direction((0, 1))
                        elif event.key == pygame.K_LEFT:
                            snake.change_direction((-1, 0))
                        elif event.key == pygame.K_RIGHT:
                            snake.change_direction((1, 0))

                if not snake.alive:
                    self.db.save_score(nickname, score, board_size)
                    high_scores = self.db.get_high_scores()
                    gui.display_end_screen(high_scores)
                    waiting = True
                    while waiting:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_r:
                                    waiting = False
                                    running = False
                                elif event.key == pygame.K_e:
                                    pygame.quit()
                                    sys.exit()

                snake.move()
                if snake.body[0] == food.position:
                    snake.eat()
                    food = Food(snake)
                    score += 1

                gui.draw_game(snake, food, score)
                gui.clock.tick(gui.FPS)




if __name__ == '__main__':
    game = Game()
    game.run()