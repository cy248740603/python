WINDOWWIDTH = 500
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
strawberryImageRect = pygame.Rect(300, 100, 40, 40)
strawberryImage = pygame.image.load(Strawberry)
strawberryStretchedImage = pygame.transform.scale(strawberryImage, (40, 40))
pygame.display.set_caption('Hello dear')