import pygame, sys
import math
import random
from button import Button


WIDTH = 1600
HEIGHT = 900

display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.image.load("assets/bg.png")


def get_font(size):
    return pygame.font.Font("assets/Nexus FPS.otf", size)

red = (255, 0, 0)
black = (0, 0, 0)

clock = pygame.time.Clock()

def play():
    display.fill("black")
    
    score = 0

    PLAY_MOUSE_POS = pygame.mouse.get_pos()

    cx = random.randint(20, WIDTH - 20)
    cy = random.randint(20, HEIGHT - 20)
    circleRadius = (20)
    pygame.draw.circle(display, (red), (cx, cy), circleRadius)

    # Play main loop
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=None, pos=(30, 15), text_input="BACK", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(display)

        score_display = Button(image=None, pos=(800, 25), text_input=f'Score: {score}', font=get_font(40), base_color="#ffea00", hovering_color="#ffea00")
        score_display.changeColor(PLAY_MOUSE_POS)
        score_display.update(display)

        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        click = pygame.mouse.get_pressed()

        sqx = (x - cx)**2
        sqy = (y - cy)**2

        if math.sqrt(sqx + sqy) < circleRadius and click[0] == 1:
            display.fill(black)
            score = score + 1
            cx = random.randint(20, WIDTH - 20)
            cy = random.randint(20, HEIGHT - 20)
            circleRadius = (20)
            pygame.draw.circle(display, (255, 0, 0), (cx, cy), circleRadius)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

            pygame.display.update()
            clock.tick(240)