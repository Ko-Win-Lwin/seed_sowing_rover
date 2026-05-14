from machine import Pin, PWM
import time

servo = PWM(Pin(9))
servo.freq(50)

# safer values
OPEN = 5200
CLOSE = 4200


def drop_seed():

    # open gate
    servo.duty_u16(OPEN)
    time.sleep(0.25)

    # close gate
    servo.duty_u16(CLOSE)
    time.sleep(0.25)
