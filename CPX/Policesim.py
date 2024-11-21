from adafruit_circuitplayground import cp   
import time    



  
while True:
    cp.pixels.fill((25, 0, 0))
    time.sleep(0.500)
    cp.pixels.fill((0, 0, 25))
    time.sleep(0.500)
    cp.pixels.fill((25, 0, 0))
    time.sleep(0.500)
    cp.pixels.fill((0, 0, 25))
    time.sleep(0.500)
    cp.pixels.fill((25, 0, 0))
    time.sleep(0.500)
    cp.pixels.fill((0, 0, 25))
    time.sleep(0.500)
    cp.pixels.fill((25, 0, 0))
    time.sleep(0.500)
    cp.pixels.fill((0, 0, 25))
    time.sleep(0.500)

    notes = [(500, 0.5), (900, 0.5), (500, 0.5), (900, 0.5)]  

    for frequency, duration in notes:
        cp.play_tone(frequency, duration)
    time.sleep(0.75)  