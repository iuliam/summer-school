import pygame

class Settings(object):
    """
    Game Settings class

    Members represent different settings for the game:
    resolution: resolution of the game
    background: color of the background
    mouse_enabled: enable the mouse
    """
    def __init__(self):
        """
        Initialize with default settings
        """
        # Size of the main window.
        self.resolution = (300, 300)
        # Backround color in Red Blue Green channels
        self.background = (0, 0, 0)
        # Mouse enabled
        self.mouse_enabled = True
        # Title
        self.title = "Sample Game"


class Game(object):
    """
    PyGame sample game class
    """

    def __init__(self, settings = Settings()):
        pygame.init()
        self.init_from_settings(settings)
        self.clock = pygame.time.Clock()

    def init_from_settings(self, settings):
        """
        Init game from Settings object
        """

        # Init screen.
        self.screen = pygame.display.set_mode(settings.resolution)
        pygame.display.set_caption(settings.title)
        pygame.mouse.set_visible(settings.mouse_enabled)

        # Init background.
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill(settings.background)

    def run(self):
        while True:
            self.clock.tick(60)