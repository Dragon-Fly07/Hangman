from Window.assets import Assets
from Window.man import Man
import pygame


class mainwindow:
    def __init__(self, target_window: pygame.Surface, position:tuple, word:str, input_string: list):
        self.target_window = target_window
        self.position = position
        self.word = word
        self.input_string = input_string
    
    def draw_input(self):
        for i in range(len(self.word)):
            pygame.draw.rect(self.target_window, (255, 255, 255), pygame.Rect(self.position[0]+i*65, self.position[1], 60, 10))

    def get_input(self, event_key):
        key_map = {
            pygame.K_a : "A",
            pygame.K_b : "B",
            pygame.K_c : "C",
            pygame.K_d : "D",
            pygame.K_e : "E",
            pygame.K_f : "F",
            pygame.K_g : "G",
            pygame.K_h : "H",
            pygame.K_i : "I",
            pygame.K_j : "J",
            pygame.K_k : "K",
            pygame.K_l : "L",
            pygame.K_m : "M",
            pygame.K_n : "N",
            pygame.K_o : "O",
            pygame.K_p : "P",
            pygame.K_q : "Q",
            pygame.K_r : "R",
            pygame.K_s : "S",
            pygame.K_t : "T",
            pygame.K_u : "U",
            pygame.K_v : "V",
            pygame.K_w : "W",
            pygame.K_x : "X",
            pygame.K_y : "Y",
            pygame.K_z : "Z",
        }

        if event_key in key_map:
            if key_map[event_key] in self.word:
                self.input_string.append(key_map[event_key])
            
    def draw_text(self):
        font = Assets.title_font
        for letter in self.input_string:
            text = font.render(letter, True, (255, 255, 255))
            positions = [i for i in range(len(self.word)) if self.word[i] == letter]
            rect = text.get_rect().center
            for x in positions:
                # TODO: Fix this mess
                self.target_window.blit(text, (self.position[0]+x*65 + rect[0]//2, self.position[1]-2*rect[1]))

    def render_gallows(self):
        pygame.draw.rect(self.target_window, "#06402B", pygame.Rect(self.position[0], self.position[1] - 200, 660, 10))
        pygame.draw.rect(self.target_window, "#341C02", pygame.Rect(self.position[0]*1.5, self.position[1]- 400, 10, 200))
        pygame.draw.rect(self.target_window, "#341C02", pygame.Rect(self.position[0]*1.5, self.position[1] - 400, 200, 10))
        pygame.draw.rect(self.target_window, "#341C02", pygame.Rect(self.position[0]*1.5-60, self.position[1]-400, 60, 10))
        pygame.draw.rect(self.target_window, "#341C02", pygame.Rect(self.position[0]*1.5-60, self.position[1]-400, 10, 30))
        pygame.draw.rect(self.target_window, "#ffffff", pygame.Rect(self.position[0]*1.5+195, self.position[1]-390, 5, 30))
