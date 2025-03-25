import pygame

class Man:
    def __init__(self, target_window, components, position):
        self.components = components
        self.target_window = target_window
        self.position = position
    
    def build(self):
        for i in self.components:
            if i == "head":
                pygame.draw.circle(self.target_window, (255, 255, 255), [self.position[0], self.position[1], 45])