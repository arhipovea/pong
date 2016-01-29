# Multiplayer hotchair Ping Pong

import pygame
import random


# Colors
BLACK    = (    0,    0,    0)
WHITE    = ( 0xFF, 0xFF, 0xFF)
RED      = ( 0xFF,    0,    0)


pygame.init()

# Main window
winWidth  = 640
winHeight = 480
winSize = [winWidth, winHeight]
screen = pygame.display.set_mode(winSize)

pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()
done = False


# Initialization
    # Players
    # Ball
    # Bonus

# Main loop
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
                
    # Game logic
        # Player processing

        # Imnterception player and ball
        
        # Ball moving

        # Generate bonus
 
        # Interception bonus and player


                    
    # Painting
    screen.fill(BLACK) 
    
        # Main game mode
        # Game over

    pygame.display.flip()      
    clock.tick(60)

pygame.quit()