from adafruit_circuitplayground import cp
import time

while True: 
   if cp.button_a:
      for i in range(0,10):
            cp.pixels[i] = (0,225,0)
            time.sleep(0.100)
            cp.pixels[i] = (0,0,0)  
            while cp.button_a:
                pass