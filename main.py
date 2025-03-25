from Window.mainmenu import mainmenu
from Window.window import mainwindow
import pygame

# position of text
ypos = 330
ypos_gameplay = 2000

window = pygame.display.set_mode((1220, 660))
pygame.display.set_caption("Hangman")

# boolean variables
running = True
main_menu_fade_out = False
game_play_fade_in = False
game_play_fade_out = False


# temp vars
input_string = []

while running:
    word = "MISSISIPPI"
    mainmenu_window = mainmenu(window, (660, ypos)) 
    main_window = mainwindow(window, (300, ypos_gameplay), word, input_string)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if mainmenu_window.key_input(event.key):
                main_menu_fade_out = True
                game_play_fade_in = True
            if game_play_fade_in:
                letter = main_window.get_input(event.key)

    if main_menu_fade_out:
        if ypos != -500:
            ypos -= 10
        window.fill((0,0,0))
    
    if game_play_fade_in:
        if ypos_gameplay != 500:
            ypos_gameplay -= 10 

    if set(input_string) == set(word):
        game_play_fade_out = True
    
    if game_play_fade_out:
        if ypos_gameplay != -500:
            ypos_gameplay -= 10
        else:
            ypos_gameplay = 2000
            game_play_fade_in = True
            game_play_fade_out = False
            input_string = []

    main_window.draw_input()
    main_window.draw_text()
    main_window.render_gallows()
    mainmenu_window.build()
    
    pygame.display.flip()

pygame.quit()
