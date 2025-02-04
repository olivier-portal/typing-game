# Import init_pygame (configs & pygame configs file)
from .init_pygame import *


def quit_button(event):
    """
    Button used to quit the game.
    :param event: The variable of the pygame event loop.
    :return: ∅
    """
    # Add button
    quit_button_image = pygame.image.load("assets/images/buttons/quit_button.png")
    quit_button = pygame.transform.scale(quit_button_image, (120, 165)).convert_alpha()
    quit_button_rect = quit_button.get_rect()
    quit_button_rect.topleft = (1050, 410)
    SCREEN.blit(quit_button, quit_button_rect)

    # Check mouse position
    x, y = pygame.mouse.get_pos()

    if quit_button_rect.collidepoint(x, y):
        quit_button = pygame.transform.scale(quit_button_image, (120 * 1.1, 165 * 1.1)).convert_alpha()
        quit_button_rect = quit_button.get_rect(topleft=(1045, 405))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            exit()

    SCREEN.blit(quit_button, quit_button_rect)
