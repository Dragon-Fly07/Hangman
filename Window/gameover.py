from Window.assets import Assets
import pygame

class gameover:
    def __init__(self, target_window, word, position):
        self.target_window = target_window
        self.word = word
        self.position = position
    
    def build(self):
        font = Assets.title_font
        font2 = Assets.subtitle_font

        text = font.render("GAME OVER", True, (255, 255, 255))
        text2 = font2.render(f"The word was {self.word}", True, (255, 255, 255))
        text3 = font2.render("Press Space to restart", True, (255, 255, 255))

        rect1 = text.get_rect().size
        rect2 = text2.get_rect().size

        self.target_window.blit(text, (self.position[0] - rect1[0]//2, self.position[1])) 
        self.target_window.blit(text2, (self.position[0] - rect2[0]//2, self.position[1]+150))
        self.target_window.blit(text3, (self.position[0] - rect2[0]//2, self.position[1]+220))
    
    def key_input(self, event_key):
        if event_key == pygame.K_SPACE:
            return True
