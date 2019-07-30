import pygame
import time
from control import Control
from snake import Snake
from gui import Gui
from food import Food

pygame.init()
window = pygame.display.set_mode((441, 441))
pygame.display.set_caption("Snake")
control = Control()
snake = Snake()
food = Food()
gui = Gui()
gui.init_field()
food.generate_food_position(gui)

while control.flag_game:
    gui.check_win_or_lose()
    control.control()
    window.fill(pygame.Color("Black"))
    if gui.game == "GAME":
        snake.draw_snake(window)
        food.draw_food(window)
        if not control.flag_pause:
            snake.move(control)
            snake.check_barrier(gui)
            snake.eat(food, gui)
            snake.check_end_window()
            snake.animation()
        gui.draw_progress(window)
        gui.draw_level(window)
    elif gui.game == "WIN":
        gui.draw_win(window)
    elif gui.game == "LOSE":
        gui.draw_lose(window)
    pygame.display.flip()
    time.sleep(0.1)
pygame.quit()
