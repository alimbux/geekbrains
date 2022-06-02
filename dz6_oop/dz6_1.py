import time
from itertools import cycle


class TrafficLight:
    __color__ = ["red", "yellow", "green"]

    def running(self):
        for color in cycle(TrafficLight.__color__):
            print(color)
            if color == "red":
                time.sleep(7)
            elif color == "yellow":
                time.sleep(3)
            else:
                time.sleep(5)


t = TrafficLight()
t.running()
