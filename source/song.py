import pygame
import os

from . import __assets_folder__

class Song:

    def __init__(self, filename):
        self.filename = filename

    def play(self): 
        try:
            pygame.mixer.music.load(os.path.join(__assets_folder__, 'songs', self.filename))
            pygame.mixer.music.play()
        except:
            print('failed to play song')
            raise

    def stop(self):
        pygame.mixer.music.stop()

    @property
    def name(self):
        return self.filename.split('.')[0]
