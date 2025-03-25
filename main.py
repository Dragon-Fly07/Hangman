import pygame

pygame.init()

window = pygame.display.set_mode((1220, 660))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    font = pygame.font.Font("src/Assets/FranklinGothic.ttf", 50)
    text = font.render("Hello world", True, (255, 255, 255))
    window.blit(text, (100, 100))
    pygame.display.flip()
pygame.quit()