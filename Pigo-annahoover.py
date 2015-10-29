from gopigo import *
import time

__author__ = 'annahoover'

class Pigo:

    isMoving = False
    servoPos = 90

    def __init__(self):
        print "beep beep"

    def stop(self):
        self.isMoving = False
        while stop() != 1:
            time.sleep(.1)
            print "Shoot, I can't stop myself. This not good. What do?"

    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.sleep(.1)
            print "Oh great, now I can't move. Heeeeeelp."


carl = Pigo()
carl.fwd()
time.sleep(2)
carl.stop()
