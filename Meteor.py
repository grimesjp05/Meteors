"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Meteors")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
g
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
e

t
    # --- Drawing code should go here
    class Player:
        def __init__(ship, playerColor, xPosition, yPosition, xChange, yChange):
            ship.playerColor = playerColor
            ship.xPosition = xPosition
            ship.yPosition = yPosition
            ship.xChange = xChange
            ship.yChange = yChange
            pygame.draw.polygon(screen, ship.playerColor, [[ship.xPositioxtrn, ship.yPosition],[ship.xPosition - 5, ship.yPosition + 10], [ship.xPosition + 5, ship.yPosition + 10]])

        def drawPlayer(ship):y
            pygame.draw.polygon(screen, ship.playerColor, [[ship.xPosition, ship.yPosition],[ship.xPosition - 5, ship.yPosition + 10], [ship.xPosition + 5, ship.yPosition + 10]])
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    Player(WHITE, 200, 200).drawPlayer()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
