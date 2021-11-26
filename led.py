# from rpi_ws281x import PixelStrip
from abc import ABC


class PixelStrip(ABC):

    ...

class LED:
    def __init__(self, led_strip: PixelStrip):
        pass