import pygame

class GameGUI:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.FPS = 10

    def draw_game(self, snake, food, score):
        self.win.fill((0, 0, 0))
        for segment in snake.body:
            pygame.draw.rect(self.win, (0, 255, 0), pygame.Rect(segment[0], segment[1], snake.cell_size, snake.cell_size))
        pygame.draw.rect(self.win, (255, 0, 0), pygame.Rect(food.position[0], food.position[1], snake.cell_size, snake.cell_size))

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        self.win.blit(score_text, (10, 10))
        pygame.display.update()

    def display_end_screen(self, high_scores):
        self.win.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        end_text = font.render("Game Over", True, (255, 255, 255))
        self.win.blit(end_text, (self.width // 2 - 50, self.height // 2 - 50))

        score_texts = []
        for idx, score in enumerate(high_scores[:10]):
            board_size = score.get('board_size', 'N/A')
            text = font.render(f"{idx + 1}. {score['nickname']} ({board_size}): {score['score']}", True, (0, 255, 0))
            score_texts.append(text)

        y_offset = 100
        for text in score_texts:
            self.win.blit(text, (50, y_offset))
            y_offset += 40

        restart_text = font.render("Press R to Restart or E to Exit", True, (255, 255, 255))
        self.win.blit(restart_text, (self.width // 2 - 50, self.height // 2 - 20))
        pygame.display.update()
