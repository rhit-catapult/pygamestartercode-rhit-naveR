#
# # import pygame
# # import sys
# #
# # pygame.init()
# #
# # # Let's create a caption for the game window
# # pygame.display.set_caption("Hello World!!!!!!")
# # # TODO 00: Change the window caption to say your name.
# #


# # screen = pygame.display.set_mode((640, 480))
# # # TODO 05: Change the window size, make sure your circle code still works.
# #
# # while True:
# #         print(event)
#
# #         if event.type == pygame.QUIT:
# #             sys.exit()
#
# #     # TODO 01: Make the background white by uncommenting the line below
# #     screen.fill(pygame.Color("Gray"))
# #
# #     # Draw things on the screen
# #
# #     # TODO 02: Try to draw a circle (any size, any color, anywhere)
# #     pygame.draw.circle( pygame.Color("Orange"), (50,50) )
# #
# #     # TODO 03: Try to draw a red circle in the middle of the screen with a radius 100
# #     #pygame.draw.circle(screen, pygame.Color("Red"), pos, radius, width(optional)  )
# #
# #     # TODO 04: Try to draw a yellow circle with the center exactly in the lower left corner of the screen, radius 10
# #     #pygame.draw.circle(screen, color, pos, radius, width(optional)  )
# #
# #
# #     pygame.display.update()
# -----------------------------------------------------
# DogBark
#
# import sys
#
#
# def main():
#
#     BLACK = pygame.Color("Black")
#     WHITE = pygame.Color("White")
#     IMAGE_SIZE = 470
#     TEXT_HEIGHT = 30
#
#     # initialize the pygame module
#     pygame.init()
#
#     # prepare the window (screen)
#     screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
#     pygame.display.set_caption("Text, Sound, and an Image")
#
#     # Prepare the image
#     # done 1: Create an image with the 2dogs.JPG image
#     image1 = pygame.image.load("2dogs.JPG")
#     # done 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
#     image1 = pygame.transform.scale(image1, (IMAGE_SIZE, IMAGE_SIZE))
#
#     # Prepare the text caption(s)
#     # done 4: Create a font object with a size 28 font.
#     font1 = pygame.font.SysFont("calibri", 28)
#     #print(pygame.font.get_fonts()) # font list
#
#     # done 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
#     caption1 = font1.render("Two Dogs", True, pygame.Color("Black"))
#
#     # Prepare the music
#     # TODO 8: Create a Sound object from the "bark.wav" file.
#     sound1 = pygame.mixer.Sound("bark.wav")
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             # TODO 9: Play the music (bark) if there's a mouse click.
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 sound1.play()
#
#         # Clear the screen and set the screen background
#         screen.fill(WHITE)
#
#         # Draw the image onto the screen
#         # done 2: Draw (blit) the image onto the screen at position (0, 0)
#         screen.blit(image1, (0, 0))
#
#         # Draw the text onto the screen
#         # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
#         screen.blit(caption1, (screen.get_width() - caption1.get_width() / 0.5, image1.get_height() + 5))
#
#         # Hint: Commands like these might be useful..
#         #          screen.get_width(), caption1.get_width(), image1.get_height()
#
#         # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.
#
#         # Update the screen
#         pygame.display.update()
#
#         gettings the mouse position
#         if event.type == pygame.MOUSEBUTTONDOWN
#             print(f"You cliked at {pygame.mouse.get_pos()}")
#
#         OOP ---> Make sprite classes
#         Objects know stuff (instance varibles)
#         Objects can do stuff (methods)
#         Example:
#            To make an object (instance) of a class call the constructor
#           class Hero:
#
# def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
#     """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
#
#     self.screen = screen
#     self.x = x
#     self.y = y
#     self.image_umbrella = pygame.image.load(with_umbrella_filename)
#     self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
#     self.last_hit_time = 0
#


#    self.screen.blit(self.image,(self.x,self.y))
#
#
# main()
# #
