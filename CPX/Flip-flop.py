from adafruit_circuitplayground import cp


while True:
    if cp.switch:
        print("Switch is on the True")
        cp.pixels[0]
    else:
        print("Switch is on the False")
        cp.pixels[5]
    
