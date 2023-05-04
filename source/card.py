import pygame

from . import __assets_folder__
import os

img = pygame.image.load(os.path.join(__assets_folder__, 'images', 'card.png'))
img = pygame.transform.scale(img, (100, 100))

class Card:

    def __init__(self, pos, size, color, song):
        self._color = color
        self._pos = pos
        self._size = size
        self._clicked = False
        self.song = song

    def draw(self, screen):
        xc, yc = self.position

        left   = xc - self._size // 2
        top    = yc - self._size // 2
        width  = self._size
        height = self._size

        if not self.clicked:
            screen.blit(img, (left, top), special_flags=pygame.BLEND_ALPHA_SDL2) 
        else:
            rect = pygame.Rect(left, top, width, height)
            pygame.draw.rect(screen, 'green', rect, border_radius=10)          

    def play_song(self):
        self.song.play()

    def stop_song(self):
        self.song.stop()
        
    @property
    def clicked(self):
        return self._clicked 

    @clicked.setter 
    def clicked(self, x):
        self._clicked = x
    
    def click(self):
        if self.clicked:
            self.clicked = False
            self.color = 'red'
        else:
            self.clicked = True
            self.color = 'green'      
            self.play_song()

    @property
    def position(self):
        return self._pos

    @property
    def color(self):
        return self._color
        
    @color.setter 
    def color(self, c):
        self._color = c

    def __repr__(self):
        return f'Card(song_name={self.song.name}, position={self.position}, color={self.color})'

    def __eq__(self, other):
        if type(self) == type(other):
            if self.song.name == other.song.name and self.position != other.position:
                return True
            else:
                return False
        else:
            raise TypeError  