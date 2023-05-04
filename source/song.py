import pygame
import os

from . import __assets_folder__

class Song:

    def __init__(self, filename, song_folder):
        self.filename = filename
        self.song_folder = song_folder

    def play(self): 
        try:
            pygame.mixer.music.load(os.path.join(self.song_folder, self.filename))
            pygame.mixer.music.play()
        except:
            print('failed to play song')
            raise

    def stop(self):
        pygame.mixer.music.stop()

    @property
    def name(self):
        return self.filename.split('.')[0]
