NBPIXELS=4

from neopixel import NeoPixel
from machine import Pin,ADC
from time import sleep_ms

np = NeoPixel(Pin(14), NBPIXELS)
adc = ADC(0)

LUMIERE_MIN = 300

while True:
    valeur=adc.read()
    print(valeur)
