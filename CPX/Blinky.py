from adafruit_circuitplayground import cp
import time
cp.pixels.brightness = 0.1
while True: 
    cp.pixels.fill((0,25,0))
    time.sleep(0.367)
    cp.pixels.fill((0,0,0))
    time.sleep(0.367)
        


