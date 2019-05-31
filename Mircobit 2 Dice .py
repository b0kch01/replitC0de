# Add your Python code here. E.g.
from microbit import *
import random

one = [[Image(
        "22222:"+
        "22222:"+
        "22922:"+
        "22222:"+
        "22222:")],
        [Image(
        "22222:"+
        "29222:"+
        "22222:"+
        "22292:"+
        "22222:")],
        [Image(
        "22222:"+
        "29222:"+
        "22922:"+
        "22292:"+
        "22222:")],
        [Image(
        "22222:"+
        "29292:"+
        "22222:"+
        "29292:"+
        "22222:")],
        [Image(
        "22222:"+
        "29292:"+
        "22922:"+
        "29292:"+
        "22222:")],
        [Image(
        "22222:"+
        "29292:"+
        "29292:"+
        "29292:"+
        "22222:")]]

while True:
    if accelerometer.was_gesture("shake"):
        display.show(random.choice(one))
