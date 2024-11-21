from adafruit_circuitplayground import cp   
import random

while True:
    x, y, z = cp.acceleration
    shake_threshold = 10.0
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
        for i in range (0,10):
            cp.pixels[i] = random.randint(0,25,0), random.randint(0,25,0), random.randint(0,25,0)