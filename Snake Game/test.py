import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
import pygame
import sys
from io import StringIO
import random

# Importing classes
from Snake import Snake
from Food import Food
from GameGUI import GameGUI
from MongoDB import MongoDB
from Game import Game

class TestSnakeGame(unittest.TestCase):

    def setUp(self):
        self.width = 640
        self.height = 480
        self.cell_size = 20
        self.snake = Snake(self.width, self.height, self.cell_size)
        self.food = Food(self.snake)
        self.game = Game()
        self.gui = GameGUI(self.width, self.height)

    def test_snake_initialization(self):
        self.assertEqual(len(self.snake.body), 1)
        self.assertEqual(self.snake.body[0], (self.width // 2, self.height // 2))
        self.assertTrue(self.snake.alive)

    def test_snake_move(self):
        initial_head = self.snake.body[0]
        self.snake.move()
        new_head = self.snake.body[0]
        self.assertNotEqual(initial_head, new_head)

    def test_snake_eat_food(self):
        initial_length = len(self.snake.body)
        self.snake.eat()
        self.snake.move()
        new_length = len(self.snake.body)
        self.assertEqual(new_length, initial_length + 1)

    def test_snake_collision_with_self(self):
        self.snake.body = [(20, 20), (20, 40), (40, 40), (40, 20), (20, 20)]
        self.snake.move()
        self.assertFalse(self.snake.alive)

    def test_snake_collision_with_wall(self):
        self.snake.body = [(self.width - self.cell_size, self.height // 2)]
        self.snake.change_direction((1, 0))
        self.snake.move()
        self.assertFalse(self.snake.alive)

    @patch('random.randint')
    def test_food_placement(self, mock_randint):
        mock_randint.return_value = 5
        food_position = self.food.place_food()
        self.assertEqual(food_position, (5 * self.snake.cell_size, 5 * self.snake.cell_size))



    def test_mongodb_save_score(self):
        mock_db = MagicMock()
        self.game.db = mock_db
        self.game.db.save_score('TestUser', 10, 20)
        self.game.db.save_score.assert_called_once_with('TestUser', 10, 20)

    def test_mongodb_get_high_scores(self):
        mock_db = MagicMock()
        self.game.db = mock_db
        self.game.db.get_high_scores.return_value = [{'nickname': 'TestUser', 'score': 10, 'board_size': 20}]
        high_scores = self.game.db.get_high_scores()
        self.assertEqual(len(high_scores), 1)
        self.assertEqual(high_scores[0]['nickname'], 'TestUser')

if __name__ == '__main__':
    unittest.main()
