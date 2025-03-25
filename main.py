from Window.mainmenu import mainmenu
import pygame


# position of text
ypos = 330

window = pygame.display.set_mode((1220, 660))

# boolean variables
running = True
main_menu_fade_out = False
game_play_fade_in = True

while running:
    mainmenu_window = mainmenu(window, (660, ypos)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if mainmenu_window.key_input(event.key):
                print("Executing Fade out")
                main_menu_fade_out = True
    if main_menu_fade_out:
        if ypos != -500:
            ypos -= 10
        window.fill((0,0,0))

    mainmenu_window.build()
    pygame.display.flip()
pygame.quit()