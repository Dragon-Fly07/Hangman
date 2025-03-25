import pygame

class Man:
    def __init__(self, target_window, components, position):
        self.components = components
        self.target_window = target_window
        self.position = position

        self.limbs = pygame.image.load("src/Assets/limbs.png").convert_alpha()
    
    def build(self):
        for i in self.components:
            if i == "head":
                pygame.draw.circle(self.target_window, (255, 255, 255), [self.position[0]*1.5+196, self.position[1]-350], 10)
            elif i == "body":
                pygame.draw.rect(self.target_window, (255, 255, 255), pygame.Rect(self.position[0]*1.5+192, self.position[1]-350, 5, 50))
            elif i == "arm-left":
                arm_left = pygame.transform.scale(self.limbs, (40, 40))
                self.target_window.blit(arm_left, (self.position[0]*1.5+192, self.position[1]-340))
            elif i == "leg-left":
                leg_left = pygame.transform.scale(self.limbs, (40, 40))
                self.target_window.blit(leg_left, (self.position[0]*1.5+192, self.position[1]-308))
            elif i == "arm-right":
                arm_right = pygame.transform.flip(pygame.transform.scale(self.limbs, (40, 40)), False, True)
                self.target_window.blit(arm_right, (self.position[0]*1.5+155, self.position[1]-338))
            elif i == "leg-right":
                leg_right = pygame.transform.flip(pygame.transform.scale(self.limbs, (40, 40)), False, True)
                self.target_window.blit(arm_right, (self.position[0]*1.5+155, self.position[1]-306))
