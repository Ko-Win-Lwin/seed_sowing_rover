from machine import Pin
import utime

trig = Pin(18, Pin.OUT)
echo = Pin(19, Pin.IN)


def get_distance():

    trig.low()
    utime.sleep_us(2)

    trig.high()
    utime.sleep_us(10)
    trig.low()

    timeout = utime.ticks_us()

    while echo.value() == 0:

        if utime.ticks_diff(
            utime.ticks_us(),
            timeout
        ) > 30000:

            return -1

    start = utime.ticks_us()

    timeout = utime.ticks_us()

    while echo.value() == 1:

        if utime.ticks_diff(
            utime.ticks_us(),
            timeout
        ) > 30000:

            return -1

    end = utime.ticks_us()

    distance = (end - start) * 0.0343 / 2

    return distance
