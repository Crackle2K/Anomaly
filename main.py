import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Anomaly")


BLACK = (0, 0, 0)
WHITE = (230, 230, 230)
GOLD = (212, 175, 55)
RED = (150, 20, 20)


font = pygame.font.Font(None, 40)  
title_font = pygame.font.Font(None, 60)


prompt = "You hear footsteps echoing... Do you hide or run?"
option1 = "Hide in the shadows"
option2 = "Run down the corridor"

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)


def button(text, x, y, w, h, color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

    draw_text(text, font, WHITE, screen, x + w//2, y + h//2)


def hide_action():
    print("You hide... The Anomaly passes by.")


def run_action():
    print("You run... The Anomaly hears you!")


running = True
while running:
    screen.fill(BLACK)

    draw_text("The Anomaly", title_font, GOLD, screen, WIDTH//2, 100)
    draw_text(prompt, font, WHITE, screen, WIDTH//2, 200)

    button(option1, 200, 400, 180, 60, RED, GOLD, hide_action)
    button(option2, 420, 400, 180, 60, RED, GOLD, run_action)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
