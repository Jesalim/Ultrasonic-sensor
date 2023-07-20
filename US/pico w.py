from machine import Pin
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    signaloff = 0  # Initialize signaloff with a default value
    signalon = 0   # Initialize signalon with a default value

    while echo.value() == 0:
        signaloff = utime.ticks_us()

    while echo.value() == 1:
        signalon = utime.ticks_us()

    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

while True:
    measured_distance = ultra()
    if measured_distance <= 50:
        print("The distance from the object is ", measured_distance, "cm")
        break

    utime.sleep(1)