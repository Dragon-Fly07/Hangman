from Window.mainmenu import mainmenu
from Window.window import mainwindow
from Window.gameover import gameover
from Words.select import select_word
import pygame

word = select_word().open_file().upper().strip().replace("\n", "")

# position of text
ypos = 330
ypos_gameplay = 2000
ypos_game_over = 750

window = pygame.display.set_mode((1220, 660))
pygame.display.set_caption("Hangman")

# boolean variables
running = True
mainmenu_in = False
main_menu_fade_out = False
game_play_fade_in = False
game_play_fade_out = False
game_over = False


# temp vars
input_string = []
man_order = []
component = ["head", "body", "arm-left", "arm-right", "leg-left", "leg-right"]

while running:
    mainmenu_window = mainmenu(window, (660, ypos))
    gameover_window = gameover(window, word, (660, ypos_game_over))
    main_window = mainwindow(window, (300, ypos_gameplay), word, input_string, man_order, component)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if mainmenu_window.key_input(event.key):
                main_menu_fade_out = True
                game_play_fade_in = True
            elif game_play_fade_in:
                letter = main_window.get_input(event.key)
            if game_over:
                print("executed")
                if gameover_window.key_input(event.key): 
                        mainmenu_in = True
                        game_over = False 
                        game_play_fade_in = True
                        game_play_fade_out = False
                        ypos_gameplay = 2000
                        component = ["head", "body", "arm-left", "arm-right", "leg-left", "leg-right"]
                        man_order = []
                        word = select_word().open_file().upper().strip().replace("\n", "")

    if mainmenu_in == True:
        if ypos_game_over != -1000:
            ypos_game_over -= 10
        else:
            ypos_game_over = 1000
            mainmenu_in = False

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
            man_order = []
            component = ["head", "body", "arm-left", "arm-right", "leg-left", "leg-right"]
            word = select_word().open_file().upper().replace("\n", "")
    print(word)
    if len(man_order) == 6:
        print(True)
        mainmenu_in = False
        if ypos_gameplay != -500:
            ypos_gameplay -= 10
            if ypos_game_over != 330:
                ypos_game_over -= 10
            else:
                game_over = True

    main_window.draw_input()
    main_window.draw_text()
    main_window.render_gallows()
    main_window.draw_man()
    gameover_window.build()
    mainmenu_window.build()

    pygame.display.flip()

pygame.quit()
