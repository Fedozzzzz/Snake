import pygame


class Snake:
    def __init__(self):
        self.RECT_SIZE = 10
        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]

    def move(self, control):
        move = self.RECT_SIZE + 1
        if control.flag_direction == "RIGHT":
            self.head[0] += move
        elif control.flag_direction == "LEFT":
            self.head[0] -= move
        elif control.flag_direction == "UP":
            self.head[1] -= move
        elif control.flag_direction == "DOWN":
            self.head[1] += move

    def animation(self):
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw_snake(self, window):
        for segment in self.body:
            pygame.draw.rect(window, pygame.Color("Green"),
                             pygame.Rect(segment[0], segment[1], self.RECT_SIZE, self.RECT_SIZE))

    def check_end_window(self):
        if self.head[0] == 419:
            self.head[0] = 23
        elif self.head[0] == 12:
            self.head[0] = 419
        elif self.head[1] == 23:
            self.head[1] = 419
        elif self.head[1] == 419:
            self.head[1] = 34

    def eat(self, food, gui):
        if self.head == food.food_position:
            self.body.append(food.food_position)
            food.generate_food_position(gui)
            gui.get_new_progress()

    def check_barrier(self, gui):
        if self.head in gui.barrier or self.head in self.body[1:]:
            self.body.pop()
            gui.progress.pop()

